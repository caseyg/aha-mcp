# aha-mcp

![License](https://img.shields.io/github/license/your-username/aha-mcp)
![npm version](https://img.shields.io/npm/v/aha-api-server)
![npm downloads](https://img.shields.io/npm/dm/aha-api-server)

Model Context Protocol (MCP) server for accessing Aha! records through the MCP. This integration enables seamless interaction with Aha! features, requirements, and pages directly through the Model Context Protocol.

## Setup Guide

### 1. Authentication Setup

1. Log in to your Aha! account at `<yourcompany>.aha.io`
2. Visit [secure.aha.io/settings/api_keys](https://secure.aha.io/settings/api_keys)
3. Click "Create new API key"
4. Copy the token immediately (it won't be shown again)

For more details about authentication and API usage, see the [Aha! API documentation](https://www.aha.io/api).

### 2. Installation

Choose one of these installation methods:

```bash
# Using npm (recommended)
npm install aha-api-server

# Using git
git clone https://github.com/aha-develop/aha-mcp.git
cd aha-mcp
npm install
```

### 3. Configuration and Usage

You can configure the MCP server using environment variables or command-line arguments.

#### Using Environment Variables

1. Create a `.env` file in the root directory:
```bash
touch .env
```

2. Add your configuration:
```plaintext
AHA_API_TOKEN=your_api_token_here
AHA_DOMAIN=yourcompany.aha.io
```

#### Starting the Server

```bash
npm run mcp-start
```

<details>
<summary>Optional Configuration</summary>

The following environment variables can be used to customize the server behavior:

| Variable | Description | Default |
|----------|-------------|---------|
| `AHA_API_TOKEN` | Your Aha! API token | Required |
| `AHA_DOMAIN` | Your Aha! domain (e.g., yourcompany.aha.io) | Required |
| `LOG_LEVEL` | Logging level (debug, info, warn, error) | info |
| `PORT` | Port for SSE transport | 3000 |
| `TRANSPORT` | Transport type (stdio or sse) | stdio |

</details>

## IDE Integration

### VSCode Setup

Add this to your `.vscode/settings.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "npm",
      "args": ["run", "mcp-start"],
      "cwd": "/path/to/aha-mcp"
    }
  }
}
```

## Available MCP Tools

The server provides the following tools:

### get_record
Retrieve an Aha! feature or requirement by reference number.
```json
{
  "reference": "DEVELOP-123"
}
```

### get_page
Get an Aha! page by reference number.
```json
{
  "reference": "ABC-N-213",
  "includeParent": false
}
```

### search_documents
Search for Aha! documents.
```json
{
  "query": "search term",
  "searchableType": "Page"
}
```

## Error Handling

The server will respond with appropriate error messages if:
- The API token is missing or invalid
- The requested record is not found
- The API request fails
- Invalid parameters are provided to the tools

<details>
<summary>Troubleshooting</summary>

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
</details>
