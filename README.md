# aha-mcp

Model Context Protocol (MCP) server for accessing Aha! records through the MCP. This integration enables seamless interaction with Aha! features, requirements, and pages directly through the Model Context Protocol.

## Prerequisites

- Node.js v20 or higher
- npm (usually comes with Node.js)
- An Aha! account with API access

## Installation

### Using npx

```bash
npx -y aha-mcp@latest
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/aha-develop/aha-mcp.git
cd aha-mcp

# Install dependencies
npm install

# Run the server
npm run mcp-start
```

## Authentication Setup

1. Log in to your Aha! account at `<yourcompany>.aha.io`
2. Visit [secure.aha.io/settings/api_keys](https://secure.aha.io/settings/api_keys)
3. Click "Create new API key"
4. Copy the token immediately (it won't be shown again)

For more details about authentication and API usage, see the [Aha! API documentation](https://www.aha.io/api).

## IDE Integration

### VSCode

Add this to your `.vscode/settings.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "npx",
      "args": ["-y", "aha-mcp"],
      "env": {
        "AHA_API_TOKEN": "your_api_token_here",
        "AHA_DOMAIN": "yourcompany.aha.io"
      }
    }
  }
}
```

### Cursor

1. Go to Cursor Settings > MCP
2. Click + Add new Global MCP Server
3. Add the following configuration:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "npx",
      "args": ["-y", "aha-mcp"],
      "env": {
        "AHA_API_TOKEN": "your_api_token_here",
        "AHA_DOMAIN": "yourcompany.aha.io"
      }
    }
  }
}
```

### Cline

Add the following to your `cline_mcp_settings.json` via Cline MCP Server settings:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "npx",
      "args": ["-y", "aha-mcp"],
      "env": {
        "AHA_API_TOKEN": "your_api_token_here",
        "AHA_DOMAIN": "yourcompany.aha.io"
      }
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
      "command": "npx",
      "args": ["-y", "aha-mcp"],
      "env": {
        "AHA_API_TOKEN": "your_api_token_here",
        "AHA_DOMAIN": "yourcompany.aha.io"
      }
    }
  }
}
```

### Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "npx",
      "args": ["-y", "aha-mcp"],
      "env": {
        "AHA_API_TOKEN": "your_api_token_here",
        "AHA_DOMAIN": "yourcompany.aha.io"
      }
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

## Example Queries

- "Get feature DEVELOP-123"
- "Fetch the product roadmap page ABC-N-213"
- "Search for pages about launch planning"
- "Get requirement ADT-123-1"
- "Find all pages mentioning Q2 goals"

## Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `AHA_API_TOKEN` | Your Aha! API token | Required |
| `AHA_DOMAIN` | Your Aha! domain (e.g., yourcompany.aha.io) | Required |
| `LOG_LEVEL` | Logging level (debug, info, warn, error) | info |
| `PORT` | Port for SSE transport | 3000 |
| `TRANSPORT` | Transport type (stdio or sse) | stdio |

## Troubleshooting

<details>
<summary>Common Issues</summary>

1. Authentication errors:
   - Verify your API token is correct in the `.env` file
   - Ensure the token has the necessary permissions in Aha!
   - Confirm you're using the correct Aha! domain

2. Server won't start:
   - Ensure all dependencies are installed
   - Check the Node.js version is v20 or higher
   - Verify the TypeScript compilation succeeds

3. Connection issues:
   - Check your network connection
   - Verify your Aha! domain is accessible
   - Ensure your API token has not expired

4. API Request failures:
   - Check the reference numbers are correct
   - Verify the searchable type is valid
   - Ensure you have permissions to access the requested resources
</details>
