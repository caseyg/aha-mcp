"""Aha! API client with GraphQL and authentication support."""

import os
import json
import logging
from typing import Optional, Dict, Any, List, Tuple, Union
from dotenv import load_dotenv
import httpx
from fastmcp import Context

# Load environment
load_dotenv()
logger = logging.getLogger(__name__)

# Configuration
AHA_DOMAIN = os.getenv("AHA_DOMAIN", "")
AHA_API_TOKEN = os.getenv("AHA_API_TOKEN", "")
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID", "")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET", "")

# In-memory token storage (for demonstration)
oauth_tokens: Dict[str, str] = {}


def check_auth() -> Optional[str]:
    """Check if authentication is configured, return error message if not"""
    if not AHA_API_TOKEN and not oauth_tokens:
        return json.dumps({
            "error": "Authentication required",
            "message": "Please set AHA_API_TOKEN environment variable or authenticate with OAuth",
            "oauth_available": bool(OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET)
        })
    return None


def get_auth_headers(ctx: Optional[Context] = None) -> Dict[str, str]:
    """Get authentication headers for API requests"""
    # Check for OAuth token first (if we have a user context)
    if ctx and hasattr(ctx, 'user_id') and ctx.user_id in oauth_tokens:
        return {"Authorization": f"Bearer {oauth_tokens[ctx.user_id]}"}
    
    # Fall back to API token
    if AHA_API_TOKEN:
        return {"Authorization": f"Bearer {AHA_API_TOKEN}"}
    
    # Check if there's any OAuth token (for single-user scenarios)
    if oauth_tokens:
        # Use the first available token
        token = next(iter(oauth_tokens.values()))
        return {"Authorization": f"Bearer {token}"}
    
    return {}


async def graphql(ctx: Context, query: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute GraphQL query against Aha! API"""
    headers = get_auth_headers(ctx)
    
    if not headers:
        raise RuntimeError("No authentication configured")
    
    # Determine domain
    domain = AHA_DOMAIN
    if not domain and oauth_tokens:
        # Try to extract domain from OAuth scenario
        # In a real implementation, you might store domain with the token
        domain = AHA_DOMAIN or "your-domain"
    
    if not domain:
        raise RuntimeError("AHA_DOMAIN not configured")
    
    url = f"https://{domain}.aha.io/api/v2/graphql"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json={"query": query, "variables": variables or {}},
            headers=headers
        )
        
        if response.status_code == 401:
            raise RuntimeError("Authentication failed. Please check your API token or OAuth credentials.")
        
        response.raise_for_status()
        data = response.json()
        
        if "errors" in data and data["errors"]:
            error_messages = [e.get("message", str(e)) for e in data["errors"]]
            raise RuntimeError(f"GraphQL errors: {error_messages}")
        
        return data.get("data", {})


async def rest_api(ctx: Context, method: str, endpoint: str, data: Optional[Union[Dict, List[Tuple[str, str]]]] = None, use_form_data: bool = False) -> Any:
    """Execute REST API request against Aha! API"""
    headers = get_auth_headers(ctx)
    headers["Accept"] = "application/json"
    
    if not headers.get("Authorization"):
        raise RuntimeError("No authentication configured")
    
    # Determine domain
    domain = AHA_DOMAIN
    if not domain and oauth_tokens:
        domain = AHA_DOMAIN or "your-domain"
    
    if not domain:
        raise RuntimeError("AHA_DOMAIN not configured")
    
    # Construct URL - endpoint should start with /
    # If endpoint doesn't start with /api/, assume it's a v1 REST API endpoint
    if not endpoint.startswith("/api/"):
        endpoint = f"/api/v1{endpoint}"
    url = f"https://{domain}.aha.io{endpoint}"
    
    async with httpx.AsyncClient() as client:
        if method.upper() == "GET":
            response = await client.get(url, headers=headers)
        elif method.upper() == "POST":
            if use_form_data and data:
                # For form data, httpx expects data parameter
                response = await client.post(url, data=data, headers=headers)
            else:
                headers["Content-Type"] = "application/json"
                response = await client.post(url, json=data, headers=headers)
        elif method.upper() == "PUT":
            if use_form_data and data:
                response = await client.put(url, data=data, headers=headers)
            else:
                headers["Content-Type"] = "application/json"
                response = await client.put(url, json=data, headers=headers)
        elif method.upper() == "DELETE":
            response = await client.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        if response.status_code == 401:
            raise RuntimeError("Authentication failed. Please check your API token or OAuth credentials.")
        
        response.raise_for_status()
        
        # Some endpoints return empty responses
        if response.content:
            return response.json()
        return None