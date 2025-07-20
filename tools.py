"""MCP tools for interacting with Aha! API."""

import re
import json
from typing import Optional, List
from fastmcp import FastMCP, Context
from client import graphql, check_auth, rest_api
from utils import (
    require_auth, execute_graphql_query, execute_mutation, execute_rest_api,
    build_filters, build_attributes, validate_reference, build_list_query,
    CrudTemplates, build_standard_fields
)

# This will be set by the main module
mcp: Optional[FastMCP] = None


def register_tools(mcp_instance: FastMCP):
    """Register all tools with the MCP instance"""
    global mcp
    mcp = mcp_instance
    
    # Core record tools
    mcp.tool(get_record, tags={"records", "search"})
    mcp.tool(search_documents, tags={"search", "documents"})
    mcp.tool(get_page, tags={"pages", "documents"})
    mcp.tool(list_projects, tags={"projects", "workspace"})
    mcp.tool(introspection, tags={"api", "debug"})
    
    # Feature management tools
    mcp.tool(list_features, tags={"features", "list"})
    mcp.tool(create_feature, tags={"features", "create"})
    mcp.tool(update_feature, tags={"features", "update"})
    mcp.tool(delete_feature, tags={"features", "delete"})
    mcp.tool(get_feature_details, tags={"features", "details"})
    mcp.tool(update_feature_tags, tags={"features", "tags"})
    mcp.tool(convert_feature_to_epic, tags={"features", "epics", "convert"})
    
    # Idea management tools
    mcp.tool(create_idea, tags={"ideas", "create"})
    mcp.tool(get_idea, tags={"ideas", "details"})
    mcp.tool(list_ideas, tags={"ideas", "list"})
    mcp.tool(update_idea, tags={"ideas", "update"})
    mcp.tool(delete_idea, tags={"ideas", "delete"})
    mcp.tool(promote_idea, tags={"ideas", "features", "promote"})
    mcp.tool(update_idea_score, tags={"ideas", "scoring"})
    mcp.tool(update_idea_tags, tags={"ideas", "tags"})
    
    # Epic management tools
    mcp.tool(list_epics, tags={"epics", "list"})
    mcp.tool(create_epic, tags={"epics", "create"})
    mcp.tool(update_epic, tags={"epics", "update"})
    mcp.tool(delete_epic, tags={"epics", "delete"})
    
    # Initiative management tools
    mcp.tool(list_initiatives, tags={"initiatives", "list"})
    mcp.tool(create_initiative, tags={"initiatives", "create"})
    mcp.tool(update_initiative, tags={"initiatives", "update"})
    mcp.tool(delete_initiative, tags={"initiatives", "delete"})
    
    # Release management tools
    mcp.tool(list_releases, tags={"releases", "list"})
    mcp.tool(create_release, tags={"releases", "create"})
    mcp.tool(update_release, tags={"releases", "update"})
    mcp.tool(delete_release, tags={"releases", "delete"})
    mcp.tool(duplicate_release, tags={"releases", "duplicate"})
    
    # Goal management tools
    mcp.tool(list_goals, tags={"goals", "list"})
    mcp.tool(create_goal, tags={"goals", "create"})
    mcp.tool(update_goal, tags={"goals", "update"})
    mcp.tool(delete_goal, tags={"goals", "delete"})
    
    # Requirement management tools
    mcp.tool(list_requirements, tags={"requirements", "list"})
    mcp.tool(create_requirement, tags={"requirements", "create"})
    mcp.tool(update_requirement, tags={"requirements", "update"})
    mcp.tool(delete_requirement, tags={"requirements", "delete"})
    
    # Comment management tools
    mcp.tool(create_comment, tags={"comments", "create"})
    mcp.tool(update_comment, tags={"comments", "update"})
    mcp.tool(delete_comment, tags={"comments", "delete"})
    mcp.tool(list_comments, tags={"comments", "list"})
    
    # User management tools
    mcp.tool(list_users, tags={"users", "list"})
    mcp.tool(create_user, tags={"users", "create"})
    
    # Attachment management tools
    mcp.tool(upload_attachment, tags={"attachments", "files"})
    mcp.tool(delete_attachment, tags={"attachments", "files"})
    
    # Tag and metadata tools
    mcp.tool(get_all_tags, tags={"tags", "metadata"})
    mcp.tool(list_workflows, tags={"workflows", "metadata"})
    mcp.tool(list_custom_fields, tags={"custom-fields", "metadata"})
    
    # Task/To-dos management tools
    mcp.tool(create_task, tags={"tasks", "create"})
    mcp.tool(list_tasks, tags={"tasks", "list"})
    mcp.tool(get_task, tags={"tasks", "details"})
    mcp.tool(update_task, tags={"tasks", "update"})
    mcp.tool(delete_task, tags={"tasks", "delete"})
    mcp.tool(complete_task, tags={"tasks", "complete"})
    mcp.tool(list_tasks_for_record, tags={"tasks", "list", "records"})
    
    # Key Results management tools
    mcp.tool(list_key_results, tags={"key-results", "list"})
    mcp.tool(create_key_result, tags={"key-results", "create"})
    mcp.tool(get_key_result, tags={"key-results", "details"})
    mcp.tool(update_key_result, tags={"key-results", "update"})
    mcp.tool(delete_key_result, tags={"key-results", "delete"})
    mcp.tool(update_key_result_progress, tags={"key-results", "progress"})
    
    # Record Links/Dependencies management tools
    mcp.tool(list_record_links, tags={"record-links", "dependencies", "list"})
    mcp.tool(create_record_link, tags={"record-links", "dependencies", "create"})
    mcp.tool(get_record_link, tags={"record-links", "dependencies", "details"})
    mcp.tool(delete_record_link, tags={"record-links", "dependencies", "delete"})
    mcp.tool(list_record_links_for_type, tags={"record-links", "dependencies", "list"})
    
    # Products/Workspaces management tools
    mcp.tool(list_products, tags={"products", "workspaces", "list"})
    mcp.tool(get_product, tags={"products", "workspaces", "details"})
    
    # Release Phases management tools
    mcp.tool(list_release_phases, tags={"release-phases", "releases", "list"})
    mcp.tool(create_release_phase, tags={"release-phases", "releases", "create"})
    mcp.tool(get_release_phase, tags={"release-phases", "releases", "details"})
    mcp.tool(update_release_phase, tags={"release-phases", "releases", "update"})
    mcp.tool(delete_release_phase, tags={"release-phases", "releases", "delete"})
    
    # Idea Votes management tools
    mcp.tool(create_idea_vote, tags={"idea-votes", "ideas", "create"})
    mcp.tool(list_idea_votes, tags={"idea-votes", "ideas", "list"})
    mcp.tool(get_idea_vote, tags={"idea-votes", "ideas", "details"})
    mcp.tool(update_idea_vote, tags={"idea-votes", "ideas", "update"})
    mcp.tool(delete_idea_vote, tags={"idea-votes", "ideas", "delete"})
    mcp.tool(create_proxy_vote, tags={"idea-votes", "ideas", "proxy"})
    
    # Pages/Notes management tools
    mcp.tool(list_pages, tags={"pages", "notes", "documentation", "list"})
    mcp.tool(create_page, tags={"pages", "notes", "documentation", "create"})
    mcp.tool(update_page, tags={"pages", "notes", "documentation", "update"})
    mcp.tool(delete_page, tags={"pages", "notes", "documentation", "delete"})
    
    # Idea Portal Management tools
    mcp.tool(list_idea_portals, tags={"ideas", "idea-portals", "portals", "list"})
    mcp.tool(list_idea_portal_users, tags={"ideas", "idea-portals", "portal-users", "list"})
    mcp.tool(create_idea_portal_user, tags={"ideas", "idea-portals", "portal-users", "create"})
    mcp.tool(update_idea_portal_user, tags={"ideas", "idea-portals", "portal-users", "update"})
    mcp.tool(list_idea_subscriptions, tags={"ideas", "idea-subscriptions", "list"})
    mcp.tool(create_idea_subscription, tags={"ideas", "idea-subscriptions", "create"})
    mcp.tool(delete_idea_subscription, tags={"ideas", "idea-subscriptions", "delete"})
    mcp.tool(list_idea_categories, tags={"ideas", "idea-categories", "list"})
    
    # Strategic Elements management tools
    mcp.tool(list_strategic_models, tags={"strategy", "strategic-models", "list"})
    mcp.tool(get_strategic_model, tags={"strategy", "strategic-models", "details"})
    mcp.tool(list_strategic_visions, tags={"strategy", "strategic-visions", "list"})
    mcp.tool(get_strategic_vision, tags={"strategy", "strategic-visions", "details"})
    mcp.tool(list_strategic_positions, tags={"strategy", "strategic-positions", "list"})
    mcp.tool(get_strategic_position, tags={"strategy", "strategic-positions", "details"})
    
    # Integration Management tools
    mcp.tool(list_integrations, tags={"integrations", "external-systems", "list"})
    mcp.tool(create_integration_field, tags={"integrations", "integration-fields", "create"})
    mcp.tool(update_integration_field, tags={"integrations", "integration-fields", "update"})
    mcp.tool(delete_integration_field, tags={"integrations", "integration-fields", "delete"})


async def get_record(reference: str, ctx: Context = None) -> str:
    """Get an Aha! record by reference (e.g., PROJ-123, ADT-123-1, ABC-I-123)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate reference format
    if not re.match(r'^[A-Z0-9]+-\d+(-\d+)?$', reference) and not re.match(r'^[A-Z0-9]+-I-\d+$', reference):
        return json.dumps({"error": f"Invalid reference format: {reference}"})
    
    # Determine record type based on reference
    if re.match(r'^[A-Z0-9]+-I-\d+$', reference):
        # This is an idea reference - use ID
        query = """query($id: ID!) {
            idea(id: $id) {
                id referenceNum name description { htmlBody }
                workflowStatus { id name }
                assignedToUser { id name email }
            }
        }"""
        try:
            data = await graphql(ctx, query, {"id": reference})
            return json.dumps(data.get("idea", {}), indent=2)
        except Exception as e:
            return json.dumps({"error": f"Failed to get idea {reference}: {str(e)}"})
    elif re.match(r'^[A-Z0-9]+-\d+-\d+$', reference):
        # This is a requirement reference
        query = """query($id: ID!) {
            requirement(id: $id) {
                id referenceNum name description { htmlBody }
                feature { id referenceNum name }
            }
        }"""
        try:
            data = await graphql(ctx, query, {"id": reference})
            return json.dumps(data.get("requirement", {}), indent=2)
        except Exception as e:
            return json.dumps({"error": f"Failed to get requirement {reference}: {str(e)}"})
    else:
        # This is a feature reference
        query = """query($id: ID!) {
            feature(id: $id) {
                id referenceNum name description { htmlBody }
                workflowStatus { id name }
                assignedToUser { id name email }
                release { id referenceNum name }
            }
        }"""
        try:
            data = await graphql(ctx, query, {"id": reference})
            return json.dumps(data.get("feature", {}), indent=2)
        except Exception as e:
            return json.dumps({"error": f"Failed to get feature {reference}: {str(e)}"})


async def search_documents(query: str, searchable_type: str = "Page", ctx: Context = None) -> str:
    """Search Aha! documents"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Build filters for searchDocuments query
    filters = {
        "query": query,
        "searchableType": [searchable_type]
    }
    
    gql_query = """query($filters: SearchDocumentFilters!, $page: Int, $per: Int) {
        searchDocuments(filters: $filters, page: $page, per: $per) {
            nodes { 
                name
                searchableId
                searchableType
            }
            currentPage totalCount totalPages
        }
    }"""
    
    try:
        data = await graphql(ctx, gql_query, {"filters": filters, "page": 1, "per": 20})
        return json.dumps(data.get("searchDocuments", {}), indent=2)
    except Exception as e:
        return json.dumps({"error": f"Search failed: {str(e)}"})


async def list_features(
    project_id: Optional[str] = None,
    release_id: Optional[str] = None,
    epic_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List features with filters"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # At least one filter is required
    if not any([project_id, release_id, epic_id]):
        return json.dumps({"error": "At least one filter required: project_id, release_id, or epic_id"})
    
    filters = []
    if project_id:
        filters.append(f'projectId: "{project_id}"')
    if release_id:
        filters.append(f'releaseId: "{release_id}"')
    if epic_id:
        filters.append(f'epicId: "{epic_id}"')
    
    filter_str = ", ".join(filters)
    
    query = f"""query {{
        features(filters: {{{filter_str}}}, page: {page}, per: {per_page}) {{
            nodes {{
                id referenceNum name
                description {{ htmlBody }}
                workflowStatus {{ id name }}
                assignedToUser {{ id name }}
                release {{ id referenceNum name }}
                epic {{ id referenceNum name }}
            }}
            currentPage totalCount totalPages
        }}
    }}"""
    
    data = await graphql(ctx, query)
    return json.dumps(data.get("features", {}), indent=2)


async def create_feature(
    release_id: str,
    name: str,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
    ctx: Context = None
) -> str:
    """Create a new feature"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {
        "name": name,
        "release": {"id": release_id}
    }
    if description:
        attributes["description"] = description
    if assigned_to_user_id:
        attributes["assignedToUser"] = {"id": assigned_to_user_id}
    if tags:
        attributes["tagList"] = ", ".join(tags)
    
    query = """mutation($attrs: FeatureAttributes!) {
        createFeature(attributes: $attrs) {
            feature { id referenceNum name }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"attrs": attributes})
    result = data.get("createFeature", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to create feature", "details": result["errors"]})
    
    return json.dumps(result.get("feature", {}), indent=2)


async def update_feature(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    assigned_to_user_email: Optional[str] = None,
    tags: Optional[List[str]] = None,
    ctx: Context = None
) -> str:
    """Update an existing feature
    
    Args:
        id: Feature ID
        name: New feature name
        description: New feature description
        workflow_status_id: New workflow status ID
        assigned_to_user_id: User ID to assign the feature to
        assigned_to_user_email: User email to assign the feature to (alternative to ID)
        tags: List of tags to apply
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {}
    if name: attributes["name"] = name
    if description: attributes["description"] = description
    if workflow_status_id: attributes["workflowStatus"] = {"id": workflow_status_id}
    if assigned_to_user_id: 
        attributes["assignedToUser"] = {"id": assigned_to_user_id}
    elif assigned_to_user_email:
        attributes["assignedToUser"] = {"email": assigned_to_user_email}
    if tags: attributes["tagList"] = ", ".join(tags)
    
    query = """mutation($id: ID!, $attrs: FeatureAttributes!) {
        updateFeature(id: $id, attributes: $attrs) {
            feature { id referenceNum name }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id, "attrs": attributes})
    result = data.get("updateFeature", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to update feature", "details": result["errors"]})
    
    return json.dumps(result.get("feature", {}), indent=2)


async def update_feature_tags(id: str, tags: str, ctx: Context = None) -> str:
    """Update feature tags using comma-separated string
    
    Args:
        id: Feature ID or reference number
        tags: Comma-separated list of tags (e.g., "tag1, tag2, tag3")
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {"tagList": tags}
    
    query = """mutation($id: ID!, $attrs: FeatureAttributes!) {
        updateFeature(id: $id, attributes: $attrs) {
            feature { id referenceNum name tagList }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id, "attrs": attributes})
    result = data.get("updateFeature", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to update tags", "details": result["errors"]})
    
    return json.dumps(result.get("feature", {}), indent=2)


async def get_all_tags(
    name_filter: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Get all tags in Aha! using GraphQL
    
    Args:
        name_filter: Optional filter to search tags by name
    
    Returns:
        List of tags with their IDs, names, colors, and types
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Build GraphQL query
    gql_query = """query($filters: TagFilters!) {
        tags(filters: $filters) {
            nodes {
                id
                name
                color
                tagType
            }
            totalCount
        }
    }"""
    
    # TagFilters is required but might be empty
    filters = {}
    
    try:
        data = await graphql(ctx, gql_query, {"filters": filters})
        tags = data.get("tags", {})
        
        # Filter client-side if name filter provided
        if name_filter:
            nodes = tags.get("nodes", [])
            filtered_nodes = [
                tag for tag in nodes 
                if name_filter.lower() in tag["name"].lower()
            ]
            tags["nodes"] = filtered_nodes
            tags["totalCount"] = len(filtered_nodes)
        
        return json.dumps(tags, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to get tags: {str(e)}"})



async def delete_feature(id: str, ctx: Context = None) -> str:
    """Delete a feature"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    query = """mutation($id: ID!) {
        deleteFeature(id: $id) {
            feature { id referenceNum }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id})
    result = data.get("deleteFeature", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to delete feature", "details": result["errors"]})
    
    return json.dumps({"success": True, "message": f"Feature {id} deleted", "deleted_feature": result.get("feature")})


async def get_feature_details(id: str, ctx: Context = None) -> str:
    """Get detailed information about a specific feature"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    query = """query($id: ID!) {
        feature(id: $id) {
            id referenceNum name
            description { htmlBody }
            workflowStatus { id name }
            assignedToUser { id name email }
            release { id referenceNum name }
            epic { id referenceNum name }
            team { id name }
            originalEstimate { 
                text
                value
            }
            remainingEstimate { 
                text
                value
            }
            workDone { 
                text
                value
            }
            tags { id name color tagType }
            customFieldValues {
                id
                value
            }
            createdAt updatedAt
            dueDate startDate
            score
            manualRiskComment
            parentRecordLinks {
                id
            }
            childRecordLinks {
                id
            }
            dependenciesCount
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id})
    return json.dumps(data.get("feature") or {"error": f"Feature {id} not found"}, indent=2)


async def get_page(reference: str, include_parent: bool = False, ctx: Context = None) -> str:
    """Get an Aha! page by reference number with optional relationships"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate page reference format
    if not re.match(r'^[A-Z0-9]+-N-\d+$', reference):
        return json.dumps({"error": f"Invalid page reference format: {reference}. Expected format: ABC-N-123"})
    
    query = """query($id: String!, $includeParent: Boolean!) {
        page(referenceNum: $id) {
            id referenceNum name
            description { htmlBody }
            parent @include(if: $includeParent) {
                id referenceNum name
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": reference, "includeParent": include_parent})
    return json.dumps(data.get("page") or {"error": f"Page {reference} not found"}, indent=2)


async def create_idea(
    project_id: str,
    name: str,
    workflow_status_id: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create a new idea"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {
        "name": name,
        "project": {"id": project_id}
    }
    
    if workflow_status_id:
        attributes["workflowStatus"] = {"id": workflow_status_id}
    if assigned_to_user_id:
        attributes["assignedToUser"] = {"id": assigned_to_user_id}
    
    query = """mutation($attrs: IdeaAttributes!) {
        createIdea(attributes: $attrs) {
            idea { id referenceNum name }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"attrs": attributes})
    result = data.get("createIdea", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to create idea", "details": result["errors"]})
    
    return json.dumps(result.get("idea", {}), indent=2)


async def get_idea(id: str, ctx: Context = None) -> str:
    """Get an Aha! idea by ID or reference number"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Check if this is a reference number (e.g., ABC-I-123)
    if re.match(r'^[A-Z0-9]+-I-\d+$', id):
        query = """query($num: String!) {
            idea(referenceNum: $num) {
                id referenceNum name
                description { htmlBody }
                workflowStatus { id name }
                assignedToUser { id name }
                project { id name }
                score visibility promotableId
                createdAt updatedAt
            }
        }"""
        variables = {"num": id}
    else:
        query = """query($id: ID!) {
            idea(id: $id) {
                id referenceNum name
                description { htmlBody }
                workflowStatus { id name }
                assignedToUser { id name }
                project { id name }
                score visibility promotableId
                createdAt updatedAt
            }
        }"""
        variables = {"id": id}
    
    data = await graphql(ctx, query, variables)
    return json.dumps(data.get("idea") or {"error": f"Idea {id} not found"}, indent=2)


async def list_ideas(
    project_id: str,
    assigned_to_user_id: Optional[str] = None,
    promoted: Optional[bool] = None,
    visibility: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List ideas in a project with optional filters"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    filters = [f'projectId: "{project_id}"']
    
    if assigned_to_user_id:
        filters.append(f'assignedToUserId: "{assigned_to_user_id}"')
    if promoted is not None:
        filters.append(f'promoted: {str(promoted).lower()}')
    if visibility:
        filters.append(f'visibility: "{visibility}"')
    
    filter_str = ", ".join(filters)
    
    query = f"""query {{
        ideas(filters: {{{filter_str}}}, page: {page}, per: {per_page}) {{
            nodes {{
                id referenceNum name
                description {{ htmlBody }}
                workflowStatus {{ id name }}
                assignedToUser {{ id name }}
                score visibility promotableId
                createdAt updatedAt
            }}
            currentPage totalCount totalPages
        }}
    }}"""
    
    data = await graphql(ctx, query)
    return json.dumps(data.get("ideas", {}), indent=2)


async def update_idea(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    score: Optional[float] = None,
    tags: Optional[List[str]] = None,
    visibility: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Update an existing idea (Note: only name, assigned_to_user_id, and workflow_status_id are supported)
    
    IMPLEMENTATION NOTES for future REST API support:
    
    1. Score updates use REST API PATCH to /ideas/ideas/{reference_num}:
       - Endpoint: https://{domain}.aha.io/ideas/ideas/{reference_num}
       - Method: PATCH
       - Body: {"ideas_idea": {"score": "28", "score_facts_attributes": [
           {"scoring_system_metric_id": "6001166983756125437", "value": 28},
           {"scoring_system_metric_id": "6001166988050612717", "value": 0}
         ]}}
       
    2. Tags use REST API POST to /taggable/{id}/tags/set:
       - Endpoint: https://{domain}.aha.io/taggable/{numeric_id}/tags/set
       - Method: POST (presumably)
       - Body: [{"label": "test", "value": "7528935782288118517"}]
       - Note: 'value' appears to be the tag ID, 'label' is the display name
       
    3. Description updates might use similar REST endpoints (to be investigated)
    4. Visibility updates might use similar REST endpoints (to be investigated)
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {}
    if name: attributes["name"] = name
    if workflow_status_id: attributes["workflowStatus"] = {"id": workflow_status_id}
    if assigned_to_user_id: attributes["assignedToUser"] = {"id": assigned_to_user_id}
    
    # Note: score, tags, description, and visibility currently not supported via GraphQL
    unsupported = []
    if score is not None: unsupported.append("score")
    if tags: unsupported.append("tags")
    if description: unsupported.append("description")
    if visibility: unsupported.append("visibility")
    
    query = """mutation($id: ID!, $attrs: IdeaAttributes!) {
        updateIdea(id: $id, attributes: $attrs) {
            idea { id referenceNum name }
            errors {
                attributes {
                    name
                    fullMessages
                }
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id, "attrs": attributes})
    result = data.get("updateIdea", {})
    
    if result.get("errors") and result["errors"].get("attributes"):
        return json.dumps({"error": "Failed to update idea", "details": result["errors"]})
    
    response = result.get("idea", {})
    if unsupported:
        response["warning"] = f"The following fields are not supported via GraphQL API: {', '.join(unsupported)}"
    
    return json.dumps(response, indent=2)


async def delete_idea(id: str, ctx: Context = None) -> str:
    """Delete an idea using REST API"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    try:
        # Use REST API to delete the idea
        endpoint = f"/ideas/{id}"
        await rest_api(ctx, "DELETE", endpoint)
        
        return json.dumps({
            "success": True,
            "message": f"Idea {id} deleted successfully"
        })
    except Exception as e:
        return json.dumps({
            "error": f"Failed to delete idea {id}: {str(e)}"
        })


async def list_projects(
    teams_only: Optional[bool] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List projects/workspaces in Aha!
    
    Args:
        teams_only: If True, show only teams; if False, show only non-teams; if None, show all
        page: Page number for pagination (default: 1)
        per_page: Number of projects per page (default: 20, max: 100)
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Build filters
    filters = {}
    if teams_only is not None:
        filters["teams"] = teams_only
    
    query = """query($filters: ProjectFilters, $page: Int!, $per: Int!) {
        projects(filters: $filters, page: $page, per: $per) {
            nodes {
                id
                name
                description { htmlBody }
                color
                childrenCount
                backlogManagementEnabled
                epicsEnabled
                defaultRelease { id referenceNum name }
                defaultUser { id name email }
                goalsCount
                developTeamsCount
                createdAt
                updatedAt
            }
            currentPage
            totalCount
            totalPages
            isLastPage
        }
    }"""
    
    try:
        data = await graphql(ctx, query, {
            "filters": filters,  # Always pass the filters object (empty if no filters)
            "page": page,
            "per": min(per_page, 100)  # Cap at 100 per page
        })
        return json.dumps(data.get("projects", {}), indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to list projects: {str(e)}"}, indent=2)


async def introspection(
    query_type: str = "list-types",
    type_name: Optional[str] = None,
    search_term: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Performs GraphQL introspection to explore the Aha! API schema with size-limited responses"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    if query_type == "list-types":
        # List main types with filtering
        query = """query {
            __schema {
                types {
                    name
                    kind
                    description
                }
            }
        }"""
        
        data = await graphql(ctx, query)
        types = data.get("__schema", {}).get("types", [])
        
        # Filter out introspection types and optionally search
        filtered_types = []
        for t in types:
            if not t["name"].startswith("__"):
                if not search_term or search_term.lower() in t["name"].lower():
                    filtered_types.append(t)
        
        # Limit to first 50 types to avoid response size issues
        filtered_types = filtered_types[:50]
        
        return json.dumps({
            "types": filtered_types,
            "total": len(filtered_types),
            "note": "Showing first 50 types. Use search_term to filter."
        }, indent=2)
    
    elif query_type == "type" and type_name:
        # Get details of a specific type
        query = """query($name: String!) {
            __type(name: $name) {
                name
                kind
                description
                fields(includeDeprecated: false) {
                    name
                    type {
                        name
                        kind
                        ofType { name kind }
                    }
                    description
                }
                inputFields {
                    name
                    type {
                        name
                        kind
                        ofType { name kind }
                    }
                    description
                    defaultValue
                }
            }
        }"""
        
        data = await graphql(ctx, query, {"name": type_name})
        type_info = data.get("__type")
        
        if not type_info:
            return json.dumps({"error": f"Type '{type_name}' not found"})
        
        # Limit fields to first 30 to avoid response size issues
        if type_info.get("fields"):
            type_info["fields"] = type_info["fields"][:30]
            if len(data.get("__type", {}).get("fields", [])) > 30:
                type_info["fields_truncated"] = True
                type_info["fields_note"] = "Showing first 30 fields only"
        
        return json.dumps(type_info, indent=2)
    
    elif query_type == "search":
        # Search for queries and mutations
        query = """query {
            __schema {
                queryType { fields { name description } }
                mutationType { fields { name description } }
            }
        }"""
        
        data = await graphql(ctx, query)
        schema = data.get("__schema", {})
        
        results = {
            "types": [],
            "queryType": {"fields": []},
            "mutationType": {"fields": []}
        }
        
        # Filter queries
        if schema.get("queryType", {}).get("fields"):
            for field in schema["queryType"]["fields"]:
                if not search_term or search_term.lower() in field["name"].lower():
                    results["queryType"]["fields"].append(field)
        
        # Filter mutations
        if schema.get("mutationType", {}).get("fields"):
            for field in schema["mutationType"]["fields"]:
                if not search_term or search_term.lower() in field["name"].lower():
                    results["mutationType"]["fields"].append(field)
        
        # Also search in type names
        types_query = """query {
            __schema { types { name kind description } }
        }"""
        
        types_data = await graphql(ctx, types_query)
        all_types = types_data.get("__schema", {}).get("types", [])
        
        for t in all_types:
            if not t["name"].startswith("__") and search_term and search_term.lower() in t["name"].lower():
                results["types"].append(t)
        
        # Limit results
        results["queryType"]["fields"] = results["queryType"]["fields"][:20]
        results["mutationType"]["fields"] = results["mutationType"]["fields"][:20]
        results["types"] = results["types"][:20]
        
        return json.dumps(results, indent=2)
    
    else:
        return json.dumps({
            "error": "Invalid query_type. Use 'list-types', 'type' (with type_name), or 'search' (with optional search_term)"
        })


# =============================================================================
# NEW TOOLS - Priority Implementation Order
# =============================================================================

async def promote_idea(
    id: str,
    target_type: str,  # "feature" or "epic"
    release_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Convert idea to feature/epic using REST API"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    if target_type not in ["feature", "epic"]:
        return json.dumps({"error": "target_type must be 'feature' or 'epic'"})
    
    # Use the documented REST API endpoint for promoting ideas
    endpoint = f"/ideas/{id}/promote"
    data = {
        "promotable_type": target_type
    }
    
    if release_id:
        data["release_id"] = release_id
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if assigned_to_user_id:
        data["assigned_to_user_id"] = assigned_to_user_id
    
    return await execute_rest_api(ctx, "PUT", endpoint, data, f"promote idea to {target_type}")


async def convert_feature_to_epic(id: str, ctx: Context = None) -> str:
    """Feature conversion (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    endpoint = f"/features/{id}/convert_to_epic"
    return await execute_rest_api(ctx, "POST", endpoint, operation="convert feature to epic")


async def list_epics(
    project_id: Optional[str] = None,
    release_id: Optional[str] = None, 
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List epics (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    filters = {}
    if project_id: filters["projectId"] = project_id
    if release_id: filters["releaseId"] = release_id
    
    if not filters:
        return json.dumps({"error": "At least one filter required: project_id or release_id"})
    
    query, variables = build_list_query("epics", build_standard_fields("epic"), filters, page, per_page)
    return await execute_graphql_query(ctx, query, variables, "epics", "list epics")



async def create_epic(
    release_id: str,
    name: str,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create epics (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {"name": name},
        {"description": description},
        {"release": release_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.create_mutation("epic", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createEpic", "epic", "create epic")



async def update_epic(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Modify epics (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {},
        {"name": name, "description": description},
        {"workflowStatus": workflow_status_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.update_mutation("epic", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"id": id, "attrs": attributes}, "updateEpic", "epic", "update epic")



async def delete_epic(id: str, ctx: Context = None) -> str:
    """Remove epics (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    query = CrudTemplates.delete_mutation("epic")
    return await execute_mutation(ctx, query, {"id": id}, "deleteEpic", "epic", "delete epic")



async def list_initiatives(
    project_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List initiatives (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    filters = {}
    if project_id: filters["projectId"] = project_id
    
    query, variables = build_list_query("initiatives", build_standard_fields("initiative"), filters, page, per_page)
    return await execute_graphql_query(ctx, query, variables, "initiatives", "list initiatives")



async def create_initiative(
    project_id: str,
    name: str,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create initiatives (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {"name": name},
        {"description": description},
        {"project": project_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.create_mutation("initiative", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createInitiative", "initiative", "create initiative")



async def update_initiative(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Modify initiatives (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {},
        {"name": name, "description": description},
        {"workflowStatus": workflow_status_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.update_mutation("initiative", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"id": id, "attrs": attributes}, "updateInitiative", "initiative", "update initiative")



async def delete_initiative(id: str, ctx: Context = None) -> str:
    """Remove initiatives (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/initiatives/{id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete initiative")



async def create_comment(
    record_id: str,
    body: str,
    record_type: str = "feature",  # feature, idea, epic, initiative, etc.
    ctx: Context = None
) -> str:
    """Add comments to features/ideas/etc (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = {"body": body, "commentable": {"id": record_id, "typename": record_type.title()}}
    
    query = """mutation($attrs: CommentAttributes!) {
        createComment(attributes: $attrs) {
            comment { id body createdAt }
            errors { attributes { name fullMessages } }
        }
    }"""
    
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createComment", "comment", "create comment")



async def update_comment(id: str, body: str, ctx: Context = None) -> str:
    """Edit existing comments (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/comments/{id}"
    data = {"comment": {"body": body}}
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update comment")



async def delete_comment(id: str, ctx: Context = None) -> str:
    """Remove comments (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/comments/{id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete comment")



async def list_comments(
    record_id: str,
    record_type: str = "feature",
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """Get comments for a record (GraphQL available - no pagination)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    query = f"""query($id: ID!) {{
        {record_type}(id: $id) {{
            comments {{
                id body createdAt
                user {{ id name email }}
            }}
            commentsCount
        }}
    }}"""
    
    try:
        data = await graphql(ctx, query, {"id": record_id})
        record_data = data.get(record_type, {})
        comments = record_data.get("comments", [])
        comments_count = record_data.get("commentsCount", 0)
        
        # Simulate pagination since GraphQL doesn't support it for comments
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_comments = comments[start_idx:end_idx]
        
        return json.dumps({
            "comments": paginated_comments,
            "currentPage": page,
            "totalCount": comments_count,
            "totalPages": (comments_count + per_page - 1) // per_page,
            "note": "Client-side pagination simulation (GraphQL comments don't support server-side pagination)"
        }, indent=2)
        
    except Exception as e:
        return json.dumps({"error": f"Failed to list comments for {record_type}: {str(e)}"}, indent=2)



async def list_releases(
    project_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List releases in a project (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    filters = {}
    if project_id: filters["projectId"] = project_id
    
    query, variables = build_list_query("releases", build_standard_fields("release"), filters, page, per_page)
    return await execute_graphql_query(ctx, query, variables, "releases", "list releases")



async def create_release(
    project_id: str,
    name: str,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create new releases (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {"name": name},
        {"developmentStartedOn": start_date, "releaseDate": release_date},
        {"project": project_id}
    )
    
    query = CrudTemplates.create_mutation("release", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createRelease", "release", "create release")



async def update_release(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Modify releases (GraphQL available)"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {},
        {"name": name, "developmentStartedOn": start_date, "releaseDate": release_date}
    )
    
    query = CrudTemplates.update_mutation("release", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"id": id, "attrs": attributes}, "updateRelease", "release", "update release")



async def delete_release(id: str, ctx: Context = None) -> str:
    """Remove releases (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/releases/{id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete release")



async def update_idea_score(
    id: str,
    score: float,
    ctx: Context = None
) -> str:
    """Update idea scores via REST API"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # First get the current idea to understand its scorecard structure
    try:
        idea_response = await rest_api(ctx, "GET", f"/ideas/{id}")
        current_score_facts = idea_response.get("idea", {}).get("score_facts", [])
        
        if not current_score_facts:
            return json.dumps({"error": f"Idea {id} has no existing scorecard to update"})
        
        # Update the first score fact with the new total score
        # In a real implementation, you might want to distribute this across metrics
        updated_score_facts = current_score_facts.copy()
        if updated_score_facts:
            updated_score_facts[0]["value"] = int(score)
        
        endpoint = f"/ideas/{id}"
        data = {
            "idea": {
                "score_facts": updated_score_facts
            }
        }
        return await execute_rest_api(ctx, "PUT", endpoint, data, "update idea score")
        
    except Exception as e:
        return json.dumps({"error": f"Failed to get current scorecard for idea {id}: {str(e)}"})



async def update_idea_tags(
    id: str,
    tags: List[str],
    ctx: Context = None
) -> str:
    """Set/update tags on ideas via REST API"""
    
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Use the documented REST API endpoint for updating idea tags
    endpoint = f"/ideas/{id}"
    data = {
        "idea": {
            "tags": ", ".join(tags)
        }
    }
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update idea tags")


# =============================================================================
# GOAL MANAGEMENT TOOLS
# =============================================================================

async def list_goals(
    project_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List goals (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    filters = {}
    if project_id: filters["projectId"] = project_id
    
    query, variables = build_list_query("goals", build_standard_fields("goal"), filters, page, per_page)
    return await execute_graphql_query(ctx, query, variables, "goals", "list goals")


async def create_goal(
    project_id: str,
    name: str,
    metric_name: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create goals (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {"name": name},
        {"successMetric": {"name": metric_name} if metric_name else None},
        {"project": project_id, "workflowStatus": workflow_status_id}
    )
    
    query = CrudTemplates.create_mutation("goal", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createGoal", "goal", "create goal")


async def update_goal(
    id: str,
    name: Optional[str] = None,
    metric_name: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Modify goals (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {},
        {"name": name, "successMetric": {"name": metric_name} if metric_name else None},
        {"workflowStatus": workflow_status_id}
    )
    
    query = CrudTemplates.update_mutation("goal", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"id": id, "attrs": attributes}, "updateGoal", "goal", "update goal")


async def delete_goal(id: str, ctx: Context = None) -> str:
    """Remove goals (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/goals/{id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete goal")


# =============================================================================
# ATTACHMENT MANAGEMENT TOOLS
# =============================================================================

async def upload_attachment(
    resource_type: str,
    resource_id: str,
    file_url: str,
    file_name: str,
    content_type: str = "application/octet-stream",
    ctx: Context = None
) -> str:
    """Upload files to records via URL (REST only)
    
    Args:
        resource_type: Type of resource (comments, notes, tasks, custom_fields, etc.)
        resource_id: ID of the resource to attach to
        file_url: URL of the file to attach
        file_name: Name for the attachment
        content_type: MIME type of the file
    """
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Map resource types to API endpoints
    endpoint_map = {
        "comments": f"/comments/{resource_id}/attachments",
        "notes": f"/notes/{resource_id}/attachments",
        "tasks": f"/tasks/{resource_id}/attachments", 
        "custom_fields": f"/custom_fields/{resource_id}/attachments",
        "custom_field_values": f"/custom_field_values/{resource_id}/attachments"
    }
    
    if resource_type not in endpoint_map:
        return json.dumps({
            "error": f"Unsupported resource type: {resource_type}. Supported: {list(endpoint_map.keys())}"
        })
    
    endpoint = endpoint_map[resource_type]
    data = {
        "attachment": {
            "file_url": file_url,
            "content_type": content_type,
            "file_name": file_name
        }
    }
    
    return await execute_rest_api(ctx, "POST", endpoint, data, "upload attachment")


async def delete_attachment(attachment_id: str, ctx: Context = None) -> str:
    """Remove file attachments (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/attachments/{attachment_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete attachment")


# =============================================================================
# REQUIREMENT MANAGEMENT TOOLS  
# =============================================================================

async def list_requirements(
    project_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List requirements for features (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Requirements require at least one filter
    filters = {"active": True}  # Default to active requirements
    if project_id:
        filters["projectId"] = project_id
    
    query, variables = build_list_query("requirements", build_standard_fields("requirement"), filters, page, per_page)
    return await execute_graphql_query(ctx, query, variables, "requirements", "list requirements")


async def create_requirement(
    name: str,
    feature_id: str,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    original_estimate: Optional[str] = None,
    initial_estimate: Optional[str] = None,
    position: Optional[int] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create requirements (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {"name": name},
        {"description": description, "originalEstimate": original_estimate, 
         "initialEstimate": initial_estimate, "position": position},
        {"feature": feature_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.create_mutation("requirement", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"attrs": attributes}, "createRequirement", "requirement", "create requirement")


async def update_requirement(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    original_estimate: Optional[str] = None,
    remaining_estimate: Optional[str] = None,
    initial_estimate: Optional[str] = None,
    work_done: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    position: Optional[int] = None,
    ctx: Optional[Context] = None
) -> str:
    """Modify requirements (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    attributes = build_attributes(
        {},
        {"name": name, "description": description, "originalEstimate": original_estimate,
         "remainingEstimate": remaining_estimate, "initialEstimate": initial_estimate,
         "workDone": work_done, "position": position},
        {"workflowStatus": workflow_status_id, "assignedToUser": assigned_to_user_id}
    )
    
    query = CrudTemplates.update_mutation("requirement", ["id", "referenceNum", "name"])
    return await execute_mutation(ctx, query, {"id": id, "attrs": attributes}, "updateRequirement", "requirement", "update requirement")


async def delete_requirement(id: str, ctx: Optional[Context] = None) -> str:
    """Remove requirements (GraphQL available)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    query = CrudTemplates.delete_mutation("requirement")
    return await execute_mutation(ctx, query, {"id": id}, "deleteRequirement", "requirement", "delete requirement")


# =============================================================================
# WORKFLOW AND METADATA TOOLS  
# =============================================================================

async def list_workflows(
    project_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get available workflows (REST preferred)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/products/{project_id}/workflows"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list workflows")


async def list_custom_fields(ctx: Optional[Context] = None) -> str:
    """Get custom field definitions (REST preferred)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/custom_field_definitions"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list custom fields")


async def duplicate_release(
    id: str,
    ctx: Optional[Context] = None
) -> str:
    """Copy release structure (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/releases/{id}/duplicate"
    return await execute_rest_api(ctx, "POST", endpoint, operation="duplicate release")


async def list_users(
    project_id: Optional[str] = None,
    email: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Get workspace users (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    if project_id:
        # List users for specific project
        endpoint = f"/products/{project_id}/users"
    else:
        # List all users with optional email filter
        endpoint = "/users"
        if email:
            endpoint += f"?email={email}"
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list users")


async def create_user(
    project_id: str,
    email: str,
    first_name: str,
    last_name: str,
    role: str,
    identity_provider_id: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Add new users (REST only)"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate role
    valid_roles = ["product_owner", "contributor", "reviewer", "viewer", "none"]
    if role not in valid_roles:
        return json.dumps({
            "error": f"Invalid role: {role}. Must be one of: {', '.join(valid_roles)}"
        })
    
    endpoint = f"/products/{project_id}/users"
    data = {
        "user": {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "role": role
        }
    }
    
    if identity_provider_id:
        data["user"]["identity_provider_id"] = identity_provider_id
    
    return await execute_rest_api(ctx, "POST", endpoint, data, "create user")


# Task/To-dos management tools

async def create_task(
    record_type: str,
    record_id: str,
    name: str,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    assigned_to_user_email: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create tasks associated with features/ideas"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate record type
    valid_types = ["features", "epics", "initiatives", "releases", "requirements", "ideas"]
    if record_type not in valid_types:
        return json.dumps({
            "error": f"Invalid record_type: {record_type}. Must be one of: {', '.join(valid_types)}"
        })
    
    endpoint = f"/{record_type}/{record_id}/tasks"
    data = {
        "task": {
            "name": name
        }
    }
    
    if description:
        data["task"]["description"] = description
    if due_date:
        data["task"]["due_date"] = due_date
    if assigned_to_user_email:
        data["task"]["assigned_to_user"] = {"email": assigned_to_user_email}
    
    return await execute_rest_api(ctx, "POST", endpoint, data, "create task")


async def list_tasks(
    assigned_to_user_id: Optional[str] = None,
    completed: Optional[bool] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List tasks by assignee or record"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/tasks"
    params = []
    
    if assigned_to_user_id:
        params.append(f"assigned_to_user_id={assigned_to_user_id}")
    if completed is not None:
        params.append(f"completed={str(completed).lower()}")
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list tasks")


async def get_task(
    task_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get task details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/tasks/{task_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get task")


async def update_task(
    task_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    assigned_to_user_email: Optional[str] = None,
    completed: Optional[bool] = None,
    ctx: Optional[Context] = None
) -> str:
    """Update task properties/status"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"task": {}}
    
    if name:
        data["task"]["name"] = name
    if description:
        data["task"]["description"] = description
    if due_date:
        data["task"]["due_date"] = due_date
    if assigned_to_user_email:
        data["task"]["assigned_to_user"] = {"email": assigned_to_user_email}
    if completed is not None:
        data["task"]["completed"] = completed
    
    if not data["task"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/tasks/{task_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update task")


async def delete_task(
    task_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Delete tasks"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/tasks/{task_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete task")


async def complete_task(
    task_id: str,
    completed: bool = True,
    ctx: Optional[Context] = None
) -> str:
    """Mark tasks complete/incomplete"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "task": {
            "completed": completed
        }
    }
    
    endpoint = f"/tasks/{task_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "complete task")


async def list_tasks_for_record(
    record_type: str,
    record_id: str,
    assigned_to_user_id: Optional[str] = None,
    completed: Optional[bool] = None,
    ctx: Optional[Context] = None
) -> str:
    """Get tasks for specific records"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate record type
    valid_types = ["features", "epics", "initiatives", "releases", "requirements", "ideas"]
    if record_type not in valid_types:
        return json.dumps({
            "error": f"Invalid record_type: {record_type}. Must be one of: {', '.join(valid_types)}"
        })
    
    endpoint = f"/{record_type}/{record_id}/tasks"
    params = []
    
    if assigned_to_user_id:
        params.append(f"assigned_to_user_id={assigned_to_user_id}")
    if completed is not None:
        params.append(f"completed={str(completed).lower()}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list tasks for record")


# Key Results management tools

async def list_key_results(
    goal_id: str,
    ctx: Optional[Context] = None
) -> str:
    """List key results for goals"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/goals/{goal_id}/key_results"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list key results")


async def create_key_result(
    goal_id: str,
    name: str,
    description: Optional[str] = None,
    target_metric: Optional[str] = None,
    starting_metric: Optional[str] = None,
    assigned_to_user_email: Optional[str] = None,
    workflow_status_name: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create key results"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "key_result": {
            "name": name
        }
    }
    
    if description:
        data["key_result"]["description"] = description
    if target_metric:
        data["key_result"]["target_metric"] = target_metric
    if starting_metric:
        data["key_result"]["starting_metric"] = starting_metric
    if assigned_to_user_email:
        data["key_result"]["assigned_to_user"] = {"email": assigned_to_user_email}
    if workflow_status_name:
        data["key_result"]["workflow_status"] = {"name": workflow_status_name}
    
    endpoint = f"/goals/{goal_id}/key_results"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create key result")


async def get_key_result(
    key_result_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get key result details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/key_results/{key_result_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get key result")


async def update_key_result(
    key_result_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    target_metric: Optional[str] = None,
    starting_metric: Optional[str] = None,
    current_metric: Optional[str] = None,
    assigned_to_user_email: Optional[str] = None,
    workflow_status_name: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Update metrics/status"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"key_result": {}}
    
    if name:
        data["key_result"]["name"] = name
    if description:
        data["key_result"]["description"] = description
    if target_metric:
        data["key_result"]["target_metric"] = target_metric
    if starting_metric:
        data["key_result"]["starting_metric"] = starting_metric
    if current_metric:
        data["key_result"]["current_metric"] = current_metric
    if assigned_to_user_email:
        data["key_result"]["assigned_to_user"] = {"email": assigned_to_user_email}
    if workflow_status_name:
        data["key_result"]["workflow_status"] = {"name": workflow_status_name}
    
    if not data["key_result"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/key_results/{key_result_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update key result")


async def delete_key_result(
    key_result_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove key results"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/key_results/{key_result_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete key result")


async def update_key_result_progress(
    key_result_id: str,
    current_metric: str,
    ctx: Optional[Context] = None
) -> str:
    """Update current progress"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "key_result": {
            "current_metric": current_metric
        }
    }
    
    endpoint = f"/key_results/{key_result_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update key result progress")


# Record Links/Dependencies management tools

async def list_record_links(
    record_type: str,
    record_id: str,
    parent_and_child_links: bool = False,
    ctx: Optional[Context] = None
) -> str:
    """List dependencies between records"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate record type
    valid_types = ["features", "releases", "ideas", "epics", "release_phases", "initiatives", "pages", "goals"]
    if record_type not in valid_types:
        return json.dumps({
            "error": f"Invalid record_type: {record_type}. Must be one of: {', '.join(valid_types)}"
        })
    
    endpoint = f"/{record_type}/{record_id}/record_links"
    if parent_and_child_links:
        endpoint += "?parent_and_child_links=true"
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list record links")


async def create_record_link(
    parent_record_type: str,
    parent_record_id: str,
    child_record_type: str,
    child_record_id: str,
    link_type: int,
    ctx: Optional[Context] = None
) -> str:
    """Create dependency relationships"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate record types
    valid_types = ["feature", "release", "idea", "epic", "release_phase", "initiative", "page", "goal"]
    if parent_record_type not in valid_types:
        return json.dumps({
            "error": f"Invalid parent_record_type: {parent_record_type}. Must be one of: {', '.join(valid_types)}"
        })
    if child_record_type not in valid_types:
        return json.dumps({
            "error": f"Invalid child_record_type: {child_record_type}. Must be one of: {', '.join(valid_types)}"
        })
    
    # Validate link type
    valid_link_types = [10, 20, 30, 40, 50, 60, 80]
    link_type_names = {
        10: "Relates to",
        20: "Depends on", 
        30: "Duplicated by",
        40: "Contained by",
        50: "Impacted by",
        60: "Blocked by",
        80: "Research for"
    }
    
    if link_type not in valid_link_types:
        return json.dumps({
            "error": f"Invalid link_type: {link_type}. Must be one of: {valid_link_types} ({', '.join(f'{k} ({v})' for k, v in link_type_names.items())})"
        })
    
    data = {
        "record_link": {
            "record_type": child_record_type,
            "record_id": child_record_id,
            "link_type": link_type
        }
    }
    
    # Use plural form for endpoint
    parent_type_plural = parent_record_type + "s" if not parent_record_type.endswith("s") else parent_record_type
    endpoint = f"/{parent_type_plural}/{parent_record_id}/record_links"
    
    return await execute_rest_api(ctx, "POST", endpoint, data, "create record link")


async def get_record_link(
    record_link_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get link details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/record_links/{record_link_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get record link")


async def delete_record_link(
    record_link_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove dependencies"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/record_links/{record_link_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete record link")


async def list_record_links_for_type(
    record_type: str,
    link_type: Optional[int] = None,
    ctx: Optional[Context] = None
) -> str:
    """Get links by record type"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # This is a conceptual endpoint - may need to be implemented differently
    # based on actual Aha! API capabilities
    endpoint = "/record_links"
    params = [f"record_type={record_type}"]
    
    if link_type:
        params.append(f"link_type={link_type}")
    
    endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list record links for type")


# Products/Workspaces management tools

async def list_products(
    updated_since: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """List products in account"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/products"
    params = []
    
    if updated_since:
        params.append(f"updated_since={updated_since}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list products")


async def get_product(
    product_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get product details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/products/{product_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get product")


# Release Phases management tools

async def list_release_phases(
    release_id: str,
    phase_type: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """List phases for releases"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate phase type
    if phase_type and phase_type not in ["milestone", "phase"]:
        return json.dumps({
            "error": f"Invalid phase_type: {phase_type}. Must be 'milestone' or 'phase'"
        })
    
    endpoint = f"/releases/{release_id}/release_phases"
    if phase_type:
        endpoint += f"?type={phase_type}"
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list release phases")


async def create_release_phase(
    release_id: str,
    name: str,
    phase_type: str = "phase",
    start_on: Optional[str] = None,
    end_on: Optional[str] = None,
    description: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create release milestones/phases"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate phase type
    if phase_type not in ["milestone", "phase"]:
        return json.dumps({
            "error": f"Invalid phase_type: {phase_type}. Must be 'milestone' or 'phase'"
        })
    
    data = {
        "release_phase": {
            "name": name,
            "type": phase_type,
            "release_id": release_id
        }
    }
    
    if start_on:
        data["release_phase"]["start_on"] = start_on
    if end_on:
        data["release_phase"]["end_on"] = end_on
    if description:
        data["release_phase"]["description"] = description
    
    endpoint = "/release_phases"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create release phase")


async def get_release_phase(
    phase_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get phase details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/release_phases/{phase_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get release phase")


async def update_release_phase(
    phase_id: str,
    name: Optional[str] = None,
    start_on: Optional[str] = None,
    end_on: Optional[str] = None,
    description: Optional[str] = None,
    progress: Optional[float] = None,
    ctx: Optional[Context] = None
) -> str:
    """Update phase dates/status"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"release_phase": {}}
    
    if name:
        data["release_phase"]["name"] = name
    if start_on:
        data["release_phase"]["start_on"] = start_on
    if end_on:
        data["release_phase"]["end_on"] = end_on
    if description:
        data["release_phase"]["description"] = description
    if progress is not None:
        data["release_phase"]["progress"] = progress
    
    if not data["release_phase"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/release_phases/{phase_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update release phase")


async def delete_release_phase(
    phase_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove phases"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/release_phases/{phase_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete release phase")


# Idea Votes management tools (using endorsements API)

async def create_idea_vote(
    idea_id: str,
    value: Optional[float] = None,
    user_email: Optional[str] = None,
    description: Optional[str] = None,
    link: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create votes for ideas"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "idea_endorsement": {}
    }
    
    if user_email:
        data["idea_endorsement"]["email"] = user_email
    if value is not None:
        data["idea_endorsement"]["value"] = value
    if description:
        data["idea_endorsement"]["description"] = description
    if link:
        data["idea_endorsement"]["link"] = link
    
    endpoint = f"/ideas/{idea_id}/endorsements"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create idea vote")


async def list_idea_votes(
    idea_id: str,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List votes for ideas"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/ideas/{idea_id}/endorsements"
    params = []
    
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list idea votes")


async def get_idea_vote(
    idea_id: str,
    vote_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get vote details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/ideas/{idea_id}/endorsements/{vote_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get idea vote")


async def update_idea_vote(
    idea_id: str,
    vote_id: str,
    value: Optional[float] = None,
    description: Optional[str] = None,
    link: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Modify vote values"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"idea_endorsement": {}}
    
    if value is not None:
        data["idea_endorsement"]["value"] = value
    if description:
        data["idea_endorsement"]["description"] = description
    if link:
        data["idea_endorsement"]["link"] = link
    
    if not data["idea_endorsement"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/ideas/{idea_id}/endorsements/{vote_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update idea vote")


async def delete_idea_vote(
    idea_id: str,
    vote_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove votes"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/ideas/{idea_id}/endorsements/{vote_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete idea vote")


async def create_proxy_vote(
    idea_id: str,
    value: float,
    voter_emails: List[str],
    description: Optional[str] = None,
    link: Optional[str] = None,
    idea_organization_id: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create proxy votes for portal users"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "idea_endorsement": {
            "idea_id": idea_id,
            "value": value,
            "idea_users": voter_emails
        }
    }
    
    if description:
        data["idea_endorsement"]["description"] = description
    if link:
        data["idea_endorsement"]["link"] = link
    if idea_organization_id:
        data["idea_endorsement"]["idea_organization_id"] = idea_organization_id
    
    endpoint = f"/ideas/{idea_id}/endorsements"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create proxy vote")


# Pages/Notes management tools

async def list_pages(
    product_id: str,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List pages/notes in products"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/products/{product_id}/pages"
    params = []
    
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list pages")


async def create_page(
    product_id: str,
    name: str,
    body: Optional[str] = None,
    page_type: str = "page",
    parent_id: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Create documentation pages"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate page type
    valid_types = ["page", "note", "whiteboard"]
    if page_type not in valid_types:
        return json.dumps({
            "error": f"Invalid page_type: {page_type}. Must be one of: {', '.join(valid_types)}"
        })
    
    data = {
        "page": {
            "name": name,
            "type": page_type
        }
    }
    
    if body:
        data["page"]["body"] = body
    if parent_id:
        data["page"]["parent_id"] = parent_id
    
    endpoint = f"/products/{product_id}/pages"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create page")


async def update_page(
    page_id: str,
    name: Optional[str] = None,
    body: Optional[str] = None,
    ctx: Optional[Context] = None
) -> str:
    """Update page content"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"page": {}}
    
    if name:
        data["page"]["name"] = name
    if body:
        data["page"]["body"] = body
    
    if not data["page"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/pages/{page_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update page")


async def delete_page(
    page_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove pages"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/pages/{page_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete page")


# Idea Portal Management tools

async def list_idea_portals(
    product_id: str,
    ctx: Optional[Context] = None
) -> str:
    """List idea portals"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/products/{product_id}/idea_portals"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list idea portals")


async def list_idea_portal_users(
    idea_portal_id: str,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List portal users/contacts"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/idea_portals/{idea_portal_id}/portal_users"
    params = []
    
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list idea portal users")


async def create_idea_portal_user(
    idea_portal_id: str,
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    permission: Optional[str] = None,
    enabled: Optional[bool] = None,
    max_endorsement_override: Optional[int] = None,
    ctx: Optional[Context] = None
) -> str:
    """Add portal users"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate permission
    if permission and permission not in ["employee", "customer"]:
        return json.dumps({
            "error": f"Invalid permission: {permission}. Must be 'employee' or 'customer'"
        })
    
    data = {
        "portal_user": {
            "email": email
        }
    }
    
    if first_name:
        data["portal_user"]["first_name"] = first_name
    if last_name:
        data["portal_user"]["last_name"] = last_name
    if permission:
        data["portal_user"]["permission"] = permission
    if enabled is not None:
        data["portal_user"]["enabled"] = enabled
    if max_endorsement_override is not None:
        data["portal_user"]["max_endorsement_override"] = max_endorsement_override
    
    endpoint = f"/idea_portals/{idea_portal_id}/portal_users"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create idea portal user")


async def update_idea_portal_user(
    idea_portal_id: str,
    user_id: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    enabled: Optional[bool] = None,
    max_endorsement_override: Optional[int] = None,
    unsubscribed: Optional[bool] = None,
    ctx: Optional[Context] = None
) -> str:
    """Update user details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {"portal_user": {}}
    
    if first_name:
        data["portal_user"]["first_name"] = first_name
    if last_name:
        data["portal_user"]["last_name"] = last_name
    if enabled is not None:
        data["portal_user"]["enabled"] = enabled
    if max_endorsement_override is not None:
        data["portal_user"]["max_endorsement_override"] = max_endorsement_override
    if unsubscribed is not None:
        data["portal_user"]["unsubscribed"] = unsubscribed
    
    if not data["portal_user"]:
        return json.dumps({"error": "No fields provided to update"})
    
    endpoint = f"/idea_portals/{idea_portal_id}/portal_users/{user_id}"
    return await execute_rest_api(ctx, "PUT", endpoint, data, "update idea portal user")


async def list_idea_subscriptions(
    idea_id: str,
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List idea subscriptions"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/ideas/{idea_id}/subscriptions"
    params = []
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list idea subscriptions")


async def create_idea_subscription(
    idea_id: str,
    user_email: str,
    ctx: Optional[Context] = None
) -> str:
    """Subscribe users to ideas"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    data = {
        "idea_subscription": {
            "email": user_email
        }
    }
    
    endpoint = f"/ideas/{idea_id}/subscriptions"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create idea subscription")


async def delete_idea_subscription(
    idea_id: str,
    subscription_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove subscriptions"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/ideas/{idea_id}/subscriptions/{subscription_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete idea subscription")


async def list_idea_categories(
    product_id: str,
    ctx: Optional[Context] = None
) -> str:
    """List idea categories"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/products/{product_id}/idea_categories"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list idea categories")


# Strategic Elements Management Tools

async def list_strategic_models(
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List strategy models"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/strategy_models"
    params = []
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list strategic models")


async def get_strategic_model(
    model_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get model details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/strategy_models/{model_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get strategic model")


async def list_strategic_visions(
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List strategic visions"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/strategy_visions"
    params = []
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list strategic visions")


async def get_strategic_vision(
    vision_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get vision details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/strategy_visions/{vision_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get strategic vision")


async def list_strategic_positions(
    page: int = 1,
    per_page: int = 20,
    ctx: Optional[Context] = None
) -> str:
    """List strategic positions"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/strategy_positions"
    params = []
    if page > 1:
        params.append(f"page={page}")
    if per_page != 20:
        params.append(f"per_page={per_page}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    return await execute_rest_api(ctx, "GET", endpoint, operation="list strategic positions")


async def get_strategic_position(
    position_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Get position details"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/strategy_positions/{position_id}"
    return await execute_rest_api(ctx, "GET", endpoint, operation="get strategic position")


# Integration Management Tools

async def list_integrations(
    ctx: Optional[Context] = None
) -> str:
    """List configured integrations"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = "/integrations"
    return await execute_rest_api(ctx, "GET", endpoint, operation="list integrations")


async def create_integration_field(
    record_type: str,
    record_id: str,
    integration_id: str,
    field_name: str,
    field_value: str,
    ctx: Optional[Context] = None
) -> str:
    """Map integration fields"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # Validate record type
    valid_types = ["features", "epics", "idea_endorsements"]
    if record_type not in valid_types:
        return json.dumps({"error": f"Invalid record type. Must be one of: {', '.join(valid_types)}"})
    
    data = {
        "integration_field": {
            "name": field_name,
            "value": field_value
        }
    }
    
    endpoint = f"/{record_type}/{record_id}/integrations/{integration_id}/fields"
    return await execute_rest_api(ctx, "POST", endpoint, data, "create integration field")


async def update_integration_field(
    record_type: str,
    record_id: str,
    integration_id: str,
    field_name: str,
    field_value: str,
    ctx: Optional[Context] = None
) -> str:
    """Update field mappings"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    # For updates, we delete and recreate the field since there's no direct update endpoint
    # This follows the pattern used in the API documentation
    return await create_integration_field(record_type, record_id, integration_id, field_name, field_value, ctx)


async def delete_integration_field(
    field_id: str,
    ctx: Optional[Context] = None
) -> str:
    """Remove field mappings"""
    auth_error = check_auth()
    if auth_error:
        return auth_error
    
    endpoint = f"/integration_fields/{field_id}"
    return await execute_rest_api(ctx, "DELETE", endpoint, operation="delete integration field")