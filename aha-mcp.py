#!/usr/bin/env python3
"""
Aha! MCP Server - FastMCP implementation with built-in OAuth support
"""
import os
import re
import json
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import httpx
from fastmcp import FastMCP, Context
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent
# Removed BearerAuthProvider import since we're using a simple custom auth provider
from starlette.responses import JSONResponse, RedirectResponse, HTMLResponse
from authlib.common.security import generate_token

# Load environment variables
load_dotenv()

# Configuration
AHA_DOMAIN = os.getenv("AHA_DOMAIN", "secure")
AHA_API_TOKEN = os.getenv("AHA_API_TOKEN")
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
OAUTH_REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI", "http://localhost:8000/oauth/callback")

# OAuth storage for mapping MCP tokens to Aha! tokens
aha_tokens_db = {}  # Maps MCP Bearer tokens to Aha! access tokens
oauth_sessions = {}  # Temporary session storage for OAuth flow

# Create FastMCP server without auth provider - we'll handle auth manually in tools
mcp = FastMCP("aha-mcp")

# Reference number patterns
PATTERNS = {
    "feature": re.compile(r"^([A-Z][A-Z0-9]*)-(\d+)$"),
    "requirement": re.compile(r"^([A-Z][A-Z0-9]*)-(\d+)-(\d+)$"),
    "page": re.compile(r"^([A-Z][A-Z0-9]*)-N-(\d+)$"),
    "idea": re.compile(r"^([A-Z][A-Z0-9]*)-I-(\d+)$")
}

# GraphQL helper with authentication
async def graphql(ctx: Context, query: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
    """Execute GraphQL query with authentication"""
    auth_header = None
    
    # Try to extract Bearer token from request context
    if hasattr(ctx, 'request_context') and ctx.request_context:
        # Handle different ways FastMCP might provide request context
        try:
            # Try to access the actual HTTP request object
            if hasattr(ctx.request_context, 'request') and ctx.request_context.request:
                request = ctx.request_context.request
                auth = request.headers.get('authorization') or request.headers.get('Authorization')
            else:
                # Try accessing as dictionary
                if hasattr(ctx.request_context, 'get'):
                    auth = ctx.request_context.get('authorization') or ctx.request_context.get('Authorization')
                else:
                    # Try accessing as object attributes
                    auth = getattr(ctx.request_context, 'authorization', None) or getattr(ctx.request_context, 'Authorization', None)
                
            if auth and auth.startswith('Bearer '):
                mcp_token = auth[7:]  # Remove "Bearer " prefix
                # Check if this is a mapped OAuth token
                aha_token = aha_tokens_db.get(mcp_token)
                if aha_token:
                    auth_header = f"Bearer {aha_token}"
                else:
                    # Use the token directly (might be an API token)
                    auth_header = auth
        except Exception as e:
            logger.debug(f"Could not extract auth from request context: {e}")
            pass
    
    # Fall back to API token from environment
    if not auth_header:
        if not AHA_API_TOKEN:
            raise ValueError("No authentication available. Set AHA_API_TOKEN or use OAuth.")
        auth_header = f"Bearer {AHA_API_TOKEN}"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://{AHA_DOMAIN}.aha.io/api/v2/graphql",
            json={"query": query, "variables": variables or {}},
            headers={"Authorization": auth_header, "Content-Type": "application/json"}
        )
        response.raise_for_status()
        result = response.json()
        if "errors" in result:
            raise RuntimeError(f"GraphQL errors: {result['errors']}")
        return result.get("data", {})

# Tools
@mcp.tool
async def get_record(reference: str, ctx: Context) -> str:
    """Get an Aha! record by reference (e.g., PROJ-123, ADT-123-1, ABC-I-123)"""
    # Determine record type
    if PATTERNS["feature"].match(reference):
        query = "query($id: ID!) { feature(id: $id) { referenceNum name description { htmlBody } } }"
        data = await graphql(ctx, query, {"id": reference})
        return json.dumps(data.get("feature") or {"error": f"Feature {reference} not found"}, indent=2)
    
    elif PATTERNS["requirement"].match(reference):
        query = "query($id: ID!) { requirement(id: $id) { referenceNum name description { htmlBody } } }"
        data = await graphql(ctx, query, {"id": reference})
        return json.dumps(data.get("requirement") or {"error": f"Requirement {reference} not found"}, indent=2)
    
    elif PATTERNS["idea"].match(reference):
        query = """query($id: ID!) { 
            idea(id: $id) { 
                id referenceNum name description { htmlBody } 
                visibility score createdAt updatedAt 
            } 
        }"""
        data = await graphql(ctx, query, {"id": reference})
        return json.dumps(data.get("idea") or {"error": f"Idea {reference} not found"}, indent=2)
    
    else:
        return json.dumps({"error": f"Invalid reference format: {reference}"}, indent=2)

@mcp.tool
async def search_documents(query: str, searchable_type: str = "Page", ctx: Context = None) -> str:
    """Search Aha! documents"""
    gql = """query($query: String!, $type: [String!]!) {
        searchDocuments(filters: {query: $query, searchableType: $type}) {
            nodes { name url searchableId searchableType }
            currentPage totalCount totalPages
        }
    }"""
    data = await graphql(ctx, gql, {"query": query, "type": [searchable_type]})
    return json.dumps(data.get("searchDocuments", {}), indent=2)

@mcp.tool
async def list_features(
    project_id: Optional[str] = None,
    release_id: Optional[str] = None,
    epic_id: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List features with filters"""
    if not any([project_id, release_id, epic_id]):
        return json.dumps({"error": "At least one filter required: project_id, release_id, or epic_id"}, indent=2)
    
    filters = {}
    if project_id: filters["projectId"] = project_id
    if release_id: filters["releaseId"] = release_id
    if epic_id: filters["epicId"] = epic_id
    
    query = """query($filters: FeatureFilters!, $page: Int!, $per: Int!) {
        features(filters: $filters, page: $page, per: $per) {
            nodes {
                id referenceNum name
                description { htmlBody }
                workflowStatus { id name }
                release { id referenceNum name }
                assignedToUser { id name }
            }
            currentPage totalCount totalPages
        }
    }"""
    
    data = await graphql(ctx, query, {"filters": filters, "page": page, "per": per_page})
    return json.dumps(data.get("features", {}), indent=2)

@mcp.tool
async def create_feature(
    release_id: str,
    name: str,
    description: Optional[str] = None,
    assigned_to_user_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
    ctx: Context = None
) -> str:
    """Create a new feature"""
    attributes = {"name": name, "release": {"id": release_id}}
    if description: attributes["description"] = description
    if assigned_to_user_id: attributes["assignedToUser"] = {"id": assigned_to_user_id}
    if tags: attributes["tagList"] = ", ".join(tags)
    
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
        errors_str = str(result["errors"]["attributes"])
        return json.dumps({"error": f"Failed to create: {errors_str}"}, indent=2)
    
    return json.dumps(result.get("feature", {}), indent=2)

@mcp.tool
async def create_idea(
    project_id: str,
    name: str,
    assigned_to_user_id: Optional[str] = None,
    workflow_status_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """Create a new idea"""
    attributes = {
        "name": name,
        "project": {"id": project_id}
    }
    if assigned_to_user_id: 
        attributes["assignedToUser"] = {"id": assigned_to_user_id}
    if workflow_status_id: 
        attributes["workflowStatus"] = {"id": workflow_status_id}
    
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
        errors_str = str(result["errors"]["attributes"])
        return json.dumps({"error": f"Failed to create: {errors_str}"}, indent=2)
    
    return json.dumps(result.get("idea", {}), indent=2)

@mcp.tool
async def get_page(reference: str, include_parent: bool = False, ctx: Context = None) -> str:
    """Get an Aha! page by reference number with optional relationships"""
    if not PATTERNS["page"].match(reference):
        return json.dumps({"error": f"Invalid page reference format: {reference}. Expected ABC-N-213"}, indent=2)
    
    query = """query($id: ID!, $includeParent: Boolean!) {
        page(id: $id) {
            id referenceNum name
            description { htmlBody }
            parent @include(if: $includeParent) {
                id referenceNum name
            }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": reference, "includeParent": include_parent})
    return json.dumps(data.get("page") or {"error": f"Page {reference} not found"}, indent=2)

@mcp.tool
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
        errors_str = str(result["errors"]["attributes"])
        return json.dumps({"error": f"Failed to update: {errors_str}"}, indent=2)
    
    return json.dumps(result.get("feature", {}), indent=2)

@mcp.tool
async def delete_feature(id: str, ctx: Context = None) -> str:
    """Delete a feature"""
    query = """mutation($id: ID!) {
        deleteFeature(id: $id) {
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
        errors_str = str(result["errors"]["attributes"])
        return json.dumps({"error": f"Failed to delete: {errors_str}"}, indent=2)
    
    return json.dumps({"success": True, "id": id}, indent=2)

@mcp.tool
async def get_feature_details(id: str, ctx: Context = None) -> str:
    """Get detailed information about a specific feature"""
    query = """query($id: ID!) {
        feature(id: $id) {
            id referenceNum name
            description { htmlBody }
            workflowStatus { id name }
            release { id referenceNum name }
            assignedToUser { id name }
            tags { id name color }
            createdAt updatedAt
            epic { id referenceNum name }
            team { id name }
        }
    }"""
    
    data = await graphql(ctx, query, {"id": id})
    return json.dumps(data.get("feature") or {"error": f"Feature {id} not found"}, indent=2)

@mcp.tool
async def get_idea(id: str, ctx: Context = None) -> str:
    """Get an Aha! idea by ID or reference number"""
    query = """query($id: ID!) { 
        idea(id: $id) { 
            id referenceNum name description { htmlBody } 
            visibility score createdAt updatedAt
            assignedToUser { id name }
            promotable { 
                ... on Feature { id referenceNum }
                ... on Epic { id referenceNum }
                ... on Requirement { id referenceNum }
            }
            workflowStatus { id name }
        } 
    }"""
    data = await graphql(ctx, query, {"id": id})
    return json.dumps(data.get("idea") or {"error": f"Idea {id} not found"}, indent=2)

@mcp.tool
async def list_ideas(
    project_id: str,
    assigned_to_user_id: Optional[str] = None,
    visibility: Optional[str] = None,
    promoted: Optional[bool] = None,
    page: int = 1,
    per_page: int = 20,
    ctx: Context = None
) -> str:
    """List ideas in a project with optional filters"""
    filters = {"projectId": project_id}
    if assigned_to_user_id: filters["assignedToUserId"] = assigned_to_user_id
    if visibility: filters["visibility"] = visibility
    if promoted is not None: filters["promoted"] = promoted
    
    query = """query($filters: IdeaFilters!, $page: Int!, $per: Int!) {
        ideas(filters: $filters, page: $page, per: $per) {
            nodes {
                id referenceNum name
                description { htmlBody }
                visibility score
                assignedToUser { id name }
                createdAt updatedAt
            }
            currentPage totalCount totalPages
        }
    }"""
    
    data = await graphql(ctx, query, {"filters": filters, "page": page, "per": per_page})
    return json.dumps(data.get("ideas", {}), indent=2)

@mcp.tool
async def update_idea(
    id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,  # Not supported by API, kept for compatibility
    visibility: Optional[str] = None,   # Not supported by API, kept for compatibility
    assigned_to_user_id: Optional[str] = None,
    tags: Optional[List[str]] = None,   # Not supported by API, kept for compatibility
    workflow_status_id: Optional[str] = None,
    score: Optional[float] = None,      # Not supported by API, kept for compatibility
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
    attributes = {}
    if name: attributes["name"] = name
    # Note: description, visibility, tags, and score are not supported in IdeaAttributes
    if assigned_to_user_id: attributes["assignedToUser"] = {"id": assigned_to_user_id}
    if workflow_status_id: attributes["workflowStatus"] = {"id": workflow_status_id}
    
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
        errors_str = str(result["errors"]["attributes"])
        return json.dumps({"error": f"Failed to update: {errors_str}"}, indent=2)
    
    return json.dumps(result.get("idea", {}), indent=2)

@mcp.tool
async def delete_idea(id: str, ctx: Context = None) -> str:
    """Delete an idea using REST API"""
    # Extract authentication
    auth_header = None
    
    # Try to extract Bearer token from request context
    if hasattr(ctx, 'request_context') and ctx.request_context:
        try:
            if hasattr(ctx.request_context, 'request') and ctx.request_context.request:
                request = ctx.request_context.request
                auth = request.headers.get('authorization') or request.headers.get('Authorization')
            else:
                if hasattr(ctx.request_context, 'get'):
                    auth = ctx.request_context.get('authorization') or ctx.request_context.get('Authorization')
                else:
                    auth = getattr(ctx.request_context, 'authorization', None) or getattr(ctx.request_context, 'Authorization', None)
                
            if auth and auth.startswith('Bearer '):
                mcp_token = auth[7:]
                aha_token = aha_tokens_db.get(mcp_token)
                if aha_token:
                    auth_header = f"Bearer {aha_token}"
                else:
                    auth_header = auth
        except Exception as e:
            logger.debug(f"Could not extract auth from request context: {e}")
            pass
    
    # Fall back to API token from environment
    if not auth_header:
        if not AHA_API_TOKEN:
            raise ValueError("No authentication available. Set AHA_API_TOKEN or use OAuth.")
        auth_header = f"Bearer {AHA_API_TOKEN}"
    
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"https://{AHA_DOMAIN}.aha.io/api/v1/ideas/{id}",
            headers={
                "Authorization": auth_header,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )
        
        if response.status_code == 204:
            # Successful deletion returns 204 No Content
            return json.dumps({"success": True, "id": id}, indent=2)
        elif response.status_code == 404:
            return json.dumps({"error": f"Idea {id} not found"}, indent=2)
        else:
            try:
                error_data = response.json()
                return json.dumps({"error": f"Failed to delete: {error_data}"}, indent=2)
            except:
                return json.dumps({"error": f"Failed to delete: HTTP {response.status_code}"}, indent=2)

@mcp.tool
async def introspection(
    query_type: str = "list-types", 
    type_name: Optional[str] = None,
    search_term: Optional[str] = None, 
    ctx: Context = None
) -> str:
    """Explore Aha! GraphQL schema"""
    
    if query_type == "type" and type_name:
        # Get detailed information about a specific type
        query = f"""query {{
            __type(name: "{type_name}") {{
                name
                kind
                description
                fields {{
                    name
                    type {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                        }}
                    }}
                    description
                }}
                inputFields {{
                    name
                    type {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                        }}
                    }}
                    description
                    defaultValue
                }}
            }}
        }}"""
        
        data = await graphql(ctx, query)
        return json.dumps(data.get("__type", {}), indent=2)
    
    elif query_type == "mutation-args":
        # Get detailed information about specific mutation arguments
        mutation_name = search_term or "createIdea"
        query = f"""query {{
            __schema {{
                mutationType {{
                    fields(includeDeprecated: true) {{
                        name
                        description
                        args {{
                            name
                            type {{
                                name
                                kind
                                ofType {{
                                    name
                                    kind
                                    inputFields {{
                                        name
                                        type {{
                                            name
                                            kind
                                            ofType {{
                                                name
                                                kind
                                            }}
                                        }}
                                        description
                                        defaultValue
                                    }}
                                }}
                            }}
                            description
                            defaultValue
                        }}
                    }}
                }}
            }}
        }}"""
        
        data = await graphql(ctx, query)
        schema = data.get("__schema", {})
        
        # Filter to specific mutation if provided
        if "mutationType" in schema and "fields" in schema["mutationType"]:
            schema["mutationType"]["fields"] = [
                f for f in schema["mutationType"]["fields"] 
                if f["name"] == mutation_name
            ]
        
        return json.dumps(schema, indent=2)
    
    else:
        # Default list types query
        query = """query {
            __schema {
                types { name kind description }
                queryType { fields { name description } }
                mutationType { fields { name description } }
            }
        }"""
        
        data = await graphql(ctx, query)
        schema = data.get("__schema", {})
        
        # Filter by search term if provided
        if search_term:
            lower = search_term.lower()
            if "types" in schema:
                schema["types"] = [t for t in schema["types"] if lower in t["name"].lower()][:20]
            for field in ["queryType", "mutationType"]:
                if field in schema and "fields" in schema[field]:
                    schema[field]["fields"] = [
                        f for f in schema[field]["fields"] 
                        if lower in f["name"].lower()
                    ][:20]
        
        return json.dumps(schema, indent=2)

# Prompts for common Aha! workflows
@mcp.prompt
def analyze_feature_backlog(project_id: str, release_id: Optional[str] = None) -> list[Message]:
    """Generate a prompt to analyze your feature backlog"""
    messages = [
        Message(f"I need to analyze the feature backlog for project {project_id}.")
    ]
    
    if release_id:
        messages.append(Message(f"Please focus specifically on release {release_id}."))
    else:
        messages.append(Message("Please analyze features across all releases."))
    
    messages.extend([
        Message("For the analysis, please:"),
        Message("1. List all features grouped by workflow status"),
        Message("2. Identify any features without assigned users"),
        Message("3. Highlight features that might be blocked or at risk"),
        Message("4. Provide a summary of the overall backlog health"),
        Message("5. Suggest any items that need immediate attention")
    ])
    
    return messages

@mcp.prompt
def create_feature_spec(
    feature_name: str, 
    release_id: str,
    user_story: str,
    acceptance_criteria: Optional[str] = None
) -> str:
    """Generate a prompt to create a detailed feature specification"""
    prompt = f"""Please help me create a comprehensive feature specification for:

Feature Name: {feature_name}
Target Release: {release_id}

User Story:
{user_story}

"""
    
    if acceptance_criteria:
        prompt += f"""Acceptance Criteria:
{acceptance_criteria}

"""
    
    prompt += """Based on this information, please:
1. Create a detailed feature description in HTML format suitable for Aha!
2. Break down the feature into clear implementation requirements
3. Identify potential technical challenges or dependencies
4. Suggest appropriate tags for categorization
5. Recommend a workflow status to start with

Format the response so I can easily create the feature in Aha! using the create_feature tool."""
    
    return prompt

@mcp.prompt
def idea_evaluation(
    project_id: str,
    evaluation_criteria: str = "value, effort, risk"
) -> list[Message]:
    """Generate a prompt to evaluate ideas in a project"""
    return [
        Message(f"I need to evaluate ideas in project {project_id}."),
        Message(f"Please analyze the ideas based on these criteria: {evaluation_criteria}"),
        Message("For each idea, provide:"),
        Message("1. A brief summary of what it proposes"),
        Message("2. An evaluation score for each criterion (1-10)"),
        Message("3. Potential implementation challenges"),
        Message("4. Recommendation on whether to promote to a feature"),
        Message("5. If promoting, suggest which release it should target"),
        Message("Create a prioritized list with your top recommendations.")
    ]

@mcp.prompt
def release_planning(
    release_id: str,
    team_capacity: Optional[str] = None,
    focus_areas: Optional[str] = None
) -> str:
    """Generate a prompt for release planning and capacity analysis"""
    prompt = f"""I need help with release planning for release {release_id}.

"""
    
    if team_capacity:
        prompt += f"Team Capacity: {team_capacity}\n"
    
    if focus_areas:
        prompt += f"Focus Areas: {focus_areas}\n"
    
    prompt += """
Please analyze the current release and provide:

1. **Current State Analysis**
   - Total number of features and their status breakdown
   - Features by assignee
   - High-risk or blocked items

2. **Capacity Planning**
   - Estimate if the current scope fits within capacity
   - Identify any overallocated team members
   - Suggest features that could be moved if needed

3. **Release Readiness**
   - Features still in early stages that might not complete
   - Dependencies between features
   - Testing and deployment considerations

4. **Recommendations**
   - Priority adjustments needed
   - Features to accelerate or defer
   - Resource reallocation suggestions

Please be specific with feature references (e.g., PROJ-123) in your analysis."""
    
    return prompt

@mcp.prompt
def bug_triage_session(
    tag: Optional[str] = None,
    severity_threshold: str = "high",
    age_days: int = 7
) -> list[Message]:
    """Generate a prompt for bug triage session"""
    messages = [
        Message("I need to conduct a bug triage session."),
        Message(f"Focus on bugs with severity {severity_threshold} or higher that are at least {age_days} days old.")
    ]
    
    if tag:
        messages.append(Message(f"Filter to bugs tagged with: {tag}"))
    
    messages.extend([
        Message("For each bug, please determine:"),
        Message("1. Current severity assessment - is it still accurate?"),
        Message("2. Root cause category (UI, backend, data, integration, etc.)"),
        Message("3. Estimated effort (S/M/L/XL)"),
        Message("4. Priority recommendation (P0/P1/P2/P3)"),
        Message("5. Suggested assignee based on expertise area"),
        Message("Group the bugs by root cause category and provide a summary of patterns.")
    ])
    
    return messages

@mcp.prompt
def feature_dependencies_analysis(
    feature_reference: str,
    check_upstream: bool = True,
    check_downstream: bool = True
) -> str:
    """Generate a prompt to analyze feature dependencies"""
    directions = []
    if check_upstream:
        directions.append("upstream (what this feature depends on)")
    if check_downstream:
        directions.append("downstream (what depends on this feature)")
    
    direction_text = " and ".join(directions)
    
    return f"""Please analyze the dependencies for feature {feature_reference}.

I need to understand the {direction_text} dependencies.

For each dependency found, provide:
1. The feature/requirement reference and name
2. The type of dependency (blocks, relates to, child of, etc.)
3. Current status of the dependent item
4. Risk assessment if the dependency is not resolved
5. Suggested mitigation strategies

Also create a visual representation using text/ASCII that shows the dependency chain.

Finally, provide recommendations on:
- Critical path items that could block {feature_reference}
- Optimal sequence for implementation
- Any circular dependencies detected
- Resource conflicts across dependent features"""

@mcp.prompt
def sprint_retrospective(
    sprint_name: str,
    team_name: Optional[str] = None
) -> list[Message]:
    """Generate a prompt for sprint retrospective analysis"""
    messages = [
        Message(f"Let's conduct a retrospective analysis for sprint: {sprint_name}")
    ]
    
    if team_name:
        messages.append(Message(f"Focusing on team: {team_name}"))
    
    messages.extend([
        Message("Please analyze the sprint data and provide insights on:"),
        Message("1. **Velocity Metrics**"),
        Message("   - Planned vs completed features"),
        Message("   - Story points delivered (if available)"),
        Message("   - Carry-over items to next sprint"),
        Message("2. **Quality Indicators**"),
        Message("   - Bugs found during sprint"),
        Message("   - Features that required rework"),
        Message("   - Test coverage concerns"),
        Message("3. **Team Performance**"),
        Message("   - Individual contribution balance"),
        Message("   - Collaboration patterns"),
        Message("   - Blocker resolution time"),
        Message("4. **Process Observations**"),
        Message("   - What went well?"),
        Message("   - What could be improved?"),
        Message("   - Action items for next sprint"),
        Message("Format as a retrospective report with specific examples and actionable recommendations.")
    ])
    
    return messages

@mcp.prompt(
    description="Generate a prompt to create weekly status report",
    tags={"reporting", "status", "weekly"}
)
def weekly_status_report(
    project_id: str,
    week_ending: str,
    include_metrics: bool = True
) -> str:
    """Generate a prompt for creating a weekly status report"""
    prompt = f"""Please generate a comprehensive weekly status report for project {project_id} for the week ending {week_ending}.

Structure the report as follows:

## Executive Summary
- Key accomplishments this week
- Critical issues or blockers
- Overall project health (Green/Yellow/Red)

## Progress Update
- Features completed this week (with references)
- Features in progress (with % complete)
- Features starting next week

"""
    
    if include_metrics:
        prompt += """## Key Metrics
- Features delivered vs planned
- Bug discovery rate
- Team velocity trend
- Release burndown status

"""
    
    prompt += """## Risks and Issues
- New risks identified
- Existing risk status updates
- Mitigation actions needed

## Upcoming Milestones
- Next week's priorities
- Upcoming release dates
- Key decisions needed

## Team Updates
- Resource changes
- PTO/availability impacts
- Recognition/achievements

Please format this in a professional manner suitable for stakeholder distribution."""
    
    return prompt

@mcp.prompt
async def idea_to_feature_conversion(
    idea_reference: str,
    target_release: str,
    ctx: Context
) -> list[Message]:
    """Generate a prompt to guide converting an idea to a feature"""
    # We can use async and access context if needed
    return [
        Message(f"I need to convert idea {idea_reference} into a feature for release {target_release}."),
        Message("Please help me by:"),
        Message("1. First, retrieve and analyze the idea details"),
        Message("2. Enhance the description with implementation details"),
        Message("3. Break down into specific requirements or tasks"),
        Message("4. Suggest appropriate feature metadata:"),
        Message("   - Feature name (refined from idea)"),
        Message("   - Initial workflow status"),
        Message("   - Tags for categorization"),
        Message("   - Effort estimation"),
        Message("   - Assignee recommendation"),
        Message("5. Create the feature creation command with all details"),
        Message("Please ensure all context from the idea is preserved and enhanced in the feature.")
    ]

@mcp.prompt(
    enabled=True,  # Can be toggled on/off
    tags={"automation", "integration"}
)
def integration_checklist(
    feature_reference: str,
    integration_type: str = "API"
) -> str:
    """Generate an integration checklist for a feature"""
    return f"""Create a comprehensive integration checklist for feature {feature_reference} which involves {integration_type} integration.

Generate a checklist covering:

1. **Pre-Integration Requirements**
   - [ ] API/Interface documentation reviewed
   - [ ] Authentication method confirmed
   - [ ] Rate limits understood
   - [ ] Data formats agreed upon
   - [ ] Error handling strategy defined

2. **Implementation Checklist**
   - [ ] Connection configuration
   - [ ] Data mapping completed
   - [ ] Error scenarios handled
   - [ ] Retry logic implemented
   - [ ] Monitoring hooks added

3. **Testing Requirements**
   - [ ] Unit tests for integration logic
   - [ ] Integration tests with mock services
   - [ ] End-to-end testing plan
   - [ ] Performance testing needs
   - [ ] Failure scenario testing

4. **Deployment Considerations**
   - [ ] Environment-specific configs
   - [ ] Secrets management
   - [ ] Rollback strategy
   - [ ] Monitoring and alerts
   - [ ] Documentation updates

5. **Post-Deployment Validation**
   - [ ] Health check verification
   - [ ] Data flow validation
   - [ ] Performance benchmarks met
   - [ ] Error rates within tolerance
   - [ ] User acceptance criteria

Please customize this checklist based on the specific feature requirements and mark any items that need special attention."""

# OAuth discovery endpoints for MCP Inspector compatibility
@mcp.custom_route("/.well-known/oauth-authorization-server", methods=["GET", "OPTIONS"])
async def oauth_discovery_route(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    base_url = str(request.url).split('/.well-known')[0]
    metadata = {
        "issuer": base_url,
        "authorization_endpoint": f"{base_url}/oauth/authorize",
        "token_endpoint": f"{base_url}/oauth/token",
        "registration_endpoint": f"{base_url}/oauth/register",
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code"],
        "code_challenge_methods_supported": ["S256"],
        "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic", "none"],
        "scopes_supported": [],
        "response_modes_supported": ["query", "fragment"],
        "subject_types_supported": ["public"],
        "id_token_signing_alg_values_supported": ["RS256"],
        "claims_supported": ["sub", "iss", "aud", "exp", "iat"]
    }
    
    return JSONResponse(metadata, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
        "Content-Type": "application/json"
    })

@mcp.custom_route("/.well-known/oauth-protected-resource", methods=["GET", "OPTIONS"])
async def oauth_protected_resource(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    base_url = str(request.url).split('/.well-known')[0]
    metadata = {
        "resource": base_url,
        "authorization_servers": [base_url],
        "bearer_methods_supported": ["header"],
        "resource_documentation": "https://github.com/aha-develop/aha-mcp",
        "resource_signing_alg_values_supported": ["RS256"]
    }
    
    return JSONResponse(metadata, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
        "Content-Type": "application/json"
    })

@mcp.custom_route("/oauth/authorize", methods=["GET", "OPTIONS"])
async def oauth_authorize_route(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    params = dict(request.query_params)
    client_id = params.get("client_id")
    redirect_uri = params.get("redirect_uri")
    
    # Generate state for CSRF protection
    state = generate_token()
    oauth_sessions[state] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_challenge": params.get("code_challenge"),
        "original_state": params.get("state"),
        "created_at": datetime.now()
    }
    
    # Redirect to Aha! OAuth (no scope parameter - matches TypeScript implementation)
    aha_params = {
        "client_id": OAUTH_CLIENT_ID,
        "redirect_uri": OAUTH_REDIRECT_URI,
        "response_type": "code",
        "state": state
    }
    
    # Use URLSearchParams-like construction for proper encoding
    from urllib.parse import urlencode
    aha_url = f"https://{AHA_DOMAIN}.aha.io/oauth/authorize?{urlencode(aha_params)}"
    return RedirectResponse(url=aha_url)

@mcp.custom_route("/oauth/callback", methods=["GET", "OPTIONS"])
async def oauth_callback_route(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    
    if not code or not state or state not in oauth_sessions:
        return HTMLResponse("OAuth error: Invalid state", status_code=400)
    
    session_data = oauth_sessions.pop(state)
    
    try:
        # Exchange code for token with Aha!
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://{AHA_DOMAIN}.aha.io/oauth/token",
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "client_id": OAUTH_CLIENT_ID,
                    "client_secret": OAUTH_CLIENT_SECRET,
                    "redirect_uri": OAUTH_REDIRECT_URI
                }
            )
            
            if response.status_code != 200:
                return HTMLResponse(f"Token exchange failed: {response.text}", status_code=400)
            
            token_data = response.json()
            aha_access_token = token_data["access_token"]
        
        # Generate MCP Bearer token
        mcp_token = generate_token()
        
        # Map MCP token to Aha! token
        aha_tokens_db[mcp_token] = aha_access_token
        logger.info(f"OAuth authentication successful for session")
        
        # Redirect back to MCP client with authorization code (not access token)
        # MCP Inspector expects the authorization code, not the final access token
        redirect_url = f"{session_data['redirect_uri']}?code={mcp_token}&state={session_data.get('original_state', '')}"
        return RedirectResponse(url=redirect_url)
        
    except Exception as e:
        return HTMLResponse(f"Callback error: {str(e)}", status_code=400)

@mcp.custom_route("/oauth/token", methods=["POST", "OPTIONS"])
async def oauth_token_route(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    try:
        # Parse form data
        form = await request.form()
        grant_type = form.get("grant_type")
        code = form.get("code")
        
        if grant_type != "authorization_code":
            return JSONResponse({"error": "unsupported_grant_type"}, status_code=400)
        
        if not code:
            return JSONResponse({"error": "invalid_request", "error_description": "Missing code"}, status_code=400)
        
        # Check if we have an Aha! token mapped to this MCP code
        if code not in aha_tokens_db:
            return JSONResponse({"error": "invalid_grant"}, status_code=400)
        
        # Return the MCP Bearer token (which maps to Aha! token)
        return JSONResponse({
            "access_token": code,  # The MCP token that maps to Aha! token
            "token_type": "Bearer",
            "expires_in": 3600,
            "scope": ""
        }, headers={
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        })
        
    except Exception as e:
        return JSONResponse({"error": "server_error", "error_description": str(e)}, status_code=500)

@mcp.custom_route("/oauth/register", methods=["POST", "OPTIONS"])
async def oauth_register_route(request):
    if request.method == "OPTIONS":
        return JSONResponse({}, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
    
    data = await request.json() if request.headers.get("content-type") == "application/json" else {}
    client_id = generate_token()
    redirect_uris = data.get("redirect_uris", ["http://localhost:3000/callback"])
    
    return JSONResponse({
        "client_id": client_id,
        "client_id_issued_at": int(datetime.now().timestamp()),
        "redirect_uris": redirect_uris,
        "grant_types": ["authorization_code"],
        "response_types": ["code"],
        "token_endpoint_auth_method": "none"
    }, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS", 
        "Access-Control-Allow-Headers": "*",
        "Content-Type": "application/json"
    })

if __name__ == "__main__":
    import sys
    
    # Print config info
    print(f"🚀 Aha! MCP Server (FastMCP with built-in auth)")
    print(f"Domain: {AHA_DOMAIN}")
    
    # Check authentication configuration
    if not (AHA_API_TOKEN or (OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET)):
        print("\n❌ Error: Authentication required!")
        print("\nSet either:")
        print("1. API Token: AHA_API_TOKEN=your-token")
        print("2. OAuth: OAUTH_CLIENT_ID=id OAUTH_CLIENT_SECRET=secret")
        sys.exit(1)
    
    if AHA_API_TOKEN:
        print(f"\n✅ API Token configured: {AHA_API_TOKEN[:10]}...")
    
    if OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET:
        print(f"\n✅ OAuth configured with FastMCP BearerAuth:")
        print(f"  Client ID: {OAUTH_CLIENT_ID[:10]}...")
        print(f"  Redirect URI: {OAUTH_REDIRECT_URI}")
    
    print("\n🌐 Starting server with FastMCP built-in authentication...")
    print("\nServer URL: http://localhost:8000/mcp")
    print("\nTo connect:")
    if OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET:
        print("  - Use OAuth authentication in MCP Inspector")
        print("  - URL: http://localhost:8000/mcp")
    if AHA_API_TOKEN:
        print("  - Or use Bearer token with your API token")
    
    
    import uvicorn
    uvicorn.run(mcp.http_app(path='/mcp'), host="0.0.0.0", port=8000, log_level="info")