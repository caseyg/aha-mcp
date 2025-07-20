# Aha! MCP Server

A Python implementation of a Model Context Protocol (MCP) server for accessing Aha! records using FastMCP 2.0.

This implementation is based on the [original TypeScript MCP server by Aha!](https://github.com/aha-develop/aha-mcp) but has been rewritten in Python using the FastMCP framework, providing enhanced functionality including OAuth support, testing, and additional MCP tools.

## Project Structure

The codebase is organized into modular files for better maintainability:

- `aha_mcp.py` - Main entry point that sets up the FastMCP server
- `client.py` - GraphQL client and authentication handling
- `tools.py` - All MCP tools for interacting with Aha! API
- `prompts.py` - Pre-defined MCP prompts for common workflows
- `oauth.py` - OAuth endpoints and discovery routes
- `test_aha_mcp.py` - Comprehensive test suite

## Quick Start

### Prerequisites

- Python 3.10 or higher
- An Aha! account with API access

### Installation

```bash
# Clone the repository
git clone https://github.com/aha-develop/aha-mcp.git
cd aha-mcp

# Install Python dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file with your Aha! credentials:

**For API Token:**
```env
AHA_API_TOKEN=your-api-token
AHA_DOMAIN=yoursubdomain
```

**For OAuth:**
```env
OAUTH_CLIENT_ID=your-oauth-client-id
OAUTH_CLIENT_SECRET=your-oauth-client-secret
AHA_DOMAIN=yoursubdomain
```

### Running

```bash
# Run the server (defaults to HTTP transport)
fastmcp run aha-mcp.py --transport http

# Or run directly
python aha-mcp.py
```

The server runs on HTTP transport at `http://localhost:8000`. When OAuth credentials are configured, it provides OAuth discovery endpoints for MCP-compliant authentication.

## Getting Your Aha! Credentials

### API Token
1. Log in to your Aha! account
2. Visit Settings → Personal → API
3. Generate a new token

### OAuth Credentials
1. Go to Settings → Account → OAuth applications
2. Create a new application
3. Use the Client ID and Client Secret

## IDE Integration

For security reasons, we recommend using your preferred secure method for managing environment variables rather than storing API tokens directly in editor configurations.

### VSCode

The instructions below were copied from the instructions [found here](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server).

Add this to your `.vscode/settings.json`, using your preferred method to securely provide the environment variables:

```json
{
  "mcp": {
    "servers": {
      "aha-mcp": {
        "command": "python",
        "args": ["/path/to/aha-mcp.py"]
        // Environment variables should be provided through your preferred secure method
      }
    }
  }
}
```

### Cursor

1. Go to Cursor Settings > MCP
2. Click + Add new Global MCP Server
3. Add a configuration similar to:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"]
      // Environment variables should be provided through your preferred secure method
    }
  }
}
```

### Cline

Add a configuration to your `cline_mcp_settings.json` via Cline MCP Server settings:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"]
      // Environment variables should be provided through your preferred secure method
    }
  }
}
```

### RooCode

Open the MCP settings by either:

- Clicking "Edit MCP Settings" in RooCode settings, or
- Using the "RooCode: Open MCP Config" command in VS Code's command palette

Then add:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"]
      // Environment variables should be provided through your preferred secure method
    }
  }
}
```

### Claude Desktop

Add a configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"]
      // Environment variables should be provided through your preferred secure method
    }
  }
}
```

## Available MCP Tools

### 1. get_record

Retrieves an Aha! feature or requirement by reference number.

**Parameters:**

- `reference` (required): Reference number of the feature or requirement (e.g., "DEVELOP-123")

**Example:**

```json
{
  "reference": "DEVELOP-123"
}
```

**Response:**

```json
{
  "reference_num": "DEVELOP-123",
  "name": "Feature name",
  "description": "Feature description",
  "workflow_status": {
    "name": "In development",
    "id": "123456"
  }
}
```

### 2. get_page

Gets an Aha! page by reference number.

**Parameters:**

- `reference` (required): Reference number of the page (e.g., "ABC-N-213")
- `includeParent` (optional): Include parent page information. Defaults to false.

**Example:**

```json
{
  "reference": "ABC-N-213",
  "includeParent": true
}
```

**Response:**

```json
{
  "reference_num": "ABC-N-213",
  "name": "Page title",
  "body": "Page content",
  "parent": {
    "reference_num": "ABC-N-200",
    "name": "Parent page"
  }
}
```

### 3. search_documents

Searches for Aha! documents.

**Parameters:**

- `query` (required): Search query string
- `searchableType` (optional): Type of document to search for (e.g., "Page"). Defaults to "Page"

**Example:**

```json
{
  "query": "product roadmap",
  "searchableType": "Page"
}
```

**Response:**

```json
{
  "results": [
    {
      "reference_num": "ABC-N-123",
      "name": "Product Roadmap 2025",
      "type": "Page",
      "url": "https://company.aha.io/pages/ABC-N-123"
    }
  ],
  "total_results": 1
}
```

### 4. create_feature

Creates a new feature in Aha!

**Parameters:**

- `releaseId` (required): ID or reference number of the release
- `name` (required): Name of the feature
- `description` (optional): Description of the feature (supports markdown)
- `assignedToUserId` (optional): ID of the user to assign the feature to
- `tags` (optional): Array of tags to add to the feature
- `workflowStatusId` (optional): ID of the workflow status
- `epicId` (optional): ID or reference number of the epic
- `teamId` (optional): ID of the team to assign the feature to

**Example:**

```json
{
  "releaseId": "PRJ1-R-1",
  "name": "New Authentication System",
  "description": "Implement OAuth 2.0 authentication",
  "tags": ["security", "backend"]
}
```

### 5. update_feature

Updates an existing feature in Aha!

**Parameters:**

- `id` (required): ID or reference number of the feature
- `name` (optional): New name for the feature
- `description` (optional): New description for the feature (supports markdown)
- `workflowStatusId` (optional): ID of the new workflow status
- `assignedToUserId` (optional): ID of the user to reassign the feature to
- `tags` (optional): New tags for the feature

**Example:**

```json
{
  "id": "DEVELOP-123",
  "name": "Updated Feature Name",
  "workflowStatusId": "123456"
}
```

### 6. delete_feature

Deletes a feature from Aha!

**Parameters:**

- `id` (required): ID or reference number of the feature to delete

**Example:**

```json
{
  "id": "DEVELOP-123"
}
```

### 7. list_features

Lists features in Aha! with optional filters

**Parameters:**

- `releaseId` (optional): Filter by release ID or reference
- `epicId` (optional): Filter by epic ID or reference
- `productId` (optional): Filter by product ID or reference
- `goalId` (optional): Filter by goal ID or reference
- `initiativeId` (optional): Filter by initiative ID or reference
- `page` (optional): Page number for pagination
- `perPage` (optional): Number of items per page

**Example:**

```json
{
  "releaseId": "PRJ1-R-1",
  "page": 1,
  "perPage": 20
}
```

### 8. get_feature_details

Gets detailed information about a specific feature

**Parameters:**

- `id` (required): ID or reference number of the feature

**Example:**

```json
{
  "id": "DEVELOP-123"
}
```

**Response includes:** Full feature details including workflow status, release, epic, assigned user, tags, dates, progress, goals, watchers, and custom fields.

### 9. get_idea

Fetches an idea by ID or reference

**Parameters:**

- `id` (required): ID or reference number of the idea (e.g., "ABC-I-123")

**Example:**

```json
{
  "id": "ABC-I-123"
}
```

### 10. list_ideas

Lists ideas for a project with optional filters

**Parameters:**

- `projectId` (required): ID or reference of the project
- `assignedToUserId` (optional): Filter by assigned user ID
- `promoted` (optional): Filter by promotion status (true/false)
- `visibility` (optional): Filter by visibility
- `page` (optional): Page number for pagination
- `perPage` (optional): Number of items per page

**Example:**

```json
{
  "projectId": "PRJ1",
  "promoted": false,
  "page": 1,
  "perPage": 20
}
```

### 11. create_idea

Creates a new idea in a project

**Parameters:**

- `projectId` (required): ID or reference of the project
- `name` (required): Name of the idea
- `assignedToUserId` (optional): ID of the user to assign the idea to
- `workflowStatusId` (optional): ID of the workflow status

**Example:**

```json
{
  "projectId": "PRJ1",
  "name": "New Dashboard Feature",
  "assignedToUserId": "user123"
}
```

### 12. update_idea

Updates an existing idea

**Parameters:**

- `id` (required): ID or reference number of the idea
- `name` (optional): New name for the idea
- `assignedToUserId` (optional): ID of the user to reassign the idea to
- `workflowStatusId` (optional): ID of the new workflow status

**Note:** Due to GraphQL limitations, some fields like score, tags, description, and visibility cannot be updated through this tool.

**Example:**

```json
{
  "id": "ABC-I-123",
  "name": "Updated Idea Name",
  "workflowStatusId": "status456"
}
```

### 13. delete_idea

Deletes an idea from Aha!

**Parameters:**

- `id` (required): ID or reference number of the idea to delete

**Example:**

```json
{
  "id": "ABC-I-123"
}
```

### 14. introspection

Performs GraphQL introspection to explore the Aha! API schema with size-limited responses.

**Parameters:**

- `queryType` (optional): Type of introspection query to run
  - `"list-types"` (default): List available types (excludes internal __ types)
  - `"simple"`: Same as list-types
  - `"query"`: List available queries
  - `"mutation"`: List available mutations
  - `"type"`: Explore a specific type (requires `typeName`)
  - `"search-queries"`: Search for queries by name/description
  - `"search-mutations"`: Search for mutations by name/description
- `typeName` (optional): Name of the type to introspect (required when queryType is "type")
  - Examples: "Idea", "Feature", "Project", "User", "Release", "Epic"
- `searchTerm` (optional): Search term for filtering results
- `maxResults` (optional): Maximum number of results to return (default: 50)

**Examples:**

```json
// List all available types
{
  "queryType": "list-types"
}

// Search for idea-related types
{
  "queryType": "list-types",
  "searchTerm": "idea"
}

// Explore the Idea type structure
{
  "queryType": "type",
  "typeName": "Idea"
}

// Search for queries related to ideas
{
  "queryType": "search-queries",
  "searchTerm": "idea",
  "maxResults": 20
}

// Find mutations for creating things
{
  "queryType": "search-mutations",
  "searchTerm": "create",
  "maxResults": 30
}
```

**Note:** Full schema introspection is disabled due to response size limits. Use list-types first to discover available types, then explore specific types individually.

**Pagination:** When using list-types, query, or mutation query types, the response includes pagination metadata:
```json
{
  "data": { /* actual results */ },
  "pagination": {
    "totalCount": 150,      // Total items before filtering
    "filteredCount": 45,    // Items after search filter
    "returnedCount": 20,    // Items in this response
    "hasMore": true,        // More results available
    "maxResults": 20        // Current limit
  }
}
```

## Available MCP Prompts

The server provides several pre-defined prompts to help with common Aha! workflows:

### 1. analyze_feature_backlog
Generates a comprehensive prompt for analyzing your feature backlog.

**Parameters:**
- `project_id` (required): The project ID to analyze
- `release_id` (optional): Specific release to focus on

### 2. create_feature_spec
Helps create a detailed feature specification ready for Aha!

**Parameters:**
- `feature_name` (required): Name of the feature
- `release_id` (required): Target release ID
- `user_story` (required): User story description
- `acceptance_criteria` (optional): Acceptance criteria

### 3. idea_evaluation
Evaluates ideas in a project based on specified criteria.

**Parameters:**
- `project_id` (required): Project containing ideas
- `evaluation_criteria` (optional): Criteria to evaluate (default: "value, effort, risk")

### 4. release_planning
Assists with release planning and capacity analysis.

**Parameters:**
- `release_id` (required): Release to plan
- `team_capacity` (optional): Team capacity information
- `focus_areas` (optional): Areas to focus on

### 5. bug_triage_session
Guides a bug triage session with severity and age filtering.

**Parameters:**
- `tag` (optional): Filter bugs by tag
- `severity_threshold` (optional): Minimum severity (default: "high")
- `age_days` (optional): Minimum age in days (default: 7)

### 6. feature_dependencies_analysis
Analyzes upstream and downstream dependencies for a feature.

**Parameters:**
- `feature_reference` (required): Feature to analyze
- `check_upstream` (optional): Check what this depends on (default: true)
- `check_downstream` (optional): Check what depends on this (default: true)

### 7. sprint_retrospective
Generates a comprehensive sprint retrospective analysis.

**Parameters:**
- `sprint_name` (required): Name of the sprint
- `team_name` (optional): Specific team to focus on

### 8. weekly_status_report
Creates a structured weekly status report.

**Parameters:**
- `project_id` (required): Project to report on
- `week_ending` (required): Week ending date
- `include_metrics` (optional): Include metrics section (default: true)

### 9. idea_to_feature_conversion
Guides the conversion of an idea into a feature.

**Parameters:**
- `idea_reference` (required): Idea to convert
- `target_release` (required): Target release for the feature

### 10. integration_checklist
Generates a comprehensive integration checklist.

**Parameters:**
- `feature_reference` (required): Feature requiring integration
- `integration_type` (optional): Type of integration (default: "API")

## Example Queries

- "Get feature DEVELOP-123"
- "Fetch the product roadmap page ABC-N-213"
- "Search for pages about launch planning"
- "Get requirement ADT-123-1"
- "Find all pages mentioning Q2 goals"
- "Create a new feature for the Q1 release"
- "Update the status of feature DEVELOP-456"
- "List all ideas in project PRJ1"
- "Delete idea ABC-I-789"

## Configuration Options

### Environment Variables

| Variable        | Description                                          | Required |
| --------------- | ---------------------------------------------------- | -------- |
| `AHA_DOMAIN`    | Your Aha! subdomain (e.g., "yourcompany")          | Yes      |
| `AHA_API_TOKEN` | Your Aha! API token                                | Yes*     |
| `OAUTH_CLIENT_ID` | OAuth client ID                                   | Yes*     |
| `OAUTH_CLIENT_SECRET` | OAuth client secret                           | Yes*     |
| `OAUTH_REDIRECT_URI` | OAuth callback URL                             | No       |
| `LOG_LEVEL`     | Logging level (debug, info, warn, error)           | No       |
| `PORT`          | Port for HTTP transport                             | No       |

*Either API token OR OAuth credentials are required

## Development

### Running Tests

```bash
# Run all tests
pytest test_aha_mcp.py

# Run with verbose output
pytest test_aha_mcp.py -v

# Run specific test
pytest test_aha_mcp.py -k "test_name"

# Run with coverage
pytest test_aha_mcp.py --cov=aha-mcp
```

### Debug Mode

```bash
# Run with debug logging
LOG_LEVEL=debug python aha-mcp.py
```

## Troubleshooting

### Common Issues

#### Authentication Errors
- Verify your API token is correct and properly set in your environment
- For OAuth, ensure both CLIENT_ID and CLIENT_SECRET are set
- Confirm you're using the correct Aha! domain (subdomain only, not full URL)

#### Python-Specific Issues
- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **Python version**: Requires Python 3.10+ (check with `python --version`)
- **OAuth discovery errors**: The server provides OAuth discovery endpoints when OAuth credentials are configured
- **Connection refused**: Make sure to use `--transport http` when running with fastmcp

#### General Issues
- **Connection refused**: Check your network and Aha! domain
- **Permission denied**: Verify your API token/OAuth app has necessary permissions
- **Invalid references**: Use correct format (e.g., PROJ-123, ABC-I-456)

## Implementation Details

This Python implementation:
- Uses FastMCP 2.0 for simplified MCP protocol handling
- Implements both API token and OAuth authentication
- Provides 14 MCP tools for interacting with Aha!
- Uses GraphQL for most operations with REST API fallback
- Includes test coverage
- Maintains stateless operation suitable for serverless deployment

### Why Python?

This Python implementation offers several advantages:
- Leverages FastMCP 2.0 for simplified MCP protocol handling
- Provides OAuth support with discovery endpoints
- Includes extensive test coverage
- Offers additional tools and functionality
- Simplifies setup and deployment
- Makes the codebase more maintainable

## License

MIT License - see LICENSE file for details.