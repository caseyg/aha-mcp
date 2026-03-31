"""Flexible identifier resolution for Aha! records.

Every tool that accepts an identifier should accept **any of**:
- Reference number: PROJ-123, PROJ-I-45, PROJ-E-1, PROJ-N-12
- Name/title: "Q3 Sprint Planning" (resolved via search)
- Numeric ID: 6789012345

The server resolves internally so the agent never needs to know which format
to use.
"""

import re
from typing import Any

from errors import AhaNotFoundError

# ---------------------------------------------------------------------------
# Reference-number patterns
# ---------------------------------------------------------------------------

FEATURE_REF = re.compile(r"^[A-Z0-9]+-\d+$")          # PROJ-123
REQUIREMENT_REF = re.compile(r"^[A-Z0-9]+-\d+-\d+$")   # PROJ-123-1
IDEA_REF = re.compile(r"^[A-Z0-9]+-I-\d+$")             # PROJ-I-45
EPIC_REF = re.compile(r"^[A-Z0-9]+-E-\d+$")             # PROJ-E-1
RELEASE_REF = re.compile(r"^[A-Z0-9]+-R-\d+$")          # PROJ-R-3
INITIATIVE_REF = re.compile(r"^[A-Z0-9]+-IN-\d+$")      # PROJ-IN-2
GOAL_REF = re.compile(r"^[A-Z0-9]+-G-\d+$")             # PROJ-G-7
PAGE_REF = re.compile(r"^[A-Z0-9]+-N-\d+$")             # PROJ-N-12

# Ordered so more-specific patterns match first (requirement before feature).
_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (REQUIREMENT_REF, "requirement"),
    (IDEA_REF, "idea"),
    (EPIC_REF, "epic"),
    (RELEASE_REF, "release"),
    (INITIATIVE_REF, "initiative"),
    (GOAL_REF, "goal"),
    (PAGE_REF, "page"),
    (FEATURE_REF, "feature"),  # must come after requirement
]


def detect_record_type(reference: str) -> str | None:
    """Infer the record type from a reference-number string.

    Returns a type name like ``"feature"`` or ``None`` if the string does not
    match any known pattern.
    """
    for pattern, record_type in _PATTERNS:
        if pattern.match(reference):
            return record_type
    return None


def is_reference(identifier: str) -> bool:
    """Return ``True`` if *identifier* looks like an Aha! reference number."""
    return any(p.match(identifier) for p, _ in _PATTERNS)


async def resolve_identifier(
    identifier: str,
    record_type: str | None = None,
    ctx: Any = None,
) -> dict[str, Any]:
    """Resolve a name, reference number, or numeric ID to an Aha! record.

    Returns ``{"id": ..., "type": ..., "reference": ...}`` or raises
    :class:`AhaNotFoundError`.

    Resolution order:
    1. Reference-number pattern -- instant, no API call needed (the reference
       is passed directly to GraphQL).
    2. Numeric ID -- assumed to be a direct database ID.
    3. Name search -- falls back to the Aha! search API.
    """
    # Avoid circular import; client is lightweight and cached.
    from client import graphql  # noqa: WPS433

    identifier = identifier.strip()

    # ------------------------------------------------------------------
    # 1. Reference number (no API call required to *identify* the record,
    #    but we still resolve it to confirm it exists and get its ID).
    # ------------------------------------------------------------------
    detected = detect_record_type(identifier)
    if detected:
        rtype = record_type or detected
        result = await _fetch_by_reference(identifier, rtype, ctx)
        if result:
            return result
        raise AhaNotFoundError(
            f'Could not find {rtype} "{identifier}".',
            suggestion=f'Example: aha_get("{identifier}") -- check that the reference exists in your Aha! account.',
        )

    # ------------------------------------------------------------------
    # 2. Numeric ID
    # ------------------------------------------------------------------
    if identifier.isdigit():
        if not record_type:
            raise AhaNotFoundError(
                f'Numeric ID "{identifier}" requires a record_type to resolve.',
                suggestion='Provide record_type (e.g., "feature") or use a reference number like "PROJ-123".',
            )
        return {"id": identifier, "type": record_type, "reference": None}

    # ------------------------------------------------------------------
    # 3. Name search
    # ------------------------------------------------------------------
    results = await _search_by_name(identifier, record_type, ctx)
    if len(results) == 1:
        return results[0]
    if len(results) > 1:
        candidates = ", ".join(
            f'{r.get("reference", r["id"])} ({r.get("name", "?")})'
            for r in results[:5]
        )
        raise AhaNotFoundError(
            f'Multiple matches for "{identifier}".',
            suggestion=f"Did you mean: {candidates}?\nPlease specify the exact reference number.",
        )
    raise AhaNotFoundError(
        f'Could not find any record matching "{identifier}".',
        suggestion=f'Example: aha_get("PROJ-123") or aha_get("Q3 Planning")',
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

# GraphQL type names used in the Aha! API for each record type.
_GQL_TYPE_MAP: dict[str, str] = {
    "feature": "feature",
    "requirement": "requirement",
    "idea": "idea",
    "epic": "epic",
    "release": "release",
    "initiative": "initiative",
    "goal": "goal",
    "page": "page",
}


async def _fetch_by_reference(
    reference: str, record_type: str, ctx: Any
) -> dict[str, Any] | None:
    """Fetch a record by its reference number via GraphQL."""
    from client import graphql  # noqa: WPS433

    gql_type = _GQL_TYPE_MAP.get(record_type)
    if not gql_type:
        return None

    query = """
    query($ref: String!) {
        %s(referenceNum: $ref) {
            id
            referenceNum
            name
        }
    }
    """ % gql_type

    try:
        data = await graphql(query, variables={"ref": reference}, ctx=ctx)
        record = data.get(gql_type)
        if record:
            return {
                "id": record["id"],
                "type": record_type,
                "reference": record.get("referenceNum", reference),
                "name": record.get("name"),
            }
    except Exception:
        pass
    return None


async def _search_by_name(
    name: str, record_type: str | None, ctx: Any
) -> list[dict[str, Any]]:
    """Search for records by name via the Aha! search API."""
    from client import rest_api  # noqa: WPS433

    endpoint = "/search"
    params = {"q": name}
    if record_type:
        params["type"] = record_type

    try:
        data = await rest_api("GET", endpoint, params=params, ctx=ctx)
        if not data:
            return []
        results: list[dict[str, Any]] = []
        for item in data if isinstance(data, list) else data.get("results", data.get("search_results", [])):
            results.append({
                "id": item.get("id", ""),
                "type": item.get("type", record_type or "unknown"),
                "reference": item.get("reference_num", item.get("referenceNum")),
                "name": item.get("name", item.get("title", "")),
            })
        return results
    except Exception:
        return []
