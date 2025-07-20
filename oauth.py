"""OAuth endpoints and discovery for Aha! MCP server."""

import os
import json
import logging
from typing import Optional
from datetime import datetime
from starlette.responses import JSONResponse, RedirectResponse, HTMLResponse
from authlib.common.security import generate_token
import httpx
from fastmcp import FastMCP

logger = logging.getLogger(__name__)

# Configuration
AHA_DOMAIN = os.getenv("AHA_DOMAIN", "")
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID", "")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET", "")
OAUTH_REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI", "http://localhost:3000/oauth/callback")

# OAuth state storage
oauth_states = {}
oauth_tokens = {}  # This is shared with client.py


def register_oauth_routes(mcp: FastMCP, tokens_dict):
    """Register OAuth routes with the MCP instance"""
    global oauth_tokens
    oauth_tokens = tokens_dict
    
    @mcp.custom_route("/.well-known/oauth-authorization-server", methods=["GET", "OPTIONS"])
    async def oauth_discovery_route(request):
        """OAuth 2.0 Authorization Server Metadata endpoint"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        base_url = str(request.url).split('/.well-known')[0]
        
        return JSONResponse({
            "issuer": base_url,
            "authorization_endpoint": f"{base_url}/oauth/authorize",
            "token_endpoint": f"{base_url}/oauth/token",
            "response_types_supported": ["code"],
            "grant_types_supported": ["authorization_code"],
            "code_challenge_methods_supported": ["S256"],
            "scopes_supported": ["read", "write"],
            "authorization_response_iss_parameter_supported": True
        }, headers={
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        })
    
    @mcp.custom_route("/.well-known/oauth-protected-resource", methods=["GET", "OPTIONS"])
    async def oauth_protected_resource_route(request):
        """OAuth 2.0 Protected Resource Metadata endpoint"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        base_url = str(request.url).split('/.well-known')[0]
        
        return JSONResponse({
            "resource": base_url,
            "authorization_servers": [base_url],
            "bearer_methods_supported": ["header"],
            "resource_documentation": "https://github.com/your-org/aha-mcp",
            "resource_signing_alg_values_supported": ["RS256"]
        }, headers={
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        })
    
    @mcp.custom_route("/oauth/authorize", methods=["GET", "OPTIONS"])
    async def oauth_authorize_route(request):
        """OAuth authorization endpoint"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        # Check if OAuth is configured
        if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_SECRET:
            return HTMLResponse(
                "<h1>OAuth Not Configured</h1><p>Please configure OAuth credentials in environment variables.</p>",
                status_code=500
            )
        
        # Extract parameters
        params = dict(request.query_params)
        client_id = params.get("client_id")
        redirect_uri = params.get("redirect_uri")
        state = params.get("state")
        code_challenge = params.get("code_challenge")
        code_challenge_method = params.get("code_challenge_method")
        
        # Validate client_id
        if client_id != OAUTH_CLIENT_ID:
            return HTMLResponse(
                f"<h1>Invalid Client</h1><p>Unknown client_id: {client_id}</p>",
                status_code=400
            )
        
        # Store state for validation
        if state:
            oauth_states[state] = {
                "redirect_uri": redirect_uri,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "created_at": datetime.now()
            }
        
        # Redirect to Aha! OAuth
        aha_auth_url = f"https://{AHA_DOMAIN}.aha.io/oauth/authorize"
        aha_params = {
            "client_id": OAUTH_CLIENT_ID,
            "redirect_uri": OAUTH_REDIRECT_URI,
            "response_type": "code",
            "state": state
        }
        
        aha_url = f"{aha_auth_url}?" + "&".join(f"{k}={v}" for k, v in aha_params.items())
        return RedirectResponse(url=aha_url)
    
    @mcp.custom_route("/oauth/callback", methods=["GET", "OPTIONS"])
    async def oauth_callback_route(request):
        """OAuth callback endpoint"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        params = dict(request.query_params)
        code = params.get("code")
        state = params.get("state")
        error = params.get("error")
        
        if error:
            return HTMLResponse(
                f"<h1>OAuth Error</h1><p>{error}: {params.get('error_description', '')}</p>",
                status_code=400
            )
        
        if not code:
            return HTMLResponse(
                "<h1>Missing Code</h1><p>No authorization code received.</p>",
                status_code=400
            )
        
        # Exchange code for token with Aha!
        token_url = f"https://{AHA_DOMAIN}.aha.io/oauth/token"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    token_url,
                    data={
                        "grant_type": "authorization_code",
                        "code": code,
                        "client_id": OAUTH_CLIENT_ID,
                        "client_secret": OAUTH_CLIENT_SECRET,
                        "redirect_uri": OAUTH_REDIRECT_URI
                    }
                )
                response.raise_for_status()
                token_data = response.json()
                
                # Store the token (in production, use secure storage)
                access_token = token_data.get("access_token")
                if access_token:
                    # In a real implementation, associate with user
                    oauth_tokens["default"] = access_token
                    
                    # Get the original redirect URI if we have state
                    if state and state in oauth_states:
                        state_data = oauth_states.pop(state)
                        original_redirect = state_data.get("redirect_uri")
                        if original_redirect:
                            # Redirect back to original application with code
                            return RedirectResponse(
                                url=f"{original_redirect}?code={generate_token()}&state={state}"
                            )
                    
                    return HTMLResponse(
                        "<h1>Authorization Successful</h1><p>You can close this window.</p>"
                    )
                else:
                    return HTMLResponse(
                        "<h1>Token Error</h1><p>No access token received.</p>",
                        status_code=400
                    )
                    
            except Exception as e:
                logger.error(f"OAuth token exchange failed: {e}")
                return HTMLResponse(
                    f"<h1>Token Exchange Failed</h1><p>{str(e)}</p>",
                    status_code=500
                )
    
    @mcp.custom_route("/oauth/token", methods=["POST", "OPTIONS"])
    async def oauth_token_route(request):
        """OAuth token endpoint for MCP client"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        # For now, return a simple success response
        # In a real implementation, this would validate the code and return a proper token
        form_data = await request.form()
        code = form_data.get("code")
        
        if not code:
            return JSONResponse(
                {"error": "invalid_request", "error_description": "Missing code parameter"},
                status_code=400
            )
        
        # Generate a simple token for the MCP client
        # In production, this should be a proper JWT or validated token
        return JSONResponse({
            "access_token": generate_token(),
            "token_type": "Bearer",
            "expires_in": 3600,
            "scope": "read write"
        })
    
    @mcp.custom_route("/oauth/register", methods=["POST", "OPTIONS"])
    async def oauth_register_route(request):
        """Dynamic client registration endpoint (optional)"""
        if request.method == "OPTIONS":
            return JSONResponse({}, headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            })
        
        # For now, return not implemented
        return JSONResponse(
            {"error": "not_implemented", "error_description": "Dynamic registration not supported"},
            status_code=501
        )