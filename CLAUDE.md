# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Build and Run
- `npm run build` - Compile TypeScript to JavaScript
- `npm run start` - Run the compiled server
- `npm run mcp-start` - Build and start in one command
- `npm run prepublishOnly` - Build before publishing to npm

### Development Requirements
- Node.js v20 or higher required
- TypeScript project targeting ES2020 with NodeNext modules
- No test framework configured - add tests if needed

## Architecture

This is an MCP (Model Context Protocol) server that integrates with Aha!'s GraphQL API. The codebase follows a clean, modular structure:

- **Entry point**: `src/index.ts` - Sets up MCP server, validates environment, configures GraphQL client
- **Tool handlers**: `src/handlers.ts` - Contains `Handlers` class with methods for each MCP tool
- **GraphQL queries**: `src/queries.ts` - All GraphQL query strings
- **Type definitions**: `src/types.ts` - TypeScript interfaces and validation regexes

### MCP Tools Exposed
1. `get_record` - Fetches features (DEVELOP-123) or requirements (ADT-123-1)
2. `get_page` - Fetches pages (ABC-N-213) with optional parent info
3. `search_documents` - Searches Aha! documents by query and type
4. `create_feature` - Creates new features in a release
5. `update_feature` - Updates existing feature properties
6. `delete_feature` - Deletes a feature
7. `list_features` - Lists features with filtering options
8. `get_feature_details` - Gets comprehensive feature information
9. `introspection` - Performs GraphQL introspection to explore the API schema (may be disabled in production)

### Environment Variables
Required:
- `AHA_API_TOKEN` - Authentication token for Aha! API
- `AHA_DOMAIN` - Aha! domain (e.g., "yourcompany")

Optional:
- `LOG_LEVEL` - Logging level (default: info)
- `PORT` - Port for SSE transport (default: 3000)
- `TRANSPORT` - Transport type: stdio or sse (default: stdio)

### Reference Number Formats
- Features: `/^[A-Z0-9]+-\d+$/` (e.g., DEVELOP-123)
- Requirements: `/^[A-Z0-9]+-\d+-\d+$/` (e.g., ADT-123-1)
- Pages: `/^[A-Z0-9]+-N-\d+$/` (e.g., ABC-N-213)

## Key Development Notes

- The project uses `@modelcontextprotocol/sdk` for MCP protocol implementation
- GraphQL requests use `graphql-request` library
- All errors should use appropriate MCP error codes (InvalidParams, InternalError)
- The server primarily uses stdio transport for IDE integrations
- TypeScript strict mode is enabled - maintain type safety
- Output is built to `build/` directory
- The package is published to npm as `aha-mcp`