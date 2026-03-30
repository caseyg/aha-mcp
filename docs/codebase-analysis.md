# Aha! MCP Server — Detailed Code Review Report

**Date:** 2026-03-30
**Scope:** Full codebase analysis of caseyg/aha-mcp (Python/FastMCP 2.0)

---

## 1. Architecture Overview

### Module Dependency Graph
```
aha-mcp.py (entry point)
  ├── client.py (API client: graphql, rest_api, check_auth, get_auth_headers, oauth_tokens)
  ├── tools.py (78 tool functions, imports from client.py and utils.py)
  ├── utils.py (helper functions/classes, imports from client.py)
  ├── prompts.py (10 prompt definitions)
  ├── resources.py (4 resource implementations, imports from client.py)
  └── oauth.py (OAuth route handlers, imports httpx directly)
```

### Registration Pattern
All modules use a `register_X(mcp_instance)` function pattern where the MCP instance is passed in, stored as a module-level global, and then tools/prompts/resources are registered imperatively. Resources have a **dual registration problem** — they are registered both inside `resources.py:register_resources()` AND again via decorators in `aha-mcp.py` (lines 38-56). Notably, `register_resources()` is never actually called from `aha-mcp.py` — the import on line 35 just grabs the raw functions.

---

## 2. Critical Bugs

### BUG 1: Indentation error in `resources.py` lines 134-159
The `releases_by_status` function has a serious indentation bug. The `feature_stats` calculation block (lines 135-159) is indented under the `continue` branch's `else` clause for the "active" status filter, but logically needs to run for ALL releases including "all" and "parking-lot" filtered ones. For non-"active" status values, `feature_stats` is never computed, causing a `KeyError` on line 169 (`r["feature_stats"]["total"]`).

### BUG 2: Duplicate key in `build_standard_fields` (utils.py lines 192-253)
The `"requirement"` key appears twice in the `extended_fields` dictionary (line 198 and line 243). The second definition (line 243, with fewer fields) silently overwrites the first (line 198, with more fields like `position`, `originalEstimate`, etc.). The first, more complete definition is the one that gets lost.

### BUG 3: `delete_feature` returns wrong shape (tools.py line 514)
`delete_feature` manually builds a success response with `{"success": True, "id": id}`, but the test at line 401-402 checks `data["success"]` and `data["id"]`. The actual response is `{"success": True, "message": "Feature DEMO-35 deleted", "deleted_feature": ...}` — there is no `"id"` key. The test passes only because the mock never reaches the actual function logic.

---

## 3. Tool Design Analysis

### Tool Descriptions
The tool descriptions are **too terse for LLM consumption**, particularly the newer tools. Examples:
- `"Modify epics (GraphQL available)"` (line 1110) — does not explain what fields can be modified
- `"Remove phases"` (line 2380) — no context about what phases are
- `"Get position details"` (line 2926) — no context about strategic positions

The **older core tools** have better descriptions (e.g., `get_record` at line 174, `update_feature` at line 358 with Args docstring). There is an inconsistency between old tools with full docstrings and new tools with one-liner descriptions.

### Parameter Types
- Parameters are well-typed with `Optional[str]`, `Optional[bool]`, `List[str]`, etc.
- However, `ctx: Context = None` should be `ctx: Optional[Context] = None` for consistency (used inconsistently across functions).
- The `delete_feature` function uses `id` as a parameter name (shadows Python built-in).

### Input Validation
- **Inconsistent**: `get_record` validates reference format (line 180), but `get_idea` does not validate the ID format when a non-reference string is passed.
- `list_features` requires at least one filter (line 272-273), but `list_initiatives` does not (line 1138), even though querying all initiatives without filters could return massive datasets.
- `create_user` validates roles (line 1755-1758), but `create_release_phase` duplicates its phase_type validation (checked at both lines 2278 and 2305).
- No input length validation anywhere — a user could pass megabytes of text as a description.

---

## 4. Error Handling

### Inconsistent Error Return Patterns
There are **four different error handling patterns** in use:

1. **Direct JSON string return**: `return json.dumps({"error": "..."})` (tools.py passim)
2. **`check_auth()` returns a JSON string or None**: Used as a guard at the top of every tool function
3. **`execute_graphql_query`/`execute_mutation`**: Catches exceptions and returns JSON error strings (utils.py lines 20-54)
4. **`execute_rest_api`**: Catches exceptions and returns JSON error strings (utils.py lines 257-274)

The problem: `check_auth()` returns a raw JSON string (client.py line 28), but other error paths return `json.dumps({"error": "..."})`. Both are strings, but `check_auth()` includes `{"error": "Authentication required", "message": "...", "oauth_available": ...}` while tool errors use `{"error": "Failed to X: ..."}`. Consumers cannot reliably distinguish auth errors from operational errors.

### Missing MCP Error Codes
Despite CLAUDE.md claiming "All errors use appropriate MCP error codes (InvalidParams, InternalError)", **no MCP error codes are used anywhere**. All errors are returned as plain JSON strings via the tool's return value, not raised as MCP-native errors. This means the MCP client has no programmatic way to distinguish error types.

### Bare Exception Catches
Most tools catch `Exception` broadly (e.g., tools.py line 197, line 210, line 253). The `ideas_by_filter` in resources.py line 256 has a bare `except:` (line 257) which will swallow even `KeyboardInterrupt`.

---

## 5. Authentication

### Token Storage
- Tokens are stored in a **module-level mutable dictionary** `oauth_tokens` in `client.py` (line 22).
- `oauth.py` has its **own** `oauth_tokens` dict (line 24) AND receives the client's dict via `register_oauth_routes(mcp, oauth_tokens)`. The `register_oauth_routes` function reassigns the global (line 29) but this only works because the dict reference is shared.
- OAuth states are stored in memory with no expiration (oauth.py line 22). The `created_at` timestamp is stored but never checked for staleness.

### Auth Check Issues
- `check_auth()` (client.py line 25-33) checks `if not AHA_API_TOKEN and not oauth_tokens`. But `oauth_tokens` is checked for truthiness (non-empty dict), which means any key in the dict — even an expired/invalid token — passes the check.
- `get_auth_headers` tries `ctx.user_id` (line 39) but `Context` in FastMCP may not have a `user_id` attribute, leading to silent fallthrough to API token auth.
- The "your-domain" fallback on line 67 and 105 in `client.py` is a placeholder that would cause confusing 404 errors.

### OAuth Security Issues
- **No PKCE verification**: The `/oauth/token` endpoint (oauth.py line 210-238) generates a **random token** via `generate_token()` and returns it without validating the authorization code.
- **No CSRF protection**: OAuth state values are stored but the callback (line 133) does not verify the state matches a pending authorization.
- **XSS in error page**: `client_id` is reflected directly into HTML on line 108: `f"<h1>Invalid Client</h1><p>Unknown client_id: {client_id}</p>"`. This is a reflected XSS vector.
- **Error leakage in OAuth callback**: Line 206 returns `str(e)` directly to the user in HTML, potentially leaking internal details.

---

## 6. API Client (client.py)

### httpx.AsyncClient Per-Request (Major Performance Issue)
**Every single API call creates and destroys an httpx.AsyncClient** via `async with httpx.AsyncClient() as client:` (client.py lines 74, 116; oauth.py line 163). This means:
- No connection pooling or reuse
- No HTTP/2 multiplexing
- SSL handshake on every request
- For `resources.py:my_assigned_work`, this is **4 sequential API calls**, each with a new TCP connection

### No Timeouts
Neither `graphql()` nor `rest_api()` set any timeout. A hanging Aha! server would block the MCP tool indefinitely.

### No Retries
No retry logic for transient failures (429 rate limits, 503 service unavailable, network errors).

### REST API Method Handling
The `rest_api` function (client.py lines 94-145) uses a cascading if/elif chain for HTTP methods instead of using `httpx.AsyncClient.request()`. This pattern duplicates `form_data` handling across POST and PUT.

---

## 7. Code Quality Issues

### Massive Code Duplication

**The auth guard pattern is repeated 78+ times:**
```python
auth_error = check_auth()
if auth_error:
    return auth_error
```
This 3-line block appears at the start of every single tool function. The `@require_auth` decorator exists in `utils.py` (line 10-17) but is **never used** in tools.py.

**REST endpoint query parameter building** is repeated ~15 times with the same pattern:
```python
params = []
if page > 1:
    params.append(f"page={page}")
if per_page != 20:
    params.append(f"per_page={per_page}")
if params:
    endpoint += "?" + "&".join(params)
```

**The "update with optional fields" pattern** is repeated ~12 times.

### Two Eras of Tool Implementation
The codebase has **two eras** of tool implementation:
1. **Early tools** (get_record, list_features, create_feature, etc.) — Inline GraphQL queries, manual attribute building, manual error checking
2. **Later tools** (list_epics, create_epic, etc.) — Use `build_list_query`, `CrudTemplates`, `execute_mutation`, `build_attributes` from utils.py

The early tools were never refactored to use the utilities, creating two parallel patterns for the same operations.

### GraphQL Injection Risk
`list_features` (line 285) and `list_ideas` (line 697) construct GraphQL filters by string interpolation:
```python
filters.append(f'projectId: "{project_id}"')
```
This is vulnerable to GraphQL injection if `project_id` contains quotes or special characters.

### tools.py Size
At 3,006 lines and 94KB, `tools.py` is a monolith. It should be split into domain-specific modules.

---

## 8. Performance Concerns

- **No caching**: `list_workflows`, `list_custom_fields`, `get_all_tags` fetch relatively static data fresh every call
- **Large payloads**: `releases_by_status` fetches up to 50 releases with 100 features each — potentially thousands of records
- **Sequential queries**: `my_assigned_work` and `recent_updates` make 4 sequential GraphQL calls that could be parallelized with `asyncio.gather()`
- **No pagination caps**: `list_features` allows arbitrary `per_page` with no upper bound

---

## 9. Security Concerns

- **GraphQL injection** via f-string filter construction in `list_features` and `list_ideas`
- **No input sanitization** — description fields accept arbitrary content, `file_url` in `upload_attachment` accepts any URL (potential SSRF)
- **Reflected XSS** in OAuth error pages
- **Error leakage** in OAuth callback returns internal exception details

---

## 10. Testing Analysis

### Coverage
- 27 tests covering ~10 of 78 tools (~13% tool coverage)
- **Zero tests** for: epics, releases, initiatives, goals, requirements, comments, tasks, key results, record links, products, release phases, idea votes, pages, portal management, strategic elements, integrations, attachments, users

### Test Quality Issues
- Mock patches `tools.graphql` but some tools call `rest_api` directly — mock level mismatch
- Tests do not verify GraphQL query content, only that the mock was called
- No negative tests for most error paths
- No integration tests
- Test file uses `importlib` to handle the hyphen in `aha-mcp.py` — renaming to `aha_mcp.py` would simplify

---

## 11. Priority Refactoring Items

| Priority | Item | Impact |
|----------|------|--------|
| P0 | Fix indentation bug in `resources.py` | Runtime error for non-active releases |
| P0 | Fix duplicate "requirement" key in `utils.py` | Silent data loss |
| P0 | Fix GraphQL injection in `list_features`/`list_ideas` | Security vulnerability |
| P1 | Create shared httpx.AsyncClient with pooling + timeouts + retries | Performance, reliability |
| P1 | Apply `@require_auth` decorator (replace 78 copy-paste guards) | Code quality |
| P1 | Parameterize all GraphQL queries | Security |
| P1 | Fix OAuth security (PKCE verification, state validation, XSS) | Security |
| P2 | Split tools.py into domain modules | Maintainability |
| P2 | Standardize error handling with MCP error types | Correctness |
| P2 | Refactor early tools to use utils.py patterns | Consistency |
| P2 | Improve tool descriptions for LLM consumption | Usability |
| P3 | Add missing tests (65+ untested tools) | Reliability |
| P3 | Parallelize sequential resource queries | Performance |
| P3 | Add response caching for static data | Performance |
