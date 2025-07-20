"""Aha! MCP Server - Main entry point."""

import os
import logging
from dotenv import load_dotenv
from fastmcp import FastMCP

# Import modules
from client import oauth_tokens
from tools import register_tools
from prompts import register_prompts
from resources import register_resources
from oauth import register_oauth_routes

# Load environment
load_dotenv()

# Configure logging
log_level = os.getenv("LOG_LEVEL", "info").upper()
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger(__name__)

# Create FastMCP instance
mcp = FastMCP(
    name="aha-mcp",
    version="2.0.0"
)

# Register all components
register_tools(mcp)
register_prompts(mcp)
register_oauth_routes(mcp, oauth_tokens)

# Import resource functions
from resources import releases_by_status, ideas_by_filter, my_assigned_work, recent_updates

# Define resources using decorator pattern like in the docs
@mcp.resource("aha://releases/{status}")
async def get_releases(status: str) -> dict:
    """Get releases filtered by status (active, all, parking-lot)."""
    return await releases_by_status(status)

@mcp.resource("aha://ideas/{filter}")  
async def get_ideas(filter: str) -> dict:
    """Get ideas filtered by type (review, new, all)."""
    return await ideas_by_filter(filter)

@mcp.resource("aha://work/{user_email}")
async def get_assigned_work(user_email: str) -> dict:
    """Get all work assigned to a specific user email."""
    return await my_assigned_work(user_email)

@mcp.resource("aha://updates/{days}")
async def get_recent_updates(days: str) -> dict:
    """Get recent updates across the workspace (default: 7 days)."""
    return await recent_updates(days)

# Export for running
__all__ = ['mcp']

if __name__ == "__main__":
    # For direct execution
    mcp.run()