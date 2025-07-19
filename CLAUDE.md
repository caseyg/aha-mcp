# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python implementation of an MCP (Model Context Protocol) server for Aha! using FastMCP 2.0. It aims to provide a comprehensive interface to Aha!'s GraphQL and REST APIs with additional features beyond the original implementation.

This implementation is based on the original TypeScript MCP server by Aha! but has been rewritten in Python using the FastMCP framework for better maintainability and enhanced functionality.

## Commands

### Build and Run
- `pip install -r requirements.txt` - Install Python dependencies
- `python aha-mcp.py` - Run the server directly
- `fastmcp run aha-mcp.py --transport http` - Run with FastMCP CLI

### Testing
- `pytest test_aha_mcp.py` - Run test suite
- `pytest test_aha_mcp.py -v` - Run tests with verbose output
- `pytest test_aha_mcp.py -k "test_name"` - Run specific test
- `pytest test_aha_mcp.py --cov=aha-mcp` - Run with coverage (if coverage installed)

### Transport Options
- **HTTP (only)**: `fastmcp run aha-mcp.py --transport http`
  - Runs on port 8000 by default
  - Provides OAuth discovery endpoints when OAuth credentials are configured
  - Note: SSE transport not available in Python implementation

### Development Requirements
- Python 3.10 or higher required
- FastMCP 2.0 framework
- Dependencies: `fastmcp>=2.0.0`, `httpx`, `pytest`, `pytest-asyncio`, `python-dotenv`
- Test framework: pytest with async support

## Authentication Setup

The server supports two authentication methods:

### Option 1: API Token (Default)
1. Get your API token from Aha! (Settings → Personal → API)
2. Set environment variables:
   ```bash
   export AHA_API_TOKEN="your-api-token"
   export AHA_DOMAIN="yourcompany"
   ```

### Option 2: OAuth2 (MCP-compliant)
1. Register an OAuth application in Aha!:
   - Go to Settings → Account → OAuth applications
   - Create a new application
   - Set redirect URL to match OAUTH_REDIRECT_URI (default: http://localhost:3000/oauth/callback)
2. Set environment variables:
   ```bash
   export OAUTH_CLIENT_ID="your-client-id"
   export OAUTH_CLIENT_SECRET="your-client-secret"
   export OAUTH_REDIRECT_URI="http://localhost:3000/oauth/callback"  # optional
   ```
3. When using OAuth, you'll need to authenticate first:
   - In OAuth mode, use the `auth_login` tool to get an authorization URL
   - Open the URL in your browser and authorize the application
   - The server will handle the callback and store your token

#### OAuth Implementation Details
- **PKCE Support**: Uses S256 code challenge method for enhanced security
- **Resource Indicators**: Implements RFC 8707 for token audience binding
- **Protected Resource Metadata**: Exposes `/.well-known/oauth-protected-resource` endpoint
- **WWW-Authenticate Headers**: Returns proper 401 responses with resource metadata
- **Token Validation**: Validates tokens are intended for this specific MCP server

## Architecture

### Python Implementation (aha-mcp.py)
- **Single file**: `aha-mcp.py` - Complete implementation using FastMCP 2.0
- **Test file**: `test_aha_mcp.py` - Comprehensive pytest test suite
- **Framework**: FastMCP 2.0 provides MCP protocol handling and OAuth discovery
- **API Integration**: Hybrid approach using GraphQL for most operations, REST API for unsupported features
- **Authentication**: Centralized auth handling with support for both API tokens and OAuth2
- **Error Handling**: Consistent error messages with proper MCP error codes

### Key Architectural Decisions
1. **FastMCP Framework**: Simplifies MCP protocol implementation significantly
2. **Single File Design**: All server logic in one file for easier maintenance
3. **Stateless Operation**: No persistent storage, suitable for serverless deployment
4. **Hybrid API Approach**: GraphQL primary, REST fallback for missing operations
5. **Comprehensive Testing**: Full test coverage with mocked GraphQL responses

### MCP Tools Exposed

1. `get_record` - Fetches features (DEVELOP-123), requirements (ADT-123-1), or ideas (ABC-I-123)
2. `get_page` - Fetches pages (ABC-N-213) with optional parent info
3. `search_documents` - Searches Aha! documents by query and type
4. `create_feature` - Creates new features in a release
5. `update_feature` - Updates existing feature properties
6. `delete_feature` - Deletes a feature
7. `list_features` - Lists features with filtering options
8. `get_feature_details` - Gets comprehensive feature information
9. `get_idea` - Fetches an idea by ID or reference (ABC-I-123)
10. `list_ideas` - Lists ideas for a project with filtering options
11. `create_idea` - Creates new ideas in a project
12. `update_idea` - Updates existing idea properties (limited by GraphQL API)
13. `delete_idea` - Deletes an idea (uses REST API)
14. `introspection` - Performs GraphQL introspection to explore the API schema
    - Supports generic type exploration with `queryType: "type"` and `typeName: "ModelName"`
    - Can search for specific queries/mutations with `searchTerm`
    - Examples: explore "Idea" type, search for "create" mutations, find "idea" queries

### Environment Variables

#### For API Token Authentication (Option 1)
Required:
- `AHA_API_TOKEN` - Authentication token for Aha! API
- `AHA_DOMAIN` - Aha! domain (e.g., "yourcompany")

#### For OAuth2 Authentication (Option 2)
Required:
- `OAUTH_CLIENT_ID` - OAuth application client ID
- `OAUTH_CLIENT_SECRET` - OAuth application client secret

Optional:
- `OAUTH_REDIRECT_URI` - OAuth callback URL (default: http://localhost:3000/oauth/callback)
- `AHA_DOMAIN` - Default Aha! domain for OAuth (optional)

#### General Configuration
Optional:
- `LOG_LEVEL` - Logging level (default: info)
- `PORT` - Port for HTTP transport (default: 8000)

### Reference Number Formats
- Features: `/^[A-Z0-9]+-\d+$/` (e.g., DEVELOP-123)
- Requirements: `/^[A-Z0-9]+-\d+-\d+$/` (e.g., ADT-123-1)
- Pages: `/^[A-Z0-9]+-N-\d+$/` (e.g., ABC-N-213)
- Ideas: `/^[A-Z0-9]+-I-\d+$/` (e.g., ABC-I-123)

## Key Development Notes

- Uses FastMCP 2.0 framework for simplified MCP implementation
- Async/await pattern throughout with `httpx` for HTTP requests
- Centralized error handling with RuntimeError for GraphQL errors
- Single-file architecture reduces complexity
- Tests use pytest with mocked GraphQL responses
- OAuth token mapping stored in-memory (stateless design)
- All errors use appropriate MCP error codes (InvalidParams, InternalError)
- GraphQL requests handled via centralized `graphql()` function
- REST API used sparingly for operations not supported by GraphQL

### Documentation Structure
- `README.md` - User-facing documentation with setup instructions
- `TODO.md` - Implementation roadmap and API comparison table
- `docs/` - Reference documentation including:
  - `aha-rest-api/` - REST API endpoint documentation
  - `fastmcp/` - FastMCP framework documentation

## Known Limitations and Future Work

### GraphQL API Limitations
Some operations are not supported via GraphQL and require REST API:
- **Idea scores and tags**: Updates only available via REST
- **File attachments**: Upload/management only via REST
- **User management**: CRUD operations only via REST
- **Comment updates/deletes**: Only creation available in GraphQL

### Planned Enhancements (See TODO.md for details)
1. **REST API Integration**: Add REST client for unsupported GraphQL operations
2. **MCP Prompts**: Add predefined prompts for common workflows
3. **MCP Resources**: Expose Aha! data as resources (releases, backlog, etc.)
4. **Additional Endpoints**: Releases, epics, requirements, users, workflows, custom fields

Refer to TODO.md for the comprehensive GraphQL vs REST API comparison table and implementation priorities.