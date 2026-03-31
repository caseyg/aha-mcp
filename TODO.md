# Aha! MCP Server -- TODO

## Completed in Rewrite (research/mcp-best-practices branch)

- [x] Consolidated 78 tools to 10 unified tools (aha_get, aha_search, aha_create, aha_update, aha_delete, aha_promote_idea, aha_upload_attachment, aha_my_work, aha_recent_activity, aha_introspect)
- [x] Flexible identifier resolution (reference, name, or ID) via resolver.py
- [x] Bidirectional Markdown <-> HTML conversion via formatting.py
- [x] MCP-native error hierarchy (errors.py: AhaAuthError, AhaNotFoundError, etc.)
- [x] Shared httpx.AsyncClient with connection pooling, timeout, retry (client.py)
- [x] Parameterized GraphQL queries (no f-string injection)
- [x] TTL cache for introspection queries (cache.py, @cached decorator)
- [x] Tool annotations (readOnlyHint, destructiveHint) on all 10 tools
- [x] response_format parameter (concise/detailed) on read tools
- [x] content_format parameter (markdown/html) for description handling
- [x] asyncio.gather() for composite tools (aha_my_work, aha_recent_activity)
- [x] Pagination cap (per_page max 100) with truncation hints
- [x] New entry point aha_mcp.py (replaces aha-mcp.py)
- [x] Comprehensive test suite for new tools (test_tools.py)
- [x] 10 MCP prompts for common workflows
- [x] 4 MCP resources (releases, ideas, assigned work, recent updates)
- [x] OAuth 2.0 support with discovery endpoints

## Completed Bug Fixes

- [x] **Fixed call signature mismatch**: resolver.py now calls `graphql(ctx, query, vars)` and `rest_api(ctx, method, endpoint)` matching client.py signatures.
- [x] **Fixed resources.py check_auth pattern**: Now uses try/except AhaAuthError instead of old return-value pattern.
- [x] **Fixed resources.py indentation bug**: `feature_stats` computation now runs for ALL releases, not just "active" ones.
- [x] **Fixed resources.py tags kwarg**: Removed unsupported `tags=` kwarg from resource registration (FastMCP 3.x).
- [x] **Fixed OAuth security**: HTML-escaped `client_id` and error params to prevent XSS, replaced `str(e)` with generic error message, added 10-minute state TTL with expiry check.
- [x] **Fixed OAuth shared client**: oauth.py now uses `get_client()` from client.py instead of creating its own httpx clients.
- [x] **Fixed f-string injection in aha_my_work**: Converted to parameterized $variables for GraphQL queries.
- [x] **Fixed f-string injection in aha_recent_activity**: Converted to parameterized $variables for GraphQL queries.
- [x] **Wired status/tags into aha_search**: `status` and `tags` parameters now included in GraphQL filter variables.
- [x] **Removed legacy files**: Deleted `aha-mcp.py`, `utils.py`, `test_aha_mcp.py`. Updated pytest.ini to discover only `test_tools.py`.

## P2: Feature Gaps (from simplified-tool-design.md)

- [x] **Name-based identifier resolution for aha_create**: The `project` and `release` params now accept names (resolved via GraphQL search).
- [x] **"me" / current user support in aha_my_work**: `assignee=None` or `"me"` now resolves to the authenticated user via `{ me { id } }` GraphQL query.
- [x] **Helpful not-found errors**: Resolver now does a fuzzy search on not-found and suggests similar records ("Did you mean: ...").

## P3: MCP Best Practices Still Missing

- [ ] **stdio transport documentation**: MCP best practices recommend stdio for local use. README should document both stdio and HTTP transport options.
- [x] **MCP-native error codes**: Tools now raise `fastmcp.exceptions.ToolError` instead of returning JSON error strings. FastMCP wraps these as proper MCP error responses with `isError=True`.
- [ ] **Resource subscriptions**: MCP spec recommends `notifications/resources/updated` for changing resources. Not implemented.
- [ ] **Progress notifications**: Long-running operations should send progress updates. Not implemented.
- [ ] **Output schemas**: MCP spec recommends `outputSchema` for structured tool responses. Not implemented.
- [ ] **listChanged notifications**: Should notify when available tools/resources change. Not implemented.

## P3: Distribution & Adoption

- [x] **Package as pip installable**: pyproject.toml with UV and pip support, console_scripts entry point.
- [x] **Dockerfile**: For containerized deployment.
- [x] **manifest.json**: Anthropic plugin format compatibility.
- [ ] **MCP Inspector testing**: Verify server works with the official MCP Inspector.

## P3: Test Coverage

- [ ] **Resources tests**: No tests for resources.py.
- [ ] **OAuth tests**: No tests for oauth.py endpoints.
- [ ] **Integration tests**: No tests that verify actual GraphQL query construction (current tests mock at the function level).
- [ ] **Error path tests**: Limited negative testing for validation failures.
- [ ] **Resolver tests**: No tests for resolver.py identifier resolution logic.
