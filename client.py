"""Aha! API client with shared connection pool, retry logic, and auth support.

This module provides the low-level transport for every Aha! API call:
- A single shared ``httpx.AsyncClient`` with connection pooling.
- ``graphql()`` for GraphQL queries/mutations (parameterized variables only).
- ``rest_api()`` for REST endpoints.
- Auth-header helpers for both API-token and OAuth flows.
"""

import asyncio
import logging
import os
from typing import Any

import httpx
from dotenv import load_dotenv

from errors import AhaApiError, AhaAuthError

# ---------------------------------------------------------------------------
# Environment / configuration
# ---------------------------------------------------------------------------

load_dotenv()
logger = logging.getLogger(__name__)

AHA_DOMAIN: str = os.getenv("AHA_DOMAIN", "")
AHA_API_TOKEN: str = os.getenv("AHA_API_TOKEN", "")
OAUTH_CLIENT_ID: str = os.getenv("OAUTH_CLIENT_ID", "")
OAUTH_CLIENT_SECRET: str = os.getenv("OAUTH_CLIENT_SECRET", "")

# In-memory OAuth token storage (shared with oauth.py via register_oauth_routes).
oauth_tokens: dict[str, str] = {}

# ---------------------------------------------------------------------------
# Shared httpx.AsyncClient
# ---------------------------------------------------------------------------

_client: httpx.AsyncClient | None = None

_RETRYABLE_STATUS_CODES = {429, 503}
_MAX_RETRIES = 3
_RETRY_BACKOFF = 1.0  # seconds; doubles each attempt


async def get_client() -> httpx.AsyncClient:
    """Return (and lazily create) the shared ``httpx.AsyncClient``."""
    global _client
    if _client is None:
        _client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0, connect=10.0),
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )
    return _client


async def close_client() -> None:
    """Shut down the shared client (call on server teardown)."""
    global _client
    if _client is not None:
        await _client.aclose()
        _client = None


# ---------------------------------------------------------------------------
# Authentication helpers
# ---------------------------------------------------------------------------


def check_auth() -> None:
    """Raise ``AhaAuthError`` if no credentials are available."""
    if not AHA_API_TOKEN and not oauth_tokens:
        raise AhaAuthError(
            "Authentication required.",
            suggestion=(
                "Set the AHA_API_TOKEN environment variable or authenticate via OAuth.\n"
                f"OAuth available: {bool(OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET)}"
            ),
        )


def get_auth_headers(ctx: Any = None) -> dict[str, str]:
    """Build ``Authorization`` headers for an API request.

    Resolution order:
    1. OAuth token for the current user context (if *ctx* provides a user_id).
    2. Static ``AHA_API_TOKEN`` env var.
    3. First available OAuth token (single-user fallback).
    """
    # Per-user OAuth token
    if ctx and hasattr(ctx, "user_id") and getattr(ctx, "user_id", None) in oauth_tokens:
        return {"Authorization": f"Bearer {oauth_tokens[ctx.user_id]}"}

    # Static API token
    if AHA_API_TOKEN:
        return {"Authorization": f"Bearer {AHA_API_TOKEN}"}

    # Single-user OAuth fallback
    if oauth_tokens:
        token = next(iter(oauth_tokens.values()))
        return {"Authorization": f"Bearer {token}"}

    return {}


def _require_domain() -> str:
    """Return the configured Aha! domain or raise."""
    if not AHA_DOMAIN:
        raise AhaAuthError(
            "AHA_DOMAIN not configured.",
            suggestion="Set the AHA_DOMAIN environment variable (e.g., 'yourcompany').",
        )
    return AHA_DOMAIN


# ---------------------------------------------------------------------------
# Retry helper
# ---------------------------------------------------------------------------


async def _request_with_retry(
    method: str,
    url: str,
    **kwargs: Any,
) -> httpx.Response:
    """Execute an HTTP request with retry logic for 429/503."""
    client = await get_client()
    last_exc: Exception | None = None
    for attempt in range(_MAX_RETRIES):
        try:
            response = await client.request(method, url, **kwargs)
            if response.status_code not in _RETRYABLE_STATUS_CODES:
                return response
            # Retryable status -- back off and try again.
            retry_after = float(response.headers.get("Retry-After", _RETRY_BACKOFF * (2**attempt)))
            logger.warning(
                "Retryable %s from %s (attempt %d/%d), sleeping %.1fs",
                response.status_code,
                url,
                attempt + 1,
                _MAX_RETRIES,
                retry_after,
            )
            await asyncio.sleep(retry_after)
        except httpx.TransportError as exc:
            last_exc = exc
            await asyncio.sleep(_RETRY_BACKOFF * (2**attempt))

    # Exhausted retries -- return last response or raise last transport error.
    if last_exc is not None:
        raise AhaApiError(f"Request failed after {_MAX_RETRIES} retries: {last_exc}")
    # If we got here via retryable status codes, return the last response so
    # callers can inspect it.
    return response  # type: ignore[possibly-undefined]


# ---------------------------------------------------------------------------
# GraphQL
# ---------------------------------------------------------------------------


async def graphql(
    query: str,
    variables: dict[str, Any] | None = None,
    ctx: Any = None,
) -> dict[str, Any]:
    """Execute a GraphQL query/mutation against the Aha! API.

    All queries **must** use ``$variables`` for parameterization -- never
    f-string interpolation.  This function enforces that by accepting
    *variables* as a separate dict.

    Raises:
        AhaAuthError: on 401.
        AhaApiError: on GraphQL-level errors or unexpected HTTP failures.
    """
    check_auth()
    domain = _require_domain()
    url = f"https://{domain}.aha.io/api/v2/graphql"

    headers = get_auth_headers(ctx)
    payload = {"query": query, "variables": variables or {}}

    response = await _request_with_retry("POST", url, json=payload, headers=headers)

    if response.status_code == 401:
        raise AhaAuthError(
            "Authentication failed (HTTP 401).",
            suggestion="Check your API token or re-authenticate via OAuth.",
        )
    if response.status_code >= 400:
        raise AhaApiError(
            f"Aha! API returned HTTP {response.status_code}: {response.text}"
        )

    data = response.json()
    if "errors" in data and data["errors"]:
        messages = [e.get("message", str(e)) for e in data["errors"]]
        raise AhaApiError(f"GraphQL errors: {messages}")

    return data.get("data", {})


# ---------------------------------------------------------------------------
# REST API
# ---------------------------------------------------------------------------


async def rest_api(
    method: str,
    endpoint: str,
    data: dict[str, Any] | list | None = None,
    params: dict[str, str] | None = None,
    use_form_data: bool = False,
    ctx: Any = None,
) -> Any:
    """Execute a REST API request against the Aha! v1 API.

    *endpoint* should be a path like ``"/features/PROJ-123"`` (the ``/api/v1``
    prefix is added automatically if missing).

    Raises:
        AhaAuthError: on 401.
        AhaApiError: on unexpected HTTP failures.
    """
    check_auth()
    domain = _require_domain()

    if not endpoint.startswith("/api/"):
        endpoint = f"/api/v1{endpoint}"
    url = f"https://{domain}.aha.io{endpoint}"

    headers = get_auth_headers(ctx)
    headers["Accept"] = "application/json"

    kwargs: dict[str, Any] = {"headers": headers}
    if params:
        kwargs["params"] = params

    if data is not None:
        if use_form_data:
            kwargs["data"] = data
        else:
            headers["Content-Type"] = "application/json"
            kwargs["json"] = data

    response = await _request_with_retry(method.upper(), url, **kwargs)

    if response.status_code == 401:
        raise AhaAuthError(
            "Authentication failed (HTTP 401).",
            suggestion="Check your API token or re-authenticate via OAuth.",
        )
    if response.status_code >= 400:
        raise AhaApiError(
            f"Aha! REST API returned HTTP {response.status_code}: {response.text}"
        )

    if response.content:
        return response.json()
    return None
