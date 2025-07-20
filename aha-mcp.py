"""Aha! MCP Server - Main entry point."""

import os
import logging
from dotenv import load_dotenv
from fastmcp import FastMCP

# Import modules
from client import oauth_tokens
from tools import register_tools
from prompts import register_prompts
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

# Export for running
__all__ = ['mcp']

if __name__ == "__main__":
    # For direct execution
    mcp.run()