"""Aha! MCP Server — simplified 10-tool implementation."""
import os
import logging
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

log_level = os.getenv("LOG_LEVEL", "info").upper()
logging.basicConfig(level=getattr(logging, log_level))

mcp = FastMCP(name="aha-mcp", version="3.0.0")

# Register tools (the 10 simplified tools)
from tools import register_tools
register_tools(mcp)

# Register prompts (unchanged)
from prompts import register_prompts
register_prompts(mcp)

# Register resources
from resources import register_resources
register_resources(mcp)

# Register OAuth routes
from client import oauth_tokens
from oauth import register_oauth_routes
register_oauth_routes(mcp, oauth_tokens)

if __name__ == "__main__":
    mcp.run()
