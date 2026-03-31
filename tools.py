"""Aha! MCP Server — 10 unified tools replacing 78 endpoint-per-tool wrappers.

Design spec: docs/simplified-tool-design.md
Follows: https://www.anthropic.com/engineering/writing-tools-for-agents
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from fastmcp import Context, FastMCP

from fastmcp.exceptions import ToolError

from client import check_auth, graphql, rest_api
from errors import (
    AhaError, AhaNotFoundError, AhaValidationError,
    raise_tool_error, tool_error_from_message,
)
from formatting import format_description, format_response_field
from resolver import detect_record_type, resolve_identifier
from cache import cached

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# GraphQL field fragments — reused across queries
# ---------------------------------------------------------------------------

CONCISE_FIELDS = {
    "feature": "id referenceNum name workflowStatus { name } assignedToUser { name }",
    "idea": "id referenceNum name workflowStatus { name } assignedToUser { name }",
    "epic": "id referenceNum name workflowStatus { name } assignedToUser { name }",
    "initiative": "id referenceNum name workflowStatus { name } assignedToUser { name }",
    "release": "id referenceNum name developmentStartedOn endOn owner { name }",
    "goal": "id referenceNum name color project { name }",
    "requirement": "id referenceNum name workflowStatus { name } assignedToUser { name }",
    "page": "id referenceNum name",
    "task": "id name body { htmlBody } dueDate status assignedToUser { name }",
    "key_result": "id name progress",
    "comment": "id body { htmlBody } createdAt user { name }",
    "project": "id name description { htmlBody }",
}

DETAILED_FIELDS = {
    "feature": """id referenceNum name
        description { htmlBody }
        workflowStatus { id name }
        assignedToUser { id name email }
        release { id referenceNum name }
        epic { id referenceNum name }
        team { id name }
        tags { id name color }
        originalEstimate { text value }
        remainingEstimate { text value }
        workDone { text value }
        score dueDate startDate
        createdAt updatedAt""",
    "idea": """id referenceNum name
        description { htmlBody }
        workflowStatus { id name }
        assignedToUser { id name email }
        project { id name }
        score visibility promotableId
        tags { id name color }
        createdAt updatedAt""",
    "epic": """id referenceNum name
        description { htmlBody }
        workflowStatus { id name }
        assignedToUser { id name email }
        release { id referenceNum name }
        project { id name }
        tags { id name color }
        createdAt updatedAt""",
    "initiative": """id referenceNum name
        description { htmlBody }
        workflowStatus { id name }
        assignedToUser { id name email }
        project { id name }
        createdAt updatedAt""",
    "release": """id referenceNum name
        developmentStartedOn endOn parkingLot
        owner { id name email }
        project { id name }
        createdAt updatedAt""",
    "goal": """id referenceNum name
        metricName color
        project { id name }
        parent { id referenceNum name }
        createdAt createdByUser { id name }""",
    "requirement": """id referenceNum name
        description { htmlBody }
        workflowStatus { id name }
        assignedToUser { id name email }
        feature { id referenceNum name }
        position originalEstimate remainingEstimate workDone
        createdAt""",
    "page": """id referenceNum name
        description { htmlBody }
        parent { id referenceNum name }
        createdAt updatedAt""",
    "task": """id name body { htmlBody }
        dueDate status
        assignedToUser { id name email }
        createdAt updatedAt""",
    "key_result": "id name progress createdAt updatedAt",
    "comment": """id body { htmlBody }
        createdAt updatedAt
        user { id name email }""",
    "project": """id name
        description { htmlBody }
        color childrenCount
        backlogManagementEnabled epicsEnabled
        defaultRelease { id referenceNum name }
        defaultUser { id name email }
        goalsCount developTeamsCount
        createdAt updatedAt""",
}

# Singular GraphQL root field names
GQL_SINGULAR = {
    "feature": "feature", "idea": "idea", "epic": "epic",
    "initiative": "initiative", "release": "release", "goal": "goal",
    "requirement": "requirement", "page": "page", "task": "task",
    "key_result": "keyResult", "comment": "comment", "project": "project",
}

# Plural GraphQL root field names (for list queries)
GQL_PLURAL = {
    "feature": "features", "idea": "ideas", "epic": "epics",
    "initiative": "initiatives", "release": "releases", "goal": "goals",
    "requirement": "requirements", "page": "pages", "task": "tasks",
    "key_result": "keyResults", "comment": "comments", "project": "projects",
    "user": "users", "workflow": "workflows", "tag": "tags",
    "custom_field": "customFields",
}

# Mutation name stems — createFeature, updateFeature, deleteFeature, etc.
GQL_MUTATION_TYPE = {
    "feature": "Feature", "idea": "Idea", "epic": "Epic",
    "initiative": "Initiative", "release": "Release", "goal": "Goal",
    "requirement": "Requirement", "page": "Page", "task": "Task",
    "key_result": "KeyResult", "comment": "Comment",
    "record_link": "RecordLink",
}

# Record types that require a project context for creation
REQUIRES_PROJECT = {"feature", "idea", "epic", "release", "page", "requirement"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _require_auth():
    """Check auth, raising ToolError if credentials are missing."""
    try:
        check_auth()
    except AhaError as e:
        raise_tool_error(e)


def _fields_for(record_type: str, response_format: str) -> str:
    """Pick concise or detailed field set for a record type."""
    source = CONCISE_FIELDS if response_format == "concise" else DETAILED_FIELDS
    return source.get(record_type, "id name")


def _format_output(data: Any, content_format: str = "markdown") -> str:
    """Serialize result to JSON, converting HTML descriptions to Markdown if requested."""
    if content_format == "markdown" and isinstance(data, (dict, list)):
        data = _convert_html_fields(data)
    return json.dumps(data, indent=2, default=str)


def _convert_html_fields(obj: Any) -> Any:
    """Recursively convert htmlBody fields from HTML to Markdown in a data structure."""
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if k == "htmlBody" and isinstance(v, str):
                result[k] = format_response_field(v, "markdown")
            elif isinstance(v, (dict, list)):
                result[k] = _convert_html_fields(v)
            else:
                result[k] = v
        return result
    elif isinstance(obj, list):
        return [_convert_html_fields(item) for item in obj]
    return obj


def _mutation_error(result: dict) -> Optional[str]:
    """Extract human-readable error from a mutation result, or None if OK."""
    errors = result.get("errors")
    if errors and errors.get("attributes"):
        msgs = []
        for attr in errors["attributes"]:
            name = attr.get("name", "unknown")
            details = ", ".join(attr.get("fullMessages", []))
            msgs.append(f"  {name}: {details}")
        return "Validation errors:\n" + "\n".join(msgs)
    return None


def _build_attributes(
    name: Optional[str] = None,
    description: Optional[str] = None,
    assignee: Optional[str] = None,
    status: Optional[str] = None,
    tags: Optional[List[str]] = None,
    parent: Optional[str] = None,
    release: Optional[str] = None,
    due_date: Optional[str] = None,
    project: Optional[str] = None,
    extra_fields: Optional[Dict[str, Any]] = None,
    content_format: str = "markdown",
) -> Dict[str, Any]:
    """Build a mutation attributes dict from common parameters.

    Only includes keys for non-None values so partial updates work.
    """
    attrs: Dict[str, Any] = {}
    if name is not None:
        attrs["name"] = name
    if description is not None:
        attrs["description"] = format_description(description, content_format)
    if assignee is not None:
        # Accept email (contains @) or ID
        if "@" in assignee:
            attrs["assignedToUser"] = {"email": assignee}
        else:
            attrs["assignedToUser"] = {"id": assignee}
    if status is not None:
        attrs["workflowStatus"] = {"id": status}
    if tags is not None:
        attrs["tagList"] = ", ".join(tags)
    if parent is not None:
        attrs["epic"] = {"id": parent}  # most common parent relationship
    if release is not None:
        attrs["release"] = {"id": release}
    if project is not None:
        attrs["project"] = {"id": project}
    if due_date is not None:
        attrs["dueDate"] = due_date
    if extra_fields:
        attrs.update(extra_fields)
    return attrs


# ---------------------------------------------------------------------------
# Tool registration
# ---------------------------------------------------------------------------

mcp: Optional[FastMCP] = None


def register_tools(mcp_instance: FastMCP):
    """Register all 10 tools with the MCP instance."""
    global mcp
    mcp = mcp_instance

    # Read-only tools
    mcp.tool(
        aha_get,
        annotations={"readOnlyHint": True, "destructiveHint": False},
    )
    mcp.tool(
        aha_search,
        annotations={"readOnlyHint": True, "destructiveHint": False},
    )
    mcp.tool(
        aha_my_work,
        annotations={"readOnlyHint": True, "destructiveHint": False},
    )
    mcp.tool(
        aha_recent_activity,
        annotations={"readOnlyHint": True, "destructiveHint": False},
    )
    mcp.tool(
        aha_introspect,
        annotations={"readOnlyHint": True, "destructiveHint": False},
    )

    # Mutating tools
    mcp.tool(
        aha_create,
        annotations={"readOnlyHint": False, "destructiveHint": False},
    )
    mcp.tool(
        aha_update,
        annotations={"readOnlyHint": False, "destructiveHint": False},
    )
    mcp.tool(
        aha_promote_idea,
        annotations={"readOnlyHint": False, "destructiveHint": False},
    )
    mcp.tool(
        aha_upload_attachment,
        annotations={"readOnlyHint": False, "destructiveHint": False},
    )

    # Destructive tools
    mcp.tool(
        aha_delete,
        annotations={"readOnlyHint": False, "destructiveHint": True},
    )


# ===================================================================
# 1. aha_get — Fetch any record
# ===================================================================

async def aha_get(
    identifier: str,
    record_type: str = None,
    response_format: str = "detailed",
    content_format: str = "markdown",
    ctx: Context = None,
) -> str:
    """Fetch any Aha! record by reference number, name, or ID.

    Accepts any identifier format:
    - Reference: "PROJ-123" (feature), "PROJ-I-45" (idea), "PROJ-E-1" (epic), "PROJ-N-12" (page)
    - Name: "Q3 Sprint Planning" (searches and returns best match)
    - Numeric ID: "6789012345"

    record_type is optional -- auto-detected from reference format. Use it to
    disambiguate name searches: "feature", "idea", "epic", "initiative",
    "release", "goal", "requirement", "page", "task", "key_result".

    response_format: "detailed" (all fields) or "concise" (name, status, assignee only).
    content_format: "markdown" (converts HTML descriptions to Markdown) or "html" (raw).
    """
    _require_auth()

    try:
        resolved = await resolve_identifier(identifier, record_type, ctx)
    except AhaError as e:
        raise_tool_error(e)

    # If resolver returned multiple matches, return them for disambiguation
    if isinstance(resolved, dict) and "matches" in resolved:
        return _format_output(resolved)

    rtype = resolved.get("_type") or record_type or detect_record_type(identifier)
    record_id = resolved.get("id") or identifier
    fields = _fields_for(rtype, response_format)
    gql_name = GQL_SINGULAR.get(rtype)

    if not gql_name:
        raise tool_error_from_message(
            f"Unknown record type: '{rtype}'.",
            hint=f"Supported types: {', '.join(GQL_SINGULAR.keys())}",
        )

    query = f"""query($id: ID!) {{
        {gql_name}(id: $id) {{ {fields} }}
    }}"""

    try:
        data = await graphql(ctx, query, {"id": record_id})
    except AhaError as e:
        raise_tool_error(e)
    except Exception as e:
        raise ToolError(f"Failed to fetch {rtype} '{identifier}': {e}") from e

    result = data.get(gql_name)
    if not result:
        raise ToolError(
            f"Record '{identifier}' not found.\n"
            f'Hint: Try aha_search(query="...") to find records by name.'
        )

    return _format_output(result, content_format)


# ===================================================================
# 2. aha_search — Unified search
# ===================================================================

async def aha_search(
    query: str = None,
    record_type: str = None,
    project: str = None,
    status: str = None,
    assignee: str = None,
    tags: list = None,
    created_after: str = None,
    created_before: str = None,
    page: int = 1,
    per_page: int = 20,
    response_format: str = "concise",
    ctx: Context = None,
) -> str:
    """Search Aha! records with filters. Returns matching records across all types.

    query: Free-text search across names, descriptions, and bodies.
    record_type: Filter by type -- "feature", "idea", "epic", "initiative",
        "release", "goal", "requirement", "page", "task", "comment", "user",
        "workflow", "tag", "custom_field", "project". Omit to search all types.
    project: Filter by project key or ID (e.g., "PROJ" or project ID).
    status: Filter by workflow status name or ID.
    assignee: Filter by assignee name or email.
    tags: Filter by tag names (list of strings).
    created_after / created_before: ISO date strings for date range filtering.
    page: Page number (default 1).
    per_page: Results per page (default 20, max 100).
    response_format: "concise" (default) or "detailed".

    Examples:
      aha_search(query="onboarding", record_type="feature")
      aha_search(record_type="idea", project="PROJ", status="New")
      aha_search(record_type="project")
    """
    _require_auth()

    per_page = min(per_page, 100)

    # --- Text search via searchDocuments ---
    if query and not record_type:
        return await _text_search(query, page, per_page, ctx)

    if query and record_type:
        # Use searchDocuments filtered to a searchable type
        type_map = {
            "feature": "Feature", "idea": "Idea", "epic": "Epic",
            "initiative": "Initiative", "release": "Release",
            "page": "Page", "goal": "Goal", "requirement": "Requirement",
        }
        searchable = type_map.get(record_type)
        if searchable:
            return await _text_search(query, page, per_page, ctx, searchable)
        # Fall through to list query if type isn't searchable

    # --- Structured list query ---
    rtype = record_type or "feature"
    plural = GQL_PLURAL.get(rtype)
    if not plural:
        raise tool_error_from_message(
            f"Cannot list record type '{rtype}'.",
            hint=f"Supported: {', '.join(GQL_PLURAL.keys())}",
        )

    fields = _fields_for(rtype, response_format)

    # Build filter variables
    filters: Dict[str, Any] = {}
    if project:
        filters["projectId"] = project
    if assignee:
        filters["assignedToUserId"] = assignee
    if status:
        filters["workflowStatusId"] = status
    if tags:
        filters["tagIds"] = tags

    gql_query = f"""query($filters: {plural.title().rstrip('s')}Filters, $page: Int!, $per: Int!) {{
        {plural}(filters: $filters, page: $page, per: $per) {{
            nodes {{ {fields} }}
            currentPage totalCount totalPages
        }}
    }}"""

    # Fallback: many list endpoints use simpler filter types; try without typed filter
    # variable if the typed version fails. Use a generic approach first.
    gql_query_simple = f"""query {{
        {plural}(filters: {{{_inline_filters(filters)}}}, page: {page}, per: {per_page}) {{
            nodes {{ {fields} }}
            currentPage totalCount totalPages
        }}
    }}"""

    try:
        data = await graphql(ctx, gql_query_simple)
    except Exception:
        # If simple inline query fails, try parameterized version
        try:
            data = await graphql(ctx, gql_query, {
                "filters": filters,
                "page": page,
                "per": per_page,
            })
        except AhaError as e2:
            raise_tool_error(e2)
        except Exception as e2:
            raise ToolError(f"Search failed: {e2}") from e2

    result = data.get(plural, {})
    nodes = result.get("nodes", [])
    total = result.get("totalCount", len(nodes))

    output = {
        "results": nodes,
        "page": result.get("currentPage", page),
        "total_count": total,
        "total_pages": result.get("totalPages", 1),
    }

    if total > per_page:
        output["hint"] = (
            f"Showing {len(nodes)} of {total} results. "
            f"Use page={page + 1} for more, or add filters to narrow results."
        )

    return _format_output(output)


def _inline_filters(filters: Dict[str, Any]) -> str:
    """Build inline GraphQL filter string from dict. For simple list queries."""
    parts = []
    for k, v in filters.items():
        if isinstance(v, bool):
            parts.append(f'{k}: {str(v).lower()}')
        elif isinstance(v, str):
            parts.append(f'{k}: "{v}"')
        else:
            parts.append(f'{k}: {v}')
    return ", ".join(parts)


async def _text_search(
    query: str, page: int, per_page: int, ctx: Context,
    searchable_type: str = None,
) -> str:
    """Execute searchDocuments GraphQL query."""
    filters: Dict[str, Any] = {"query": query}
    if searchable_type:
        filters["searchableType"] = [searchable_type]

    gql = """query($filters: SearchDocumentFilters!, $page: Int, $per: Int) {
        searchDocuments(filters: $filters, page: $page, per: $per) {
            nodes { name searchableId searchableType }
            currentPage totalCount totalPages
        }
    }"""

    try:
        data = await graphql(ctx, gql, {"filters": filters, "page": page, "per": per_page})
    except AhaError as e:
        raise_tool_error(e)
    except Exception as e:
        raise ToolError(f"Search failed: {e}") from e

    result = data.get("searchDocuments", {})
    nodes = result.get("nodes", [])
    total = result.get("totalCount", len(nodes))

    output = {
        "results": nodes,
        "page": result.get("currentPage", page),
        "total_count": total,
        "total_pages": result.get("totalPages", 1),
    }
    if total > per_page:
        output["hint"] = (
            f"Showing {len(nodes)} of {total}. "
            f"Use page={page + 1} or add record_type filter."
        )
    return _format_output(output)


# ===================================================================
# 3. aha_create — Create any record
# ===================================================================

async def aha_create(
    record_type: str,
    name: str,
    project: str = None,
    description: str = None,
    assignee: str = None,
    status: str = None,
    tags: list = None,
    parent: str = None,
    release: str = None,
    due_date: str = None,
    extra_fields: dict = None,
    content_format: str = "markdown",
    ctx: Context = None,
) -> str:
    """Create a new Aha! record.

    record_type: Required. One of: "feature", "idea", "epic", "initiative",
        "release", "goal", "requirement", "page", "task", "comment",
        "key_result", "record_link".
    name: Required. The title/name of the record.
    project: Project key or ID. Required for features, ideas, epics, releases.
    description: Body text in Markdown (auto-converted to HTML). Use content_format="html" to send raw HTML.
    assignee: Name or email of assignee.
    parent: Reference or ID of parent record (e.g., epic for a feature, feature for a requirement).
    release: Reference or ID of release to assign to.
    due_date: Due date in ISO format (YYYY-MM-DD).
    extra_fields: Dict of additional type-specific fields.

    Examples:
      aha_create("feature", "Login redesign", project="PROJ", release="PROJ-R-1")
      aha_create("idea", "Dark mode", project="PROJ", description="## Summary\\nUsers want dark mode.")
      aha_create("task", "Update docs", parent="PROJ-123", due_date="2026-04-15")
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    type_name = GQL_MUTATION_TYPE.get(record_type)
    if not type_name:
        return _format_output({
            "error": f"Cannot create record type '{record_type}'.",
            "hint": f"Supported: {', '.join(GQL_MUTATION_TYPE.keys())}",
        })

    if record_type in REQUIRES_PROJECT and not project and not release:
        return _format_output({
            "error": f"Creating a {record_type} requires a 'project' or 'release' parameter.",
            "example": f'aha_create("{record_type}", "My Record", project="PROJ")',
        })

    attrs = _build_attributes(
        name=name, description=description, assignee=assignee,
        status=status, tags=tags, parent=parent, release=release,
        due_date=due_date, project=project, extra_fields=extra_fields,
        content_format=content_format,
    )

    # For types that use release as the parent container (feature, epic)
    if record_type in ("feature", "epic") and release and "release" not in attrs:
        attrs["release"] = {"id": release}

    gql_singular = GQL_SINGULAR.get(record_type, record_type)
    concise = CONCISE_FIELDS.get(record_type, "id name")

    mutation = f"""mutation($attrs: {type_name}Attributes!) {{
        create{type_name}(attributes: $attrs) {{
            {gql_singular} {{ {concise} }}
            errors {{ attributes {{ name fullMessages }} }}
        }}
    }}"""

    try:
        data = await graphql(ctx, mutation, {"attrs": attrs})
    except Exception as e:
        return _format_output({"error": f"Failed to create {record_type}: {e}"})

    result = data.get(f"create{type_name}", {})
    err = _mutation_error(result)
    if err:
        return _format_output({"error": f"Failed to create {record_type}.", "details": err})

    created = result.get(gql_singular, {})
    ref = created.get("referenceNum", created.get("id", ""))
    return _format_output({
        "created": created,
        "message": f"{record_type.title()} '{name}' created as {ref}.",
    })


# ===================================================================
# 4. aha_update — Update any record
# ===================================================================

async def aha_update(
    identifier: str,
    name: str = None,
    description: str = None,
    status: str = None,
    assignee: str = None,
    tags: list = None,
    release: str = None,
    due_date: str = None,
    extra_fields: dict = None,
    content_format: str = "markdown",
    ctx: Context = None,
) -> str:
    """Update an existing Aha! record. Only provided fields are changed.

    identifier: Reference number, name, or ID of the record to update.
        Accepts any format: "PROJ-123", "Q3 Planning", or "6789012345".

    All other parameters are optional -- only include fields you want to change.
    extra_fields: Dict for type-specific fields (score, progress, custom fields, etc.).

    Examples:
      aha_update("PROJ-123", status="6789", assignee="alice@co.com")
      aha_update("PROJ-I-45", name="Updated Idea Title")
      aha_update("PROJ-123", tags=["priority", "q3"])
      aha_update("PROJ-123", extra_fields={"score": 85})
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    try:
        resolved = await resolve_identifier(identifier, ctx=ctx)
    except AhaNotFoundError as e:
        return _format_output({"error": str(e)})
    except AhaError as e:
        return _format_output({"error": str(e)})

    if isinstance(resolved, dict) and "matches" in resolved:
        return _format_output(resolved)

    rtype = resolved.get("_type") or detect_record_type(identifier)
    record_id = resolved.get("id") or identifier
    type_name = GQL_MUTATION_TYPE.get(rtype)

    if not type_name:
        return _format_output({
            "error": f"Cannot update record type '{rtype}'.",
            "hint": f"Supported: {', '.join(GQL_MUTATION_TYPE.keys())}",
        })

    attrs = _build_attributes(
        name=name, description=description, assignee=assignee,
        status=status, tags=tags, release=release, due_date=due_date,
        extra_fields=extra_fields, content_format=content_format,
    )

    if not attrs:
        return _format_output({
            "error": "No fields to update. Provide at least one field to change.",
            "example": 'aha_update("PROJ-123", name="New Name")',
        })

    gql_singular = GQL_SINGULAR.get(rtype, rtype)
    concise = CONCISE_FIELDS.get(rtype, "id name")

    mutation = f"""mutation($id: ID!, $attrs: {type_name}Attributes!) {{
        update{type_name}(id: $id, attributes: $attrs) {{
            {gql_singular} {{ {concise} }}
            errors {{ attributes {{ name fullMessages }} }}
        }}
    }}"""

    try:
        data = await graphql(ctx, mutation, {"id": record_id, "attrs": attrs})
    except Exception as e:
        return _format_output({"error": f"Failed to update {rtype} '{identifier}': {e}"})

    result = data.get(f"update{type_name}", {})
    err = _mutation_error(result)
    if err:
        return _format_output({"error": f"Failed to update {rtype}.", "details": err})

    updated = result.get(gql_singular, {})
    return _format_output({"updated": updated, "message": f"{rtype.title()} '{identifier}' updated."})


# ===================================================================
# 5. aha_delete — Delete any record
# ===================================================================

async def aha_delete(
    identifier: str,
    ctx: Context = None,
) -> str:
    """Delete an Aha! record permanently.

    WARNING: This is irreversible.

    identifier: Reference number, name, or ID. Examples: "PROJ-123", "Old Feature", "6789012345".
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    try:
        resolved = await resolve_identifier(identifier, ctx=ctx)
    except AhaNotFoundError as e:
        return _format_output({"error": str(e)})
    except AhaError as e:
        return _format_output({"error": str(e)})

    if isinstance(resolved, dict) and "matches" in resolved:
        return _format_output(resolved)

    rtype = resolved.get("_type") or detect_record_type(identifier)
    record_id = resolved.get("id") or identifier
    type_name = GQL_MUTATION_TYPE.get(rtype)

    if not type_name:
        # Fall back to REST for types without GraphQL delete
        try:
            endpoint = f"/{GQL_PLURAL.get(rtype, rtype + 's')}/{record_id}"
            await rest_api(ctx, "DELETE", endpoint)
            return _format_output({"deleted": True, "message": f"{rtype.title()} '{identifier}' deleted."})
        except Exception as e:
            return _format_output({"error": f"Failed to delete '{identifier}': {e}"})

    gql_singular = GQL_SINGULAR.get(rtype, rtype)

    mutation = f"""mutation($id: ID!) {{
        delete{type_name}(id: $id) {{
            {gql_singular} {{ id referenceNum }}
            errors {{ attributes {{ name fullMessages }} }}
        }}
    }}"""

    try:
        data = await graphql(ctx, mutation, {"id": record_id})
    except Exception as e:
        # Some types only support REST delete (ideas, etc.)
        try:
            endpoint = f"/{GQL_PLURAL.get(rtype, rtype + 's')}/{record_id}"
            await rest_api(ctx, "DELETE", endpoint)
            return _format_output({"deleted": True, "message": f"{rtype.title()} '{identifier}' deleted."})
        except Exception as e2:
            return _format_output({"error": f"Failed to delete '{identifier}': {e2}"})

    result = data.get(f"delete{type_name}", {})
    err = _mutation_error(result)
    if err:
        return _format_output({"error": f"Failed to delete {rtype}.", "details": err})

    return _format_output({"deleted": True, "message": f"{rtype.title()} '{identifier}' deleted."})


# ===================================================================
# 6. aha_promote_idea — Convert idea to feature
# ===================================================================

async def aha_promote_idea(
    idea: str,
    target_project: str = None,
    target_release: str = None,
    ctx: Context = None,
) -> str:
    """Promote an Aha! idea to a feature. This is a workflow action, not a simple update.

    idea: Reference number, name, or ID of the idea to promote.
        Examples: "PROJ-I-45", "Dark mode request", "6789012345"
    target_project: Project to create the feature in (defaults to idea's project).
    target_release: Release to assign the new feature to.

    Returns the newly created feature with its reference number.
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    try:
        resolved = await resolve_identifier(idea, "idea", ctx)
    except AhaNotFoundError as e:
        return _format_output({"error": str(e)})
    except AhaError as e:
        return _format_output({"error": str(e)})

    if isinstance(resolved, dict) and "matches" in resolved:
        return _format_output(resolved)

    idea_id = resolved.get("id") or idea

    # Use REST API for idea promotion
    endpoint = f"/ideas/{idea_id}/promote"
    payload: Dict[str, Any] = {"promotable_type": "feature"}
    if target_release:
        payload["release_id"] = target_release

    try:
        result = await rest_api(ctx, "PUT", endpoint, payload)
        return _format_output({
            "promoted": result,
            "message": f"Idea '{idea}' promoted to feature.",
        })
    except Exception as e:
        return _format_output({"error": f"Failed to promote idea '{idea}': {e}"})


# ===================================================================
# 7. aha_upload_attachment — Attach file to record
# ===================================================================

async def aha_upload_attachment(
    record: str,
    file_url: str,
    ctx: Context = None,
) -> str:
    """Attach a file to an Aha! record via URL.

    record: Reference number, name, or ID of the record to attach to.
    file_url: Public URL of the file to attach.

    Example: aha_upload_attachment("PROJ-123", "https://example.com/spec.pdf")
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    try:
        resolved = await resolve_identifier(record, ctx=ctx)
    except (AhaNotFoundError, AhaError) as e:
        return _format_output({"error": str(e)})

    if isinstance(resolved, dict) and "matches" in resolved:
        return _format_output(resolved)

    rtype = resolved.get("_type") or detect_record_type(record)
    record_id = resolved.get("id") or record

    # Map record types to REST attachment endpoints
    endpoint_map = {
        "feature": f"/features/{record_id}/attachments",
        "idea": f"/ideas/{record_id}/attachments",
        "epic": f"/epics/{record_id}/attachments",
        "requirement": f"/requirements/{record_id}/attachments",
        "page": f"/notes/{record_id}/attachments",
        "task": f"/tasks/{record_id}/attachments",
        "comment": f"/comments/{record_id}/attachments",
    }

    endpoint = endpoint_map.get(rtype)
    if not endpoint:
        return _format_output({
            "error": f"Attachments not supported for type '{rtype}'.",
            "hint": f"Supported: {', '.join(endpoint_map.keys())}",
        })

    # Extract filename from URL
    file_name = file_url.rsplit("/", 1)[-1].split("?")[0] or "attachment"

    payload = {
        "attachment": {
            "file_url": file_url,
            "content_type": "application/octet-stream",
            "file_name": file_name,
        }
    }

    try:
        result = await rest_api(ctx, "POST", endpoint, payload)
        return _format_output({
            "attached": result,
            "message": f"File attached to {rtype} '{record}'.",
        })
    except Exception as e:
        return _format_output({"error": f"Failed to upload attachment: {e}"})


# ===================================================================
# 8. aha_my_work — Current user's assignments
# ===================================================================

async def aha_my_work(
    assignee: str = None,
    response_format: str = "concise",
    ctx: Context = None,
) -> str:
    """Get all work assigned to a user across features, epics, requirements, and tasks.

    assignee: User email or ID. Defaults to the authenticated user (use "me").
    response_format: "concise" (default) or "detailed".

    Returns a unified view grouped by type, sorted by due date.
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    # Build parallel queries for each work type
    feature_fields = _fields_for("feature", response_format)
    epic_fields = _fields_for("epic", response_format)
    req_fields = _fields_for("requirement", response_format)
    task_fields = _fields_for("task", response_format)

    # Build filter dict for parameterized queries
    assignee_filters: Dict[str, Any] = {}
    if assignee:
        assignee_filters["assignedToUserId"] = assignee

    async def fetch_features():
        q = f"""query($filters: FeatureFilters, $page: Int!, $per: Int!) {{
            features(filters: $filters, page: $page, per: $per) {{
                nodes {{ {feature_fields} }} totalCount
            }}
        }}"""
        try:
            return await graphql(ctx, q, {"filters": assignee_filters, "page": 1, "per": 50})
        except Exception:
            return {}

    async def fetch_epics():
        q = f"""query($filters: EpicFilters, $page: Int!, $per: Int!) {{
            epics(filters: $filters, page: $page, per: $per) {{
                nodes {{ {epic_fields} }} totalCount
            }}
        }}"""
        try:
            return await graphql(ctx, q, {"filters": assignee_filters, "page": 1, "per": 50})
        except Exception:
            return {}

    async def fetch_requirements():
        req_filters = {**assignee_filters, "active": True}
        q = f"""query($filters: RequirementFilters, $page: Int!, $per: Int!) {{
            requirements(filters: $filters, page: $page, per: $per) {{
                nodes {{ {req_fields} }} totalCount
            }}
        }}"""
        try:
            return await graphql(ctx, q, {"filters": req_filters, "page": 1, "per": 50})
        except Exception:
            return {}

    async def fetch_tasks():
        # Tasks use REST API since GraphQL task listing is limited
        try:
            endpoint = "/tasks"
            params = {}
            if assignee:
                params["assigned_to_user"] = assignee
            result = await rest_api(ctx, "GET", endpoint, params=params)
            return result
        except Exception:
            return {}

    features_data, epics_data, reqs_data, tasks_data = await asyncio.gather(
        fetch_features(), fetch_epics(), fetch_requirements(), fetch_tasks(),
    )

    output = {
        "features": features_data.get("features", {}).get("nodes", []),
        "epics": epics_data.get("epics", {}).get("nodes", []),
        "requirements": reqs_data.get("requirements", {}).get("nodes", []),
        "tasks": tasks_data if isinstance(tasks_data, list) else [],
        "summary": {},
    }

    for key in ("features", "epics", "requirements", "tasks"):
        output["summary"][key] = len(output[key])

    output["summary"]["total"] = sum(output["summary"].values())

    return _format_output(output)


# ===================================================================
# 9. aha_recent_activity — Recent changes across workspace
# ===================================================================

async def aha_recent_activity(
    days: int = 7,
    project: str = None,
    record_type: str = None,
    ctx: Context = None,
) -> str:
    """Get recent activity across the workspace.

    days: Number of days to look back (default 7, max 30).
    project: Filter to a specific project key or ID.
    record_type: Filter to "feature", "idea", "epic", etc.

    Returns recently created and updated records, grouped by type.
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    days = min(days, 30)
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")

    types_to_query = (
        [record_type] if record_type
        else ["feature", "idea", "epic"]
    )

    # Build filters dict for parameterized queries
    base_filters: Dict[str, Any] = {"updatedSince": since}
    if project:
        base_filters["projectId"] = project

    async def fetch_type(rtype: str):
        fields = _fields_for(rtype, "concise")
        plural = GQL_PLURAL.get(rtype, rtype + "s")
        # Use the appropriate filter type name for each record type
        filter_type = f"{plural.title().rstrip('s')}Filters"

        q = f"""query($filters: {filter_type}, $page: Int!, $per: Int!) {{
            {plural}(filters: $filters, page: $page, per: $per) {{
                nodes {{ {fields} }}
                totalCount
            }}
        }}"""
        try:
            data = await graphql(ctx, q, {"filters": base_filters, "page": 1, "per": 30})
            items = data.get(plural, {}).get("nodes", [])
            total = data.get(plural, {}).get("totalCount", len(items))
            return rtype, items, total
        except Exception:
            return rtype, [], 0

    results = await asyncio.gather(*(fetch_type(t) for t in types_to_query))

    output: Dict[str, Any] = {"period": f"Last {days} days", "activity": {}}
    for rtype, items, total in results:
        if items or total:
            output["activity"][rtype] = {
                "items": items,
                "total": total,
            }

    if not any(v["items"] for v in output["activity"].values()):
        output["message"] = f"No recent activity in the last {days} days."
        if not project:
            output["hint"] = "Try increasing 'days' or specifying a project."

    return _format_output(output)


# ===================================================================
# 10. aha_introspect — GraphQL schema exploration
# ===================================================================

async def aha_introspect(
    query_type: str = "overview",
    type_name: str = None,
    search_term: str = None,
    ctx: Context = None,
) -> str:
    """Explore the Aha! GraphQL API schema.

    query_type:
      "overview" - List all types (optionally filter with search_term).
      "type" - Explore a specific type (requires type_name, e.g., "Feature", "IdeaAttributes").
      "search" - Find queries/mutations matching search_term.

    Examples:
      aha_introspect()  -- list all types
      aha_introspect("type", type_name="Feature")
      aha_introspect("search", search_term="create")
    """
    auth_error = _require_auth()
    if auth_error:
        return auth_error

    if query_type == "overview":
        return await _introspect_overview(search_term, ctx)
    elif query_type == "type":
        if not type_name:
            return _format_output({
                "error": "type_name required when query_type='type'.",
                "example": 'aha_introspect("type", type_name="Feature")',
            })
        return await _introspect_type(type_name, ctx)
    elif query_type == "search":
        return await _introspect_search(search_term, ctx)
    else:
        return _format_output({
            "error": f"Invalid query_type: '{query_type}'.",
            "hint": "Use 'overview', 'type', or 'search'.",
        })


@cached(ttl_seconds=300)
async def _introspect_overview(search_term: Optional[str], ctx: Context) -> str:
    query = """query { __schema { types { name kind description } } }"""
    data = await graphql(ctx, query)
    types = data.get("__schema", {}).get("types", [])

    filtered = [
        t for t in types
        if not t["name"].startswith("__")
        and (not search_term or search_term.lower() in t["name"].lower())
    ][:50]

    return _format_output({
        "types": filtered,
        "total": len(filtered),
        "note": "Showing up to 50 types. Use search_term to filter.",
    })


@cached(ttl_seconds=300)
async def _introspect_type(type_name: str, ctx: Context) -> str:
    query = """query($name: String!) {
        __type(name: $name) {
            name kind description
            fields(includeDeprecated: false) {
                name description
                type { name kind ofType { name kind } }
            }
            inputFields {
                name description defaultValue
                type { name kind ofType { name kind } }
            }
        }
    }"""

    data = await graphql(ctx, query, {"name": type_name})
    type_info = data.get("__type")

    if not type_info:
        return _format_output({
            "error": f"Type '{type_name}' not found.",
            "hint": "Use aha_introspect('overview') to list available types.",
        })

    # Truncate long field lists
    for key in ("fields", "inputFields"):
        if type_info.get(key) and len(type_info[key]) > 30:
            total = len(type_info[key])
            type_info[key] = type_info[key][:30]
            type_info[f"{key}_note"] = f"Truncated to 30 of {total} fields."

    return _format_output(type_info)


@cached(ttl_seconds=300)
async def _introspect_search(search_term: Optional[str], ctx: Context) -> str:
    query = """query {
        __schema {
            queryType { fields { name description } }
            mutationType { fields { name description } }
        }
    }"""

    data = await graphql(ctx, query)
    schema = data.get("__schema", {})

    queries = [
        f for f in (schema.get("queryType", {}).get("fields") or [])
        if not search_term or search_term.lower() in f["name"].lower()
    ][:20]

    mutations = [
        f for f in (schema.get("mutationType", {}).get("fields") or [])
        if not search_term or search_term.lower() in f["name"].lower()
    ][:20]

    return _format_output({
        "queries": queries,
        "mutations": mutations,
        "hint": "Use aha_introspect('type', type_name='...') to explore a specific type.",
    })
