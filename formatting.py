"""Markdown <-> HTML conversion for Aha! rich-text fields.

Aha!'s API expects HTML for descriptions/bodies and returns HTML in responses.
Agents naturally write and read Markdown. This module handles bidirectional
conversion transparently.
"""

import re

import markdown as _markdown_lib
from markdownify import markdownify as _markdownify


# Tags whose presence indicates the string is already HTML.
_HTML_TAG_RE = re.compile(
    r"<(?:p|h[1-6]|div|ul|ol|li|table|tr|td|th|br|hr|blockquote|pre|code|strong|em|a|img)\b",
    re.IGNORECASE,
)

# Cruft patterns stripped from Aha! HTML before converting to Markdown.
_EMPTY_DIV_RE = re.compile(r"<div[^>]*>\s*</div>", re.IGNORECASE)
_STYLE_ATTR_RE = re.compile(r'\s+style="[^"]*"', re.IGNORECASE)
_NBSP_RE = re.compile(r"&nbsp;")


def is_html(text: str) -> bool:
    """Heuristic: does *text* contain HTML tags?"""
    return bool(_HTML_TAG_RE.search(text))


def markdown_to_html(text: str) -> str:
    """Convert Markdown to HTML.

    Auto-detects if the input is already HTML and passes it through unchanged.
    """
    if not text:
        return text
    if is_html(text):
        return text
    return _markdown_lib.markdown(
        text,
        extensions=["tables", "fenced_code", "nl2br"],
    )


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean Markdown.

    Strips empty divs, inline style attributes, and ``&nbsp;`` entities before
    conversion so the resulting Markdown is free of cruft.
    """
    if not html:
        return html
    # Clean common Aha! HTML cruft
    cleaned = _EMPTY_DIV_RE.sub("", html)
    cleaned = _STYLE_ATTR_RE.sub("", cleaned)
    cleaned = _NBSP_RE.sub(" ", cleaned)
    result = _markdownify(cleaned, heading_style="ATX", strip=["style"])
    # Collapse runs of blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def format_description(text: str, target: str = "html") -> str:
    """Format a description for the target format.  Used on **input** to Aha!.

    *target* is ``"html"`` (default, for the Aha! API) or ``"markdown"``.
    """
    if not text:
        return text
    if target == "html":
        return markdown_to_html(text)
    return html_to_markdown(text) if is_html(text) else text


def format_response_field(value: str, content_format: str = "markdown") -> str:
    """Format a response field for output.  Used on **output** from Aha!.

    *content_format* is ``"markdown"`` (default) or ``"html"`` (raw pass-through).
    """
    if not value:
        return value
    if content_format == "html":
        return value
    return html_to_markdown(value) if is_html(value) else value
