"""MCP-native error handling for Aha! MCP operations."""


class AhaError(Exception):
    """Base error for Aha! MCP operations."""

    def __init__(self, message: str, suggestion: str | None = None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)


class AhaAuthError(AhaError):
    """Authentication or authorization failure."""
    pass


class AhaNotFoundError(AhaError):
    """Record not found."""
    pass


class AhaValidationError(AhaError):
    """Invalid input or parameter."""
    pass


class AhaApiError(AhaError):
    """Upstream Aha! API error (5xx, unexpected response)."""
    pass


def format_error(error: AhaError) -> str:
    """Format an error with a helpful message and optional suggestion.

    Examples:
        Error: Could not find record "PROJ-999".
        Did you mean: PROJ-99 (Q3 Planning), PROJ-9 (User Research)?
        Example: aha_get("PROJ-123") or aha_get("Q3 Planning")
    """
    parts = [f"Error: {error.message}"]
    if error.suggestion:
        parts.append(error.suggestion)
    return "\n".join(parts)
