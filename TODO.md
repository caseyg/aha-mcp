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

## P0: Critical Bugs to Fix

- [ ] **Call signature mismatch**: tools.py/resources.py/utils.py call `graphql(ctx, query, vars)` but client.py defines `graphql(query, vars, ctx)`. Same for rest_api. Tests pass only because mocks bypass the real client.
- [ ] **format_response_field type error**: `tools.py:_format_output()` passes dict/list to `formatting.py:format_response_field()` which expects str. Needs recursive field conversion.
- [ ] **resources.py check_auth pattern**: Still uses old pattern (expects return value) but new client.py raises exceptions. Also has indentation bug where feature_stats only computed for "active" releases.
- [ ] **resources.py bare except**: `ideas_by_filter` line 256 has bare `except:` that swallows KeyboardInterrupt.
- [ ] **OAuth security**: XSS in error page (oauth.py reflects client_id into HTML), no state validation in callback, no token expiry on oauth_states.

## P1: Code Quality

- [ ] **Remove legacy files**: Delete or archive `aha-mcp.py`, `test_aha_mcp.py`, `run_tests.sh`. Update `pytest.ini` to point at `test_tools.py`.
- [ ] **Fix resources.py to use new patterns**: Use exception-based auth, use new client.py call signatures, parallelize queries with asyncio.gather().
- [ ] **Fix utils.py or remove it**: Currently has stale imports and call signatures. Either update to match new client.py or remove (new tools.py doesn't use it).
- [ ] **Improve _format_output**: Add recursive HTML-to-Markdown conversion for nested dicts/lists before JSON serialization.
- [ ] **aha_my_work uses f-string filters**: Lines 938-941 use inline f-string GraphQL filter construction instead of parameterized variables. Potential injection.
- [ ] **aha_recent_activity uses f-string filters**: Line 1028 uses f-string for project_filter and since date.

## P2: Feature Gaps (from simplified-tool-design.md)

- [ ] **Name-based identifier resolution for aha_create**: The `project` and `release` params accept IDs but not names. Should resolve "Q3 Release" -> release ID.
- [ ] **"me" / current user support in aha_my_work**: Design spec says "defaults to authenticated user" but implementation requires explicit email/ID.
- [ ] **Helpful not-found errors**: Design spec says errors should suggest similar records (e.g., "Did you mean PROJ-99?"). Current errors just say "not found".
- [ ] **Filter parameters on aha_search**: `status` and `tags` filters are accepted as parameters but not actually wired into the GraphQL query.

## P3: MCP Best Practices Still Missing

- [ ] **stdio transport documentation**: MCP best practices recommend stdio for local use. README should document both stdio and HTTP transport options.
- [ ] **MCP-native error codes**: errors.py defines the hierarchy but tools catch exceptions and return JSON error strings instead of raising McpError with proper error codes (-32602, -32603, etc.).
- [ ] **Resource subscriptions**: MCP spec recommends `notifications/resources/updated` for changing resources. Not implemented.
- [ ] **Progress notifications**: Long-running operations should send progress updates. Not implemented.
- [ ] **Output schemas**: MCP spec recommends `outputSchema` for structured tool responses. Not implemented.
- [ ] **listChanged notifications**: Should notify when available tools/resources change. Not implemented.

## P3: Distribution & Adoption

- [ ] **Package as pip installable**: `pip install aha-mcp` would improve adoption.
- [ ] **Dockerfile**: For containerized deployment.
- [ ] **manifest.json**: Anthropic plugin format compatibility.
- [ ] **MCP Inspector testing**: Verify server works with the official MCP Inspector.

## P3: Test Coverage

- [ ] **Resources tests**: No tests for resources.py.
- [ ] **OAuth tests**: No tests for oauth.py endpoints.
- [ ] **Integration tests**: No tests that verify actual GraphQL query construction (current tests mock at the function level).
- [ ] **Error path tests**: Limited negative testing for validation failures.
- [ ] **Resolver tests**: No tests for resolver.py identifier resolution logic.
