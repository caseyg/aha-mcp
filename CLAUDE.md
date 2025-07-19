# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Build and Run
- `npm run build` - Compile TypeScript to JavaScript
- `npm run start` - Run the compiled server
- `npm run mcp-start` - Build and start in one command
- `npm run prepublishOnly` - Build before publishing to npm

### Transport Options
- **stdio (default)**: `npm run mcp-start`
  - For IDE integrations like Claude Code
- **SSE**: `TRANSPORT=sse npm run mcp-start` or `TRANSPORT=sse PORT=3000 npm run mcp-start`
  - For web applications and HTTP-based integrations
  - Endpoints available: `/sse` (connection), `/message` (messaging), `/health` (status)

### Development Requirements
- Node.js v20 or higher required
- TypeScript project targeting ES2020 with NodeNext modules
- No test framework configured - add tests if needed

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

This is an MCP (Model Context Protocol) server that integrates with Aha!'s GraphQL API. The codebase follows a clean, modular structure:

- **Entry point**: `src/index.ts` - Sets up MCP server, validates environment, configures GraphQL client
- **Tool handlers**: `src/handlers.ts` - Contains `Handlers` class with methods for each MCP tool
- **GraphQL queries**: `src/queries.ts` - All GraphQL query strings
- **Type definitions**: `src/types.ts` - TypeScript interfaces and validation regexes

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
12. `update_idea` - Updates existing idea properties
13. `delete_idea` - Deletes an idea
14. `promote_idea` - Promotes an idea to a feature, epic, or requirement
15. `introspection` - Performs GraphQL introspection to explore the API schema
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
- `TRANSPORT` - Transport type: stdio or sse (default: stdio)
- `PORT` - Port for SSE transport (default: 3000)

### Reference Number Formats
- Features: `/^[A-Z0-9]+-\d+$/` (e.g., DEVELOP-123)
- Requirements: `/^[A-Z0-9]+-\d+-\d+$/` (e.g., ADT-123-1)
- Pages: `/^[A-Z0-9]+-N-\d+$/` (e.g., ABC-N-213)
- Ideas: `/^[A-Z0-9]+-I-\d+$/` (e.g., ABC-I-123)

## Key Development Notes

- The project uses `@modelcontextprotocol/sdk` for MCP protocol implementation
- GraphQL requests use `graphql-request` library
- All errors should use appropriate MCP error codes (InvalidParams, InternalError)
- The server supports both stdio transport (for IDE integrations) and SSE transport (for web applications)
- TypeScript strict mode is enabled - maintain type safety
- Output is built to `build/` directory
- The package is published to npm as `aha-mcp`