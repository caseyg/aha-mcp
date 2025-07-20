"""MCP tools for interacting with Aha! API."""

import re
import json
from typing import Optional, List
from fastmcp import FastMCP, Context
from client import graphql, check_auth, rest_api

# This will be set by the main module
mcp: Optional[FastMCP] = None


def register_tools(mcp_instance: FastMCP):
    """Register all tools with the MCP instance"""
    global mcp
    mcp = mcp_instance
    
    # Register all tools
    mcp.tool(get_record)
    mcp.tool(search_documents)
    mcp.tool(list_features)
    mcp.tool(create_feature)
    mcp.tool(update_feature)
    mcp.tool(update_feature_tags)
    mcp.tool(get_all_tags)
    mcp.tool(delete_feature)
    mcp.tool(get_feature_details)
    mcp.tool(get_page)
    mcp.tool(create_idea)
    mcp.tool(get_idea)
    mcp.tool(list_ideas)
    mcp.tool(update_idea)
    mcp.tool(delete_idea)
    mcp.tool(list_projects)
    mcp.tool(introspection)


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