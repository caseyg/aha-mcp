# Aha! MCP Server — Refactor Plan

**Date:** 2026-03-30
**Based on:** [Codebase Analysis](codebase-analysis.md) and [MCP Best Practices Research](../mcp-server-best-practices.md)

---

## Executive Summary

The aha-mcp server has comprehensive Aha! API coverage (78 tools) but suffers from critical bugs, security vulnerabilities, performance issues, and significant code duplication. This plan addresses findings in priority order across 4 phases, each independently shippable.

---

## Phase 1: Critical Fixes (P0)

**Goal:** Fix bugs and security vulnerabilities. No architectural changes.

### 1.1 Fix indentation bug in `resources.py`

The `feature_stats` calculation in `releases_by_status` is indented inside the `if status == "active"` branch. It must run for all status values.

```python
# BEFORE (broken): feature_stats only computed for "active"
# AFTER: dedent feature_stats block to loop body level
```

**Files:** `resources.py` lines 134-159

### 1.2 Fix duplicate dictionary key in `utils.py`

The `"requirement"` key in `build_standard_fields.extended_fields` appears twice. The second (less complete) definition silently overwrites the first.

**Fix:** Remove the duplicate at line 243 and keep the more complete definition at line 198.

**Files:** `utils.py` lines 192-253

### 1.3 Fix GraphQL injection in filter construction

`list_features` and `list_ideas` construct GraphQL filters via f-string interpolation, allowing injection through crafted `project_id` values.

**Fix:** Use GraphQL variables instead of string interpolation:
```python
# BEFORE (vulnerable):
filters.append(f'projectId: "{project_id}"')

# AFTER (safe):
variables["projectId"] = project_id
# In query: features(projectId: $projectId)
```

**Files:** `tools.py` lines 285, 697 (and any other f-string filter construction)

### 1.4 Fix OAuth security issues

- **XSS in error page** (`oauth.py` line 108): HTML-escape `client_id` before reflecting into HTML
- **Error leakage** (`oauth.py` line 206): Replace `str(e)` with a generic error message
- **State validation**: Verify OAuth state in callback matches a pending authorization
- **Token expiry**: Add TTL checks to `oauth_states` entries

**Files:** `oauth.py`

### 1.5 Fix `delete_feature` response shape

The function returns `{"success": True, "message": ...}` but tests expect `{"id": ...}`. Align the response and fix the test.

**Files:** `tools.py` line 514, `test_aha_mcp.py` lines 401-402

---

## Phase 2: Infrastructure (P1)

**Goal:** Fix the HTTP client, auth pattern, and error handling. These changes touch many files but are mechanical.

### 2.1 Shared httpx.AsyncClient with connection pooling

Create a module-level `AsyncClient` with:
- Connection pooling (reuse TCP connections to aha.io)
- Configurable timeout (30s default)
- Retry logic for 429/503/network errors with exponential backoff
- Proper lifecycle management (create on first use, close on shutdown)

```python
# client.py
_client: httpx.AsyncClient | None = None

async def get_client() -> httpx.AsyncClient:
    global _client
    if _client is None:
        _client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0, connect=10.0),
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )
    return _client

async def close_client():
    global _client
    if _client:
        await _client.aclose()
        _client = None
```

Replace all `async with httpx.AsyncClient() as client:` blocks with `client = await get_client()`.

**Files:** `client.py`, `oauth.py`

### 2.2 Apply `@require_auth` decorator

The decorator already exists in `utils.py` but is never used. Replace all 78 instances of:
```python
auth_error = check_auth()
if auth_error:
    return auth_error
```

With the decorator:
```python
@require_auth
async def my_tool(ctx: Context, ...):
```

**Files:** `tools.py` (78 functions), `utils.py` (verify decorator works correctly)

### 2.3 Standardize error handling

Per MCP spec, tools should raise typed errors, not return JSON error strings.

1. Define error types:
```python
class AhaAuthError(Exception): pass
class AhaValidationError(Exception): pass
class AhaApiError(Exception): pass
```

2. Update `check_auth()` to raise `AhaAuthError` instead of returning a string
3. Update tool utilities to raise instead of returning error strings
4. Add a FastMCP error handler that converts exceptions to proper MCP error responses

**Files:** `client.py`, `utils.py`, `tools.py`

### 2.4 Simplify REST API method dispatch

Replace the if/elif chain in `rest_api()` with `httpx.AsyncClient.request()`:
```python
response = await client.request(method.upper(), url, json=data, headers=headers)
```

**Files:** `client.py` lines 94-145

---

## Phase 3: Code Organization (P2)

**Goal:** Make the codebase maintainable. Split the monolith, unify patterns.

### 3.1 Split tools.py into domain modules

Create `tools/` package:
```
tools/
├── __init__.py          # register_tools() that imports all submodules
├── records.py           # get_record, search_documents, get_page
├── features.py          # list/create/update/delete features + tags, convert to epic
├── ideas.py             # list/create/update/delete ideas + promote, score, tags, votes
├── epics.py             # list/create/update/delete epics
├── initiatives.py       # list/create/update/delete initiatives
├── releases.py          # list/create/update/delete releases + phases, duplicate
├── goals.py             # list/create/update/delete goals + key results
├── requirements.py      # list/create/update/delete requirements
├── comments.py          # create/update/delete/list comments
├── tasks.py             # create/list/get/update/delete/complete tasks
├── users.py             # list/create users
├── pages.py             # list/create/update/delete pages
├── portals.py           # idea portals, portal users, subscriptions, categories
├── strategy.py          # strategic models, visions, positions
├── integrations.py      # integrations, integration fields
├── attachments.py       # upload/delete attachments
├── metadata.py          # tags, workflows, custom fields
├── products.py          # list/get products
├── record_links.py      # list/create/get/delete record links
└── introspection.py     # GraphQL introspection
```

Each module exports a `register(mcp)` function. The `__init__.py` calls all of them.

### 3.2 Refactor early tools to use utils.py patterns

Rewrite the "era 1" tools (get_record, list_features, create_feature, update_feature, etc.) to use `CrudTemplates`, `execute_mutation`, `build_list_query`, and `build_attributes` from utils.py.

### 3.3 Improve tool descriptions for LLM consumption

Per MCP best practices, every tool description should:
- Start with a verb (e.g., "List", "Create", "Update", "Delete")
- Explain what the tool does in one sentence
- Mention required parameters and their format
- Include example inputs where format is non-obvious (e.g., reference number formats)

```python
# BEFORE:
"Modify epics (GraphQL available)"

# AFTER:
"Update an existing epic's properties (name, description, status, dates).
Requires the epic's reference number (e.g., PROJ-E-1). Only provided
fields are updated; omitted fields remain unchanged."
```

### 3.4 Fix resource dual-registration

Remove the decorator-based resource registration from `aha-mcp.py` lines 38-56 and instead call `register_resources(mcp)` properly. Resources should be registered in one place only.

### 3.5 Rename `aha-mcp.py` to `aha_mcp.py`

The hyphen in the filename forces `importlib` hacks in tests. A simple rename eliminates this.

---

## Phase 4: Robustness (P3)

**Goal:** Improve test coverage, performance, and reliability.

### 4.1 Add tests for untested tools

65+ tools have zero test coverage. Add tests organized by domain module:
- Use the same mock pattern as existing tests
- Add both success and error path tests
- Verify GraphQL query content (not just that the mock was called)
- Add negative tests for validation failures

### 4.2 Parallelize sequential resource queries

`my_assigned_work` and `recent_updates` make 4 sequential API calls each. Use `asyncio.gather()`:

```python
# BEFORE:
features = await graphql(ctx, features_query)
epics = await graphql(ctx, epics_query)
requirements = await graphql(ctx, requirements_query)
tasks = await graphql(ctx, tasks_query)

# AFTER:
features, epics, requirements, tasks = await asyncio.gather(
    graphql(ctx, features_query),
    graphql(ctx, epics_query),
    graphql(ctx, requirements_query),
    graphql(ctx, tasks_query),
)
```

### 4.3 Add response caching for static data

Cache results of `list_workflows`, `list_custom_fields`, `get_all_tags`, and `introspection` with a TTL (e.g., 5 minutes):

```python
from functools import lru_cache
import time

_cache: dict[str, tuple[float, Any]] = {}
CACHE_TTL = 300  # 5 minutes

async def cached_query(key: str, query_fn):
    now = time.time()
    if key in _cache and now - _cache[key][0] < CACHE_TTL:
        return _cache[key][1]
    result = await query_fn()
    _cache[key] = (now, result)
    return result
```

### 4.4 Add pagination caps

Set maximum `per_page` values to prevent accidentally requesting huge datasets:
```python
per_page = min(per_page, 100)  # Cap at 100 items
```

### 4.5 Add MCP tool annotations

Per MCP spec, add `readOnlyHint`, `destructiveHint`, and `idempotentHint` annotations:
```python
mcp.tool(delete_feature, tags={"features", "delete"}, annotations={
    "readOnlyHint": False,
    "destructiveHint": True,
    "idempotentHint": True,
})
```

This helps LLM clients make informed decisions about which tools to call autonomously vs. requiring confirmation.

---

## Implementation Order

```
Week 1: Phase 1 (critical fixes) — 1-2 days
Week 1: Phase 2.1-2.2 (http client + auth decorator) — 2-3 days
Week 2: Phase 2.3-2.4 (error handling + REST simplification) — 1-2 days
Week 2: Phase 3.1-3.2 (split tools.py + unify patterns) — 2-3 days
Week 3: Phase 3.3-3.5 (descriptions + cleanup) — 1-2 days
Week 3-4: Phase 4 (tests + perf) — ongoing
```

Each phase can be shipped independently. Phase 1 should be done immediately as it contains bugs and security fixes.

---

## Appendix: Files Changed Per Phase

| Phase | Files | Estimated LOC Changed |
|-------|-------|----------------------|
| 1 | resources.py, utils.py, tools.py, oauth.py, test_aha_mcp.py | ~50 |
| 2 | client.py, utils.py, tools.py (78 functions) | ~300 |
| 3 | tools.py → tools/*.py, aha-mcp.py → aha_mcp.py | ~3000 (reorganization) |
| 4 | test_*.py, resources.py, tools/*.py | ~1500 |
