"""MCP-native error handling for Aha! MCP operations.

Uses ``fastmcp.exceptions.ToolError`` so FastMCP returns proper MCP error
responses (``isError=True``) instead of the tool returning JSON error strings.
"""

from fastmcp.exceptions import ToolError


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


def raise_tool_error(error: AhaError) -> None:
    """Convert an AhaError into a ToolError and raise it.

    This bridges the domain error hierarchy with FastMCP's ToolError so that
    tool functions can let domain exceptions propagate as proper MCP errors.
    """
    raise ToolError(format_error(error)) from error


def tool_error_from_message(message: str, hint: str | None = None) -> ToolError:
    """Create a ToolError with an optional hint line."""
    parts = [message]
    if hint:
        parts.append(f"Hint: {hint}")
    return ToolError("\n".join(parts))
