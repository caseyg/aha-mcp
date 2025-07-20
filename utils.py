"""Utility functions for Aha! MCP tools to reduce code duplication."""

import re
import json
from typing import Optional, List, Dict, Any
from fastmcp import Context
from client import graphql, check_auth, rest_api


def require_auth(func):
    """Decorator to handle authentication checking"""
    async def wrapper(*args, **kwargs):
        auth_error = check_auth()
        if auth_error:
            return auth_error
        return await func(*args, **kwargs)
    return wrapper


async def execute_graphql_query(
    ctx: Context, 
    query: str, 
    variables: Dict[str, Any] = None, 
    result_key: Optional[str] = None, 
    operation: str = "operation"
) -> str:
    """Execute GraphQL query with standardized error handling"""
    try:
        data = await graphql(ctx, query, variables or {})
        result = data.get(result_key) if result_key else data
        return json.dumps(result or {"error": f"No data returned for {operation}"}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to {operation}: {str(e)}"})


async def execute_mutation(
    ctx: Context, 
    query: str, 
    variables: Dict[str, Any], 
    mutation_name: str, 
    target_key: str, 
    action: str
) -> str:
    """Execute mutation with standardized error handling"""
    try:
        data = await graphql(ctx, query, variables)
        result = data.get(mutation_name, {})
        
        if result.get("errors") and result["errors"].get("attributes"):
            return json.dumps({"error": f"Failed to {action}", "details": result["errors"]})
        
        return json.dumps(result.get(target_key, {}), indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to {action}: {str(e)}"})


def build_filters(**kwargs) -> str:
    """Build GraphQL filter string from keyword arguments"""
    filters = []
    for key, value in kwargs.items():
        if value is not None:
            if isinstance(value, bool):
                filters.append(f'{key}: {str(value).lower()}')
            elif isinstance(value, str):
                filters.append(f'{key}: "{value}"')
            else:
                filters.append(f'{key}: {value}')
    return ", ".join(filters)


def build_attributes(
    required_fields: Dict[str, Any], 
    optional_fields: Optional[Dict[str, Any]] = None, 
    nested_objects: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Build attributes dictionary for mutations"""
    attributes = required_fields.copy()
    
    if optional_fields:
        for key, value in optional_fields.items():
            if value is not None:
                attributes[key] = value
    
    if nested_objects:
        for key, value in nested_objects.items():
            if value is not None:
                if isinstance(value, dict):
                    attributes[key] = value
                else:
                    attributes[key] = {"id": value}
    
    return attributes


def validate_reference(reference: str, expected_format: str) -> Optional[str]:
    """Validate reference format and return error message if invalid"""
    patterns = {
        "feature": r'^[A-Z0-9]+-\d+$',
        "requirement": r'^[A-Z0-9]+-\d+-\d+$',
        "page": r'^[A-Z0-9]+-N-\d+$',
        "idea": r'^[A-Z0-9]+-I-\d+$',
        "epic": r'^[A-Z0-9]+-E-\d+$',
        "release": r'^[A-Z0-9]+-R-\d+$',
        "initiative": r'^[A-Z0-9]+-IN-\d+$',
        "goal": r'^[A-Z0-9]+-G-\d+$'
    }
    
    pattern = patterns.get(expected_format)
    if not pattern or not re.match(pattern, reference):
        return json.dumps({"error": f"Invalid {expected_format} reference format: {reference}"})
    return None


def build_list_query(
    resource_name: str,
    fields: List[str],
    filters: Optional[Dict[str, Any]] = None,
    page: int = 1,
    per_page: int = 20
) -> tuple[str, Dict[str, Any]]:
    """Build standardized list query with pagination"""
    
    field_str = " ".join(fields)
    filter_str = build_filters(**filters) if filters else ""
    filter_clause = f"filters: {{{filter_str}}}, " if filter_str else ""
    
    query = f"""query {{
        {resource_name}({filter_clause}page: {page}, per: {per_page}) {{
            nodes {{ {field_str} }}
            currentPage totalCount totalPages
        }}
    }}"""
    
    return query, {}


class CrudTemplates:
    """Templates for common CRUD operations"""
    
    @staticmethod
    def get_query(resource_name: str, fields: List[str]) -> str:
        field_str = " ".join(fields)
        return f"""query($id: ID!) {{
            {resource_name}(id: $id) {{ {field_str} }}
        }}"""
    
    @staticmethod
    def create_mutation(resource_name: str, return_fields: List[str]) -> str:
        field_str = " ".join(return_fields)
        return f"""mutation($attrs: {resource_name.title()}Attributes!) {{
            create{resource_name.title()}(attributes: $attrs) {{
                {resource_name} {{ {field_str} }}
                errors {{ attributes {{ name fullMessages }} }}
            }}
        }}"""
    
    @staticmethod
    def update_mutation(resource_name: str, return_fields: List[str]) -> str:
        field_str = " ".join(return_fields)
        return f"""mutation($id: ID!, $attrs: {resource_name.title()}Attributes!) {{
            update{resource_name.title()}(id: $id, attributes: $attrs) {{
                {resource_name} {{ {field_str} }}
                errors {{ attributes {{ name fullMessages }} }}
            }}
        }}"""
    
    @staticmethod
    def delete_mutation(resource_name: str) -> str:
        return f"""mutation($id: ID!) {{
            delete{resource_name.title()}(id: $id) {{
                {resource_name} {{ id referenceNum }}
                errors {{ attributes {{ name fullMessages }} }}
            }}
        }}"""
    
    @staticmethod
    def promote_mutation(source_resource: str, target_resource: str, return_fields: List[str]) -> str:
        field_str = " ".join(return_fields)
        return f"""mutation($id: ID!, $attrs: {target_resource.title()}Attributes!) {{
            promote{source_resource.title()}(id: $id, attributes: $attrs) {{
                {target_resource} {{ {field_str} }}
                errors {{ attributes {{ name fullMessages }} }}
            }}
        }}"""


def build_standard_fields(resource_name: str) -> List[str]:
    """Get standard fields for a resource type"""
    base_fields = ["id", "referenceNum", "name"]
    
    extended_fields = {
        "feature": base_fields + [
            "description { htmlBody }",
            "workflowStatus { id name }",
            "assignedToUser { id name email }",
            "release { id referenceNum name }",
            "epic { id referenceNum name }"
        ],
        "requirement": base_fields + [
            "description { htmlBody }",
            "position",
            "originalEstimate",
            "remainingEstimate", 
            "initialEstimate",
            "workDone",
            "workflowStatus { id name }",
            "assignedToUser { id name email }",
            "feature { id referenceNum name }",
            "team { id name }",
            "createdAt"
        ],
        "epic": base_fields + [
            "description { htmlBody }",
            "workflowStatus { id name }",
            "assignedToUser { id name email }",
            "release { id referenceNum name }",
            "project { id name }"
        ],
        "idea": base_fields + [
            "description { htmlBody }",
            "workflowStatus { id name }",
            "assignedToUser { id name }",
            "score", "visibility", "promotableId",
            "createdAt", "updatedAt"
        ],
        "release": base_fields + [
            "developmentStartedOn", "endOn",
            "owner { id name email }",
            "parkingLot", "createdAt"
        ],
        "initiative": base_fields + [
            "description { htmlBody }",
            "workflowStatus { id name }",
            "assignedToUser { id name email }",
            "project { id name }"
        ],
        "goal": base_fields + [
            "metricName", "color",
            "project { id name }",
            "parent { id referenceNum name }",
            "createdAt", "createdByUser { id name }"
        ],
        "requirement": base_fields + [
            "description { htmlBody }",
            "feature { id referenceNum name }"
        ],
        "comment": [
            "id", "body { htmlBody }",
            "createdAt", "updatedAt",
            "user { id name email }"
        ]
    }
    
    return extended_fields.get(resource_name, base_fields)


async def execute_rest_api(
    ctx: Context,
    method: str,
    endpoint: str,
    data: Optional[Any] = None,
    operation: str = "operation"
) -> str:
    """Execute REST API request with standardized error handling"""
    try:
        result = await rest_api(ctx, method, endpoint, data)
        
        if result is None:
            # DELETE operations typically return None
            return json.dumps({"success": True, "message": f"{operation.title()} completed successfully"})
        
        return json.dumps(result, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to {operation}: {str(e)}"})