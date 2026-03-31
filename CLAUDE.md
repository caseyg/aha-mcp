# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python MCP server for Aha! using FastMCP 2.0. Recently refactored from 78 endpoint-per-tool wrappers to 10 unified tools following Anthropic's [Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) guidelines.

Based on the original TypeScript MCP server by Aha! but rewritten in Python with significantly broader API coverage and a simplified tool surface.

## Commands

### Build and Run
- `uv sync` -- Install dependencies (preferred, uses pyproject.toml)
- `uv run python aha_mcp.py` -- Run the server via UV
- `pip install -r requirements.txt` -- Install dependencies (legacy)
- `python aha_mcp.py` -- Run the server (stdio transport)
- `fastmcp run aha_mcp.py` -- Run via FastMCP CLI

### Testing
- `uv run pytest test_tools.py -v` -- Run the tool tests via UV (preferred)
- `pytest test_tools.py -v` -- Run the tool tests (primary test suite)
- `pytest test_tools.py -k "test_aha_get"` -- Run a specific test

### Development Requirements
- Python 3.10+
- FastMCP 2.0 framework
- Dependencies: `fastmcp>=2.0.0`, `httpx`, `python-dotenv`, `markdown>=3.5`, `markdownify>=0.13`, `starlette`, `uvicorn`, `authlib`
- Test dependencies: `pytest>=7.0.0`, `pytest-asyncio>=0.21.0`, `pytest-mock>=3.10.0`

## Architecture

### Module Map

```
aha_mcp.py       -- Entry point. Creates FastMCP instance, registers tools/prompts/resources/oauth.
client.py        -- Shared httpx.AsyncClient with connection pooling (20 connections),
                    30s timeout, retry on 429/503 with exponential backoff.
                    Exports: graphql(ctx, query, variables), rest_api(ctx, method, endpoint, ...),
                    check_auth(), get_auth_headers(), close_client(), oauth_tokens.
tools.py         -- 10 unified tools: aha_get, aha_search, aha_create, aha_update,
                    aha_delete, aha_promote_idea, aha_upload_attachment, aha_my_work,
                    aha_recent_activity, aha_introspect.
resolver.py      -- Flexible identifier resolution. Accepts reference numbers (PROJ-123),
                    names ("Q3 Planning"), or numeric IDs. Resolves via pattern matching,
                    GraphQL lookup, or search API.
formatting.py    -- Bidirectional Markdown <-> HTML conversion using markdown + markdownify.
                    Auto-detects input format via HTML tag heuristic.
errors.py        -- Error hierarchy: AhaError -> AhaAuthError, AhaNotFoundError,
                    AhaValidationError, AhaApiError. Each carries message + suggestion.
cache.py         -- TTL cache with @cached decorator. Used for introspection (5min TTL).
prompts.py       -- 10 MCP prompts for common workflows (backlog analysis, release planning, etc.)
resources.py     -- 4 MCP resources: releases by status, ideas by filter, assigned work, recent updates.
oauth.py         -- OAuth 2.0 discovery, authorization, token endpoints.
```

### Key Design Patterns

1. **One tool per CRUD verb**: `aha_get`, `aha_search`, `aha_create`, `aha_update`, `aha_delete` handle all record types via `record_type` parameter.
2. **Flexible identifier resolution**: `resolver.py` accepts any identifier format. Pattern-based detection for references, search API fallback for names.
3. **GraphQL field fragments**: `CONCISE_FIELDS` and `DETAILED_FIELDS` dicts in `tools.py` define per-type field sets. `response_format` parameter selects between them.
4. **Tool annotations**: All tools registered with `readOnlyHint` and `destructiveHint` annotations.
5. **`asyncio.gather()`**: Composite tools (`aha_my_work`, `aha_recent_activity`) run parallel GraphQL queries.
6. **@cached decorator**: `cache.py` provides TTL caching for introspection queries.

### Authentication
- **API Token**: Set `AHA_API_TOKEN` and `AHA_DOMAIN` env vars.
- **OAuth**: Set `OAUTH_CLIENT_ID`, `OAUTH_CLIENT_SECRET`. Exposes discovery endpoints at `/.well-known/oauth-authorization-server`.
- Auth check: `client.py:check_auth()` raises `AhaAuthError` if no credentials.
- Auth headers: `client.py:get_auth_headers(ctx)` resolves per-user OAuth > API token > fallback.

### API Client (client.py)
- **Shared httpx.AsyncClient**: Lazy-created singleton with connection pooling.
- **graphql(ctx, query, variables)**: Parameterized queries only. Raises on GraphQL errors.
- **rest_api(ctx, method, endpoint, data, params, ...)**: REST fallback. Auto-prefixes `/api/v1`.
- **Retry**: 429/503 retried up to 3 times with exponential backoff.

### Reference Number Formats
- Features: `PROJ-123`
- Requirements: `PROJ-123-1`
- Ideas: `PROJ-I-45`
- Epics: `PROJ-E-1`
- Releases: `PROJ-R-3`
- Initiatives: `PROJ-IN-2`
- Goals: `PROJ-G-7`
- Pages: `PROJ-N-12`

## Research Docs
- `docs/simplified-tool-design.md` -- Design spec for the 10-tool architecture
- `docs/mcp-server-best-practices.md` -- MCP best practices research
- `docs/codebase-analysis.md` -- Analysis of the old 78-tool codebase
- `docs/competitive-analysis.md` -- Comparison with other Aha! MCP servers
- `docs/refactor-plan.md` -- Phased refactoring plan
