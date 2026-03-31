# Aha! MCP Server

A Python MCP server that connects AI agents to Aha!'s product management platform. Uses 10 unified tools (consolidated from 78) following [Anthropic's best practices for writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).

### Use Cases

- **Product Management**: Browse and manage features, releases, epics, and initiatives.
- **Idea Management**: Create, evaluate, and promote product ideas.
- **Development Planning**: Manage requirements, track dependencies, analyze release capacity.
- **Team Collaboration**: Track assignments, tasks, and generate status reports.
- **Strategic Planning**: Access goals, key results, and strategic models.

## Prerequisites

- Python 3.10 or higher
- An Aha! account with API access
- API token or OAuth credentials

## Installation

### Using UV (Recommended)

```bash
uv pip install aha-mcp
# or add to your project
uv add aha-mcp
```

### Using pip

```bash
pip install aha-mcp
```

### From Source

```bash
git clone https://github.com/aha-develop/aha-mcp.git
cd aha-mcp
uv sync            # or: pip install -e ".[dev]"
```

### Docker

```bash
docker build -t aha-mcp .
docker run -e AHA_API_TOKEN=your-token -e AHA_DOMAIN=yoursubdomain aha-mcp
```

## Configuration

### Option 1: API Token (Recommended for Personal Use)

1. Get your API token from Aha! (Settings > Personal > API)
2. Create a `.env` file:
   ```env
   AHA_API_TOKEN=your-api-token
   AHA_DOMAIN=yoursubdomain
   ```

### Option 2: OAuth (For Team/Application Use)

1. Create an OAuth application in Aha! (Settings > Account > OAuth applications)
2. Create a `.env` file:
   ```env
   OAUTH_CLIENT_ID=your-oauth-client-id
   OAUTH_CLIENT_SECRET=your-oauth-client-secret
   AHA_DOMAIN=yoursubdomain
   ```

## Running the Server

```bash
# Run with UV (recommended)
uv run python aha_mcp.py

# Run directly (uses stdio transport by default)
python aha_mcp.py

# Run via installed entry point (after pip/uv install)
aha-mcp

# Or run with FastMCP CLI
fastmcp run aha_mcp.py
```

## IDE Integration

<details>
<summary><b>Claude Code</b></summary>

```bash
claude mcp add aha-mcp -- python aha_mcp.py
```

Set environment variables in your `.env` file or shell before running.
</details>

<details>
<summary><b>Claude Desktop</b></summary>

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha_mcp.py"],
      "env": {
        "AHA_API_TOKEN": "your-api-token",
        "AHA_DOMAIN": "yoursubdomain"
      }
    }
  }
}
```
</details>

<details>
<summary><b>VSCode / Cursor / Other IDEs</b></summary>

Add to your IDE's MCP configuration (e.g., `.vscode/settings.json`):

```json
{
  "mcp": {
    "servers": {
      "aha-mcp": {
        "command": "python",
        "args": ["/path/to/aha_mcp.py"],
        "env": {
          "AHA_API_TOKEN": "your-api-token",
          "AHA_DOMAIN": "yoursubdomain"
        }
      }
    }
  }
}
```
</details>

## Tools (10)

The server exposes 10 unified tools, each prefixed with `aha_`, consolidating 78 endpoint-specific tools into a clean interface. Every tool that accepts a record identifier supports **reference numbers** (`PROJ-123`), **names** (`"Q3 Planning"`), or **numeric IDs** (`"6789012345"`) interchangeably.

| Tool | Purpose | Annotations |
|------|---------|-------------|
| `aha_get` | Fetch any record by reference, name, or ID | read-only |
| `aha_search` | Search/list records with filters and pagination | read-only |
| `aha_create` | Create any record type | mutating |
| `aha_update` | Update any record (partial updates) | mutating |
| `aha_delete` | Delete any record | destructive |
| `aha_promote_idea` | Convert an idea to a feature | mutating |
| `aha_upload_attachment` | Attach a file to a record via URL | mutating |
| `aha_my_work` | Get all work assigned to a user | read-only |
| `aha_recent_activity` | Recent changes across the workspace | read-only |
| `aha_introspect` | Explore the Aha! GraphQL API schema | read-only |

<details>
<summary><b>Tool Details</b></summary>

### aha_get
Fetch any Aha! record. Auto-detects type from reference format.
- `identifier` (required): `"PROJ-123"`, `"PROJ-I-45"`, `"Q3 Planning"`, or `"6789012345"`
- `record_type` (optional): `"feature"`, `"idea"`, `"epic"`, `"release"`, etc.
- `response_format`: `"detailed"` (default) or `"concise"`
- `content_format`: `"markdown"` (default) or `"html"`

### aha_search
Search and list records with filters. Supports free-text search and structured listing.
- `query`: Free-text search string
- `record_type`: Filter by type (feature, idea, epic, release, project, etc.)
- `project`, `status`, `assignee`, `tags`: Additional filters
- `page`, `per_page`: Pagination (max 100 per page)
- `response_format`: `"concise"` (default) or `"detailed"`

### aha_create
Create any record type with common and type-specific fields.
- `record_type` (required): `"feature"`, `"idea"`, `"epic"`, `"task"`, etc.
- `name` (required): Record title
- `project`: Required for features, ideas, epics, releases
- `description`: Markdown (auto-converted to HTML for Aha!)
- `assignee`, `status`, `tags`, `parent`, `release`, `due_date`: Common fields
- `extra_fields`: Dict for type-specific fields

### aha_update
Update any record. Only provided fields are changed.
- `identifier` (required): Reference, name, or ID
- All other fields optional: `name`, `description`, `status`, `assignee`, `tags`, etc.

### aha_delete
Permanently delete a record.
- `identifier` (required): Reference, name, or ID

### aha_promote_idea
Convert an idea to a feature (workflow action).
- `idea` (required): Idea reference, name, or ID
- `target_project`, `target_release`: Optional targeting

### aha_upload_attachment
Attach a file to a record via URL.
- `record` (required): Record reference, name, or ID
- `file_url` (required): Public URL of the file

### aha_my_work
Get all work assigned to a user across features, epics, requirements, and tasks.
Uses `asyncio.gather()` for parallel API calls.
- `assignee`: User email or ID
- `response_format`: `"concise"` (default) or `"detailed"`

### aha_recent_activity
Get recently created/updated records grouped by type.
- `days`: Look-back period (default 7, max 30)
- `project`: Filter to a specific project
- `record_type`: Filter to a specific type

### aha_introspect
Explore the Aha! GraphQL API schema (cached with 5-min TTL).
- `query_type`: `"overview"`, `"type"`, or `"search"`
- `type_name`: Type to explore (when query_type="type")
- `search_term`: Search term for filtering
</details>

## Prompts (10)

Pre-defined prompts for common Aha! workflows:

- `analyze_feature_backlog` -- Backlog analysis for a project
- `create_feature_spec` -- Feature specification template
- `idea_evaluation` -- Evaluate and prioritize ideas
- `release_planning` -- Release capacity analysis
- `bug_triage_session` -- Bug triage with filtering
- `feature_dependencies_analysis` -- Dependency analysis
- `sprint_retrospective` -- Sprint retrospective
- `weekly_status_report` -- Status report generation
- `idea_to_feature_conversion` -- Idea-to-feature workflow
- `integration_checklist` -- Integration planning checklist

## Resources (4)

MCP resources for direct data access:

- `aha://releases/{status}` -- Releases filtered by status (active, all, parking-lot)
- `aha://ideas/{filter}` -- Ideas filtered by type (review, new, all)
- `aha://work/assigned/{user_email}` -- Work assigned to a user
- `aha://updates/recent/{days}` -- Recent updates across workspace

## Example Usage

```
"Get feature PROJ-123"
"Search for features about onboarding"
"Create a feature called 'Login Redesign' in project PROJ"
"Update PROJ-I-45 with tags ['priority', 'q3']"
"Show me all my assigned work"
"What changed in the last 7 days?"
"Promote idea PROJ-I-45 to a feature in release PROJ-R-1"
```

## Development

### Running Tests

```bash
# Run with UV (recommended)
uv run pytest test_tools.py -v

# Run directly
pytest test_tools.py -v

# Run a specific test
pytest test_tools.py -k "test_aha_get"
```

### Debug Mode

```bash
LOG_LEVEL=debug uv run python aha_mcp.py
# or
LOG_LEVEL=debug python aha_mcp.py
```

## Architecture

```
aha_mcp.py          Entry point -- creates FastMCP instance, registers all components
client.py           Shared httpx.AsyncClient with connection pooling, retry, auth
tools.py            10 unified tool functions with flexible identifier resolution
resolver.py         Identifier resolution (reference / name / ID -> record)
formatting.py       Bidirectional Markdown <-> HTML conversion
errors.py           MCP-native error hierarchy (AhaAuthError, AhaNotFoundError, etc.)
cache.py            TTL cache for static data (schema introspection, workflows)
prompts.py          10 MCP prompts for common workflows
resources.py        4 MCP resources for direct data access
oauth.py            OAuth 2.0 routes and discovery endpoints
utils.py            Legacy utilities (from the 78-tool era, retained for reference)
```

Key design decisions:
- **10 tools, not 78**: One router per CRUD verb instead of one tool per API endpoint
- **Flexible identifiers**: Every tool accepts references, names, or IDs interchangeably
- **`response_format` parameter**: Agents control verbosity (`"concise"` vs `"detailed"`)
- **Markdown <-> HTML**: Auto-converts between Markdown (for agents) and HTML (for Aha! API)
- **Tool annotations**: `readOnlyHint` / `destructiveHint` on every tool
- **Shared HTTP client**: Connection pooling, 30s timeout, retry on 429/503
- **Composite tools**: `aha_my_work` and `aha_recent_activity` use `asyncio.gather()`

## Troubleshooting

- **ModuleNotFoundError**: Run `uv sync` or `pip install -r requirements.txt`
- **Python version error**: Requires Python 3.10+ (`python --version`)
- **Authentication**: Verify API token and AHA_DOMAIN are set correctly
- **Invalid reference**: Use formats like `PROJ-123` (feature), `PROJ-I-45` (idea), `PROJ-E-1` (epic)

## License

MIT License -- see LICENSE file for details.
