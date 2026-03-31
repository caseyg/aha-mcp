# Aha! MCP Server — Simplified Tool Design

**Date:** 2026-03-30
**Based on:** [Anthropic Engineering: Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

---

## The Problem

The current server has **78 tools**. Per Anthropic's guidance: *"More tools don't always lead to better outcomes."* The anti-pattern is wrapping every API endpoint into a tool. The recommendation is **3-5 thoughtful tools** targeting high-impact workflows.

78 tools means the agent must scan a massive tool list on every turn, increasing confusion, token waste, and the chance of picking the wrong tool. Many tools are near-duplicates across object types (list_features, list_ideas, list_epics, list_initiatives, list_releases, list_goals, list_requirements — all do the same thing with different nouns).

## The Redesign: 78 → 10 tools

### Core Principle: One Router, Not Many Endpoints

Aha! has a unified object model. Features, ideas, epics, initiatives, releases, goals, requirements, pages, comments, tasks — they're all "records" with a reference number or ID. The agent doesn't need `get_feature`, `get_idea`, `get_epic` as separate tools. It needs **one tool that fetches any record**.

### Flexible Input Resolution

Per the blog post: *"Merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful language significantly improves Claude's precision."*

Every tool that accepts an identifier should accept **any of**:
- **Reference number**: `PROJ-123`, `PROJ-I-45`, `PROJ-E-1`, `PROJ-N-12`
- **Name/title**: `"Q3 Sprint Planning"` (resolved via search)
- **Numeric ID**: `6789012345`

The server resolves the input internally. The agent never needs to know which format to use.

```python
async def resolve_record(identifier: str, record_type: str = None) -> dict:
    """Resolve a name, reference number, or ID to an Aha! record."""
    # Try reference number pattern first
    if re.match(r'^[A-Z0-9]+-', identifier):
        return await fetch_by_reference(identifier)
    # Try numeric ID
    if identifier.isdigit():
        return await fetch_by_id(identifier, record_type)
    # Fall back to search by name
    results = await search(identifier, record_type)
    if len(results) == 1:
        return results[0]
    return {"matches": results, "message": f"Multiple matches for '{identifier}'. Please specify."}
```

---

## The 10 Tools

### 1. `aha_get` — Fetch any record

Replaces: `get_record`, `get_feature_details`, `get_idea`, `get_page`, `get_task`, `get_key_result`, `get_record_link`, `get_product`, `get_release_phase`, `get_idea_vote`, `get_strategic_model`, `get_strategic_vision`, `get_strategic_position` (13 tools → 1)

```python
async def aha_get(
    identifier: str,
    record_type: str = None,
    response_format: str = "detailed"
) -> str:
    """Fetch any Aha! record by reference number, name, or ID.

    Accepts any identifier format:
    - Reference: "PROJ-123" (feature), "PROJ-I-45" (idea), "PROJ-E-1" (epic), "PROJ-N-12" (page)
    - Name: "Q3 Sprint Planning" (searches and returns best match)
    - Numeric ID: "6789012345"

    record_type is optional — auto-detected from reference format. Use it to
    disambiguate name searches: "feature", "idea", "epic", "initiative",
    "release", "goal", "requirement", "page", "task", "key_result".

    response_format: "detailed" (all fields) or "concise" (name, status, assignee only).
    """
```

### 2. `aha_search` — Search across all record types

Replaces: `search_documents`, `list_features`, `list_ideas`, `list_epics`, `list_initiatives`, `list_releases`, `list_goals`, `list_requirements`, `list_pages`, `list_tasks`, `list_tasks_for_record`, `list_key_results`, `list_record_links`, `list_record_links_for_type`, `list_products`, `list_release_phases`, `list_idea_votes`, `list_comments`, `list_users`, `list_idea_portals`, `list_idea_portal_users`, `list_idea_subscriptions`, `list_idea_categories`, `list_strategic_models`, `list_strategic_visions`, `list_strategic_positions`, `list_integrations`, `list_workflows`, `list_custom_fields`, `get_all_tags` (30 tools → 1)

```python
async def aha_search(
    query: str = None,
    record_type: str = None,
    project: str = None,
    status: str = None,
    assignee: str = None,
    tags: list[str] = None,
    created_after: str = None,
    created_before: str = None,
    page: int = 1,
    per_page: int = 20,
    response_format: str = "concise"
) -> str:
    """Search Aha! records with filters. Returns matching records across all types.

    query: Free-text search across names, descriptions, and bodies.
    record_type: Filter by type — "feature", "idea", "epic", "initiative",
        "release", "goal", "requirement", "page", "task", "comment", "user",
        "workflow", "tag", "custom_field". Omit to search all types.
    project: Filter by project/product name or key (e.g., "PROJ" or "My Product").
    status: Filter by workflow status name (e.g., "In progress", "Shipped").
    assignee: Filter by assignee name or email.
    tags: Filter by tag names.
    response_format: "concise" (default, name + status + ref) or "detailed" (all fields).

    Returns paginated results. Default 20 per page, max 100.
    If no filters provided, returns recent items across the workspace.
    """
```

### 3. `aha_create` — Create any record

Replaces: `create_feature`, `create_idea`, `create_epic`, `create_initiative`, `create_release`, `create_goal`, `create_requirement`, `create_comment`, `create_user`, `create_task`, `create_key_result`, `create_record_link`, `create_release_phase`, `create_idea_vote`, `create_proxy_vote`, `create_page`, `create_idea_portal_user`, `create_idea_subscription`, `create_integration_field` (19 tools → 1)

```python
async def aha_create(
    record_type: str,
    name: str,
    project: str = None,
    description: str = None,
    assignee: str = None,
    status: str = None,
    tags: list[str] = None,
    parent: str = None,
    release: str = None,
    due_date: str = None,
    extra_fields: dict = None
) -> str:
    """Create a new Aha! record.

    record_type: Required. One of: "feature", "idea", "epic", "initiative",
        "release", "goal", "requirement", "page", "task", "comment",
        "key_result", "record_link".
    name: Required. The title/name of the record.
    project: Project name or key. Required for features, ideas, epics, releases.
    description: Body text (supports HTML).
    assignee: Name or email of the person to assign.
    parent: Reference or name of parent record (e.g., epic for a feature).
    release: Reference or name of release to assign to.
    extra_fields: Dict of additional type-specific fields (custom fields, scores, etc.).

    Returns the created record with its reference number.
    """
```

### 4. `aha_update` — Update any record

Replaces: `update_feature`, `update_idea`, `update_epic`, `update_initiative`, `update_release`, `update_goal`, `update_requirement`, `update_comment`, `update_task`, `update_key_result`, `update_release_phase`, `update_idea_vote`, `update_page`, `update_idea_portal_user`, `update_integration_field`, `update_feature_tags`, `update_idea_tags`, `update_idea_score`, `update_key_result_progress`, `complete_task` (20 tools → 1)

```python
async def aha_update(
    identifier: str,
    name: str = None,
    description: str = None,
    status: str = None,
    assignee: str = None,
    tags: list[str] = None,
    release: str = None,
    due_date: str = None,
    extra_fields: dict = None
) -> str:
    """Update an existing Aha! record. Only provided fields are changed.

    identifier: Reference number, name, or ID of the record to update.
        Accepts any format: "PROJ-123", "Q3 Planning", or "6789012345".

    All other parameters are optional — only include fields you want to change.
    extra_fields: Dict for type-specific fields (score, progress, custom fields, etc.).
        Examples: {"score": 85}, {"progress": 0.75}, {"custom_field_name": "value"}

    To mark a task complete: aha_update("PROJ-123-1", status="Done")
    To update tags: aha_update("PROJ-123", tags=["priority", "q3"])
    To update a score: aha_update("PROJ-I-45", extra_fields={"score": 90})
    """
```

### 5. `aha_delete` — Delete any record

Replaces: `delete_feature`, `delete_idea`, `delete_epic`, `delete_initiative`, `delete_release`, `delete_goal`, `delete_requirement`, `delete_comment`, `delete_task`, `delete_key_result`, `delete_record_link`, `delete_release_phase`, `delete_idea_vote`, `delete_page`, `delete_idea_subscription`, `delete_attachment`, `delete_integration_field` (17 tools → 1)

```python
async def aha_delete(
    identifier: str
) -> str:
    """Delete an Aha! record. Accepts reference number, name, or ID.

    WARNING: This permanently deletes the record. Use with caution.

    identifier: "PROJ-123", "Old Feature Name", or "6789012345"
    """
```

### 6. `aha_promote_idea` — Convert idea to feature

Kept as separate tool because it's a high-value workflow, not a simple CRUD operation.

```python
async def aha_promote_idea(
    idea: str,
    target_project: str = None,
    target_release: str = None
) -> str:
    """Promote an Aha! idea to a feature. This is a workflow action, not a simple update.

    idea: Reference number, name, or ID of the idea to promote.
    target_project: Project to create the feature in (defaults to idea's project).
    target_release: Release to assign the new feature to.

    Returns the newly created feature with its reference number.
    """
```

### 7. `aha_upload_attachment` — Attach a file

Kept separate because it requires multipart upload, not JSON.

```python
async def aha_upload_attachment(
    record: str,
    file_url: str
) -> str:
    """Attach a file to an Aha! record.

    record: Reference number, name, or ID of the record to attach to.
    file_url: URL of the file to attach.
    """
```

### 8. `aha_my_work` — Get current user's assignments

A high-value composite tool per the blog post's `get_customer_context` pattern.

```python
async def aha_my_work(
    assignee: str = None,
    response_format: str = "concise"
) -> str:
    """Get all work assigned to a user across features, epics, requirements, and tasks.

    assignee: Name or email. Defaults to the authenticated user.
    response_format: "concise" (default) or "detailed".

    Returns a unified view of all assigned work, grouped by type,
    sorted by due date. Includes status and release context.
    """
```

### 9. `aha_recent_activity` — Recent changes across workspace

Another composite tool for a common workflow.

```python
async def aha_recent_activity(
    days: int = 7,
    project: str = None,
    record_type: str = None
) -> str:
    """Get recent activity across the workspace.

    days: Number of days to look back (default 7, max 30).
    project: Filter to a specific project.
    record_type: Filter to a specific type.

    Returns recently created and updated records, grouped by day.
    """
```

### 10. `aha_introspect` — Explore the API schema

Kept for power users and debugging.

```python
async def aha_introspect(
    query_type: str = "overview",
    type_name: str = None,
    search_term: str = None
) -> str:
    """Explore the Aha! GraphQL API schema.

    query_type: "overview" (list all types), "type" (explore a specific type),
        "search" (find queries/mutations matching a term).
    type_name: Name of the type to explore (when query_type="type").
    search_term: Term to search for in queries/mutations (when query_type="search").
    """
```

---

## Summary: 78 → 10

| New Tool | Replaces | Count |
|----------|----------|-------|
| `aha_get` | 13 get/detail tools | 13 → 1 |
| `aha_search` | 30 list/search tools | 30 → 1 |
| `aha_create` | 19 create tools | 19 → 1 |
| `aha_update` | 20 update tools | 20 → 1 |
| `aha_delete` | 17 delete tools | 17 → 1 |
| `aha_promote_idea` | 1 workflow tool | 1 → 1 |
| `aha_upload_attachment` | 2 attachment tools | 2 → 1 |
| `aha_my_work` | composite (new) | — |
| `aha_recent_activity` | composite (new) | — |
| `aha_introspect` | 1 debug tool | 1 → 1 |
| **Total** | **78 tools** | **→ 10 tools** |

## Key Design Decisions

### 1. Namespace prefix: `aha_`
Per the blog: use consistent prefixes. Every tool starts with `aha_` so agents can distinguish Aha! tools from other MCP servers.

### 2. Flexible identifier resolution
Every tool that takes a record accepts name, reference number, or numeric ID interchangeably. The server resolves internally. This eliminates the need for the agent to know Aha!'s reference format.

### 3. `response_format` parameter
Per the blog: enable agents to control verbosity. `"concise"` returns ~70% fewer tokens for list operations. `"detailed"` includes all fields for when the agent needs full context.

### 4. Composite tools for common workflows
`aha_my_work` and `aha_recent_activity` are the Aha! equivalents of the blog's `get_customer_context` example — they compile multiple API calls into a single meaningful response.

### 5. Tool annotations
```python
# Read-only tools
aha_get:             readOnlyHint=True,  destructiveHint=False
aha_search:          readOnlyHint=True,  destructiveHint=False
aha_my_work:         readOnlyHint=True,  destructiveHint=False
aha_recent_activity: readOnlyHint=True,  destructiveHint=False
aha_introspect:      readOnlyHint=True,  destructiveHint=False

# Mutating tools
aha_create:          readOnlyHint=False, destructiveHint=False
aha_update:          readOnlyHint=False, destructiveHint=False
aha_promote_idea:    readOnlyHint=False, destructiveHint=False
aha_upload:          readOnlyHint=False, destructiveHint=False

# Destructive tools
aha_delete:          readOnlyHint=False, destructiveHint=True
```

### 6. Helpful error responses
Per the blog post pattern:
```
Error: Could not find record "PROJ-999".
Did you mean one of these? PROJ-99 (Q3 Planning), PROJ-9 (User Research).
Example: aha_get("PROJ-123") or aha_get("Q3 Planning")
```

Not:
```
{"error": "Record not found"}
```

### 7. Truncation with guidance
```
Results truncated (showing 20 of 347 features).
Use filters to narrow: aha_search(record_type="feature", status="In progress", project="PROJ")
```
