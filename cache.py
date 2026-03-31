"""Simple TTL cache for static data (workflows, tags, schema)."""

import time
import functools
from typing import Any, Awaitable, Callable

_cache: dict[str, tuple[float, Any]] = {}
DEFAULT_TTL: int = 300  # 5 minutes


async def get_cached(key: str, fetch_fn: Callable[..., Awaitable[Any]], ttl: int = DEFAULT_TTL) -> Any:
    """Return cached value if fresh, otherwise call *fetch_fn* and cache the result."""
    now = time.monotonic()
    if key in _cache:
        ts, value = _cache[key]
        if now - ts < ttl:
            return value
    value = await fetch_fn()
    _cache[key] = (now, value)
    return value


def cached(ttl_seconds: int = DEFAULT_TTL):
    """Decorator that caches async function results by their arguments.

    Usage:
        @cached(ttl_seconds=300)
        async def expensive_call(arg1, arg2):
            ...
    """
    def decorator(func: Callable[..., Awaitable[Any]]):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Build cache key from function name + args (exclude ctx)
            key_parts = [func.__name__]
            for a in args:
                if not hasattr(a, 'request_id'):  # skip Context objects
                    key_parts.append(str(a))
            for k, v in sorted(kwargs.items()):
                if k != 'ctx':
                    key_parts.append(f"{k}={v}")
            key = ":".join(key_parts)

            now = time.monotonic()
            if key in _cache:
                ts, value = _cache[key]
                if now - ts < ttl_seconds:
                    return value
            value = await func(*args, **kwargs)
            _cache[key] = (now, value)
            return value
        return wrapper
    return decorator


def invalidate(key: str | None = None) -> None:
    """Clear one key or, if *key* is ``None``, all cached data."""
    if key is None:
        _cache.clear()
    else:
        _cache.pop(key, None)
