# MCP Server Best Practices: A Comprehensive Research Report

**Compiled: 2026-03-30**
**Sources: MCP Specification (modelcontextprotocol.io), Anthropic Engineering, FastMCP documentation, community practices**

---

## Table of Contents

1. [Architecture and Design Principles](#1-architecture-and-design-principles)
2. [Tool Design Best Practices](#2-tool-design-best-practices)
3. [Resource Design Best Practices](#3-resource-design-best-practices)
4. [Prompt Design Best Practices](#4-prompt-design-best-practices)
5. [Transport Selection and Configuration](#5-transport-selection-and-configuration)
6. [Error Handling Patterns](#6-error-handling-patterns)
7. [Security Best Practices](#7-security-best-practices)
8. [Authentication and Authorization](#8-authentication-and-authorization)
9. [Pagination and Large Result Sets](#9-pagination-and-large-result-sets)
10. [Performance Considerations](#10-performance-considerations)
11. [Testing Strategies](#11-testing-strategies)
12. [Common Anti-Patterns](#12-common-anti-patterns)
13. [Lifecycle Management](#13-lifecycle-management)

---

## 1. Architecture and Design Principles

### Client-Server Model

MCP follows a strict client-server architecture. An **MCP host** (such as Claude Desktop, Claude Code, or VS Code) creates one **MCP client** per **MCP server** connection. Each client maintains a dedicated, independent connection to its server.

**Key architectural principles:**

- **Servers are context providers.** MCP servers expose tools, resources, and prompts. They do not dictate how the AI application uses LLMs or manages context -- that is the host's responsibility.
- **Capability negotiation is mandatory.** During initialization, both client and server declare what they support. Both parties MUST only use capabilities that were successfully negotiated.
- **The protocol is stateful.** MCP requires proper lifecycle management with initialization, operation, and shutdown phases. The initialization handshake MUST be the first interaction.
- **One client per server.** Local servers (stdio) typically serve a single client. Remote servers (Streamable HTTP) may serve multiple clients simultaneously.

### Two-Layer Design

MCP consists of two layers:

1. **Data layer** -- JSON-RPC 2.0 based protocol for message structure, lifecycle management, and primitives (tools, resources, prompts, notifications).
2. **Transport layer** -- Communication mechanisms (stdio, Streamable HTTP) that handle connection establishment, message framing, and authorization.

The data layer is transport-agnostic. The same JSON-RPC message format works across all transports.

### Three Core Primitives

| Primitive | Control Model | Purpose |
|-----------|--------------|---------|
| **Tools** | Model-controlled | Executable functions the LLM can invoke (API calls, computations, database queries) |
| **Resources** | Application-driven | Data sources providing contextual information (files, schemas, API responses) |
| **Prompts** | User-controlled | Reusable templates for structuring LLM interactions (slash commands, system prompts) |

**Recommendation:** Choose the right primitive for the right job. Do not shoehorn everything into tools. Use resources for read-only context data. Use prompts for reusable interaction templates. Use tools only for actions that have side effects or require dynamic computation.

---

## 2. Tool Design Best Practices

### Naming Conventions

- Use clear, descriptive names that follow a consistent pattern: `domain_action` (e.g., `weather_current`, `calculator_arithmetic`, `database_query`).
- Names should be unique identifiers within the server's namespace.
- Avoid vague names like `do_thing` or `process` -- the name should immediately convey what the tool does.
- Use `title` for human-readable display names (e.g., `"title": "Weather Information Provider"`).

### Description Guidelines

- Write descriptions that explain **what the tool does** and **when to use it**.
- Descriptions are consumed by LLMs to decide which tool to invoke. They must be precise and unambiguous.
- Include information about expected input formats in field-level descriptions (e.g., `"description": "City name, address, or coordinates (latitude,longitude)"`).
- Document default values for optional parameters in their descriptions.

### Input Schema Design

- Always provide a complete JSON Schema via `inputSchema`.
- Mark parameters as `required` when they are truly necessary.
- Provide sensible defaults for optional parameters and document them.
- Use `enum` constraints when the set of valid values is known (e.g., `"enum": ["metric", "imperial", "kelvin"]`).
- Include helpful `description` fields on every property -- these guide the LLM in constructing correct tool calls.

### Output Schema (Structured Content)

- Consider providing an `outputSchema` for tools that return structured data. This enables:
  - Strict schema validation of responses
  - Type information for better integration
  - Better documentation and developer experience
  - Clients and LLMs can properly parse and utilize returned data
- When returning structured content in `structuredContent`, ALSO return the serialized JSON in a `TextContent` block for backwards compatibility.
- Use the `isError` field to distinguish successful results from tool execution errors.

### Tool Annotations

- Provide annotations that describe tool behavior (audience, priority).
- Note: Clients MUST consider tool annotations to be untrusted unless they come from trusted servers.

### Human-in-the-Loop

The spec is explicit: there SHOULD always be a human in the loop with the ability to deny tool invocations. Applications SHOULD:
- Provide UI that makes clear which tools are being exposed to the AI model.
- Insert clear visual indicators when tools are invoked.
- Present confirmation prompts to the user for operations.

---

## 3. Resource Design Best Practices

### URI Design

- Every resource MUST be uniquely identified by a URI conforming to RFC 3986.
- Use standard URI schemes where appropriate:
  - `file://` for filesystem-like resources (do not need to map to actual files)
  - `https://` only when the client can fetch the resource directly from the web
  - `git://` for version control integration
- Custom URI schemes MUST conform to RFC 3986.
- Validate all resource URIs on the server side.

### Resource Templates

- Use URI templates (RFC 6570) for parameterized resources (e.g., `file:///{path}`).
- Support auto-completion through the completion API for template arguments.
- Provide clear descriptions for templates explaining what parameters are expected.

### Metadata and Annotations

- Always include `name` and `mimeType` when known.
- Use `title` for human-readable display names.
- Use annotations to guide clients:
  - `audience`: `["user"]`, `["assistant"]`, or `["user", "assistant"]` to indicate intended consumers.
  - `priority`: 0.0 to 1.0 indicating importance (1 = required, 0 = optional).
  - `lastModified`: ISO 8601 timestamp for freshness tracking.
- Include `size` in bytes when available for binary resources.

### Subscriptions

- Implement the `subscribe` capability if resources change over time.
- Send `notifications/resources/updated` when subscribed resources change.
- Send `notifications/resources/list_changed` when the set of available resources changes.
- These notifications prevent clients from polling and enable real-time synchronization.

### Content Types

- Return text content for text-based resources with appropriate MIME types.
- Return binary content as base64-encoded blobs with correct MIME types.
- Binary data MUST be properly encoded.

---

## 4. Prompt Design Best Practices

### Design Principles

- Prompts are **user-controlled** -- they should be explicitly selectable by users (e.g., as slash commands).
- Each prompt should have a clear, specific purpose.
- Use `arguments` to make prompts customizable and reusable.
- Mark arguments as `required` or optional appropriately.

### Message Structure

- Prompts return an array of `PromptMessage` objects with `role` and `content`.
- Support multi-turn conversations by returning messages with both `user` and `assistant` roles.
- Embed resources directly in prompt messages for rich context.
- Support multiple content types: text, image, audio, and embedded resources.

### Security

- MUST carefully validate all prompt inputs and outputs to prevent injection attacks.
- Validate prompt arguments before processing.
- Sanitize any user-provided content that gets interpolated into prompts.

---

## 5. Transport Selection and Configuration

### stdio Transport

**When to use:** Local integrations where the client launches the server as a subprocess.

**Characteristics:**
- Zero network overhead -- optimal performance for local operations.
- Client launches server as a subprocess.
- Messages delimited by newlines; messages MUST NOT contain embedded newlines.
- Server reads from stdin, writes to stdout.
- Server MAY write to stderr for logging; clients MAY capture, forward, or ignore it.
- Server MUST NOT write non-MCP content to stdout.

**Best practices:**
- Prefer stdio whenever the server runs on the same machine as the client.
- Clients SHOULD support stdio whenever possible.
- Use stderr for diagnostic logging, never stdout.
- Implement clean shutdown: client closes stdin, waits for exit, then SIGTERM, then SIGKILL.

### Streamable HTTP Transport

**When to use:** Remote servers, multi-client scenarios, or when HTTP infrastructure (load balancers, proxies) is needed.

**Characteristics:**
- Server provides a single HTTP endpoint supporting POST and GET.
- Client sends JSON-RPC messages via POST.
- Server may respond with `application/json` or `text/event-stream` (SSE).
- Supports session management via `Mcp-Session-Id` header.
- Supports resumability and redelivery via SSE event IDs.

**Best practices:**
- MUST validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks.
- When running locally, SHOULD bind only to localhost (127.0.0.1), not 0.0.0.0.
- SHOULD implement proper authentication for all connections.
- Session IDs SHOULD be globally unique and cryptographically secure (e.g., UUID, JWT, or cryptographic hash).
- Session IDs MUST only contain visible ASCII characters (0x21 to 0x7E).
- Implement the `MCP-Protocol-Version` header on all requests for version negotiation.
- Support both paginated and streaming responses.

### Backwards Compatibility (SSE to Streamable HTTP)

The old HTTP+SSE transport from protocol version 2024-11-05 is deprecated. For backwards compatibility:
- Servers wanting to support older clients should host both old and new endpoints.
- Clients should attempt POST first, then fall back to GET if they get a 4xx response.

---

## 6. Error Handling Patterns

### Two Error Categories

MCP distinguishes between two types of errors:

1. **Protocol Errors** -- Standard JSON-RPC errors for protocol-level issues:
   - Unknown tool: `-32602`
   - Invalid arguments: `-32602`
   - Resource not found: `-32002`
   - Internal errors: `-32603`
   - Unsupported protocol version: `-32602`

2. **Tool Execution Errors** -- Reported in tool results with `isError: true`:
   - API failures
   - Invalid input data
   - Business logic errors
   - Rate limit exceeded

### Best Practices

- **Use the right error type.** Protocol errors for protocol-level issues (tool not found, invalid params). Tool execution errors for business logic failures (API down, invalid data).
- **Provide descriptive error messages.** Include enough context for the LLM to understand what went wrong and potentially retry or adjust.
- **Return error details in the `data` field** for protocol errors when additional context helps (e.g., supported versions, valid parameter values).
- **Never expose internal implementation details** in error messages that could leak security-sensitive information.
- **Handle invalid cursors gracefully** -- return error code `-32602`.

### Timeout Handling

- Implement timeouts for all sent requests to prevent hung connections.
- When a timeout occurs, send a cancellation notification and stop waiting.
- SDKs and middleware SHOULD allow per-request timeout configuration.
- MAY reset the timeout clock when receiving progress notifications (indicating active work).
- SHOULD always enforce a maximum timeout regardless of progress notifications.

---

## 7. Security Best Practices

### Input Validation

Servers MUST:
- Validate all tool inputs against the declared schema.
- Validate all resource URIs.
- Sanitize tool outputs before returning them.
- Check resource permissions before operations.

### Access Controls

- Implement proper access controls for all tools and resources.
- Rate limit tool invocations to prevent abuse.
- Log tool usage for audit purposes.

### Clients SHOULD:
- Prompt for user confirmation on sensitive operations.
- Show tool inputs to the user before calling the server (prevents data exfiltration).
- Validate tool results before passing to the LLM.
- Implement timeouts for tool calls.

### DNS Rebinding Prevention

When implementing Streamable HTTP:
- MUST validate the `Origin` header on all incoming connections.
- SHOULD bind to localhost only when running locally.
- SHOULD implement proper authentication for all connections.

### Session Security

- Use secure, non-deterministic session IDs (cryptographically random UUIDs).
- MUST NOT use sessions for authentication -- always verify authorization on every request.
- Bind session IDs to user-specific information when possible (`<user_id>:<session_id>`).
- Rotate or expire session IDs to limit hijacking windows.

### Local Server Security

Local MCP servers pose unique risks because they execute on the user's machine with client privileges:
- MCP clients MUST implement consent mechanisms before executing local server commands.
- Display the exact command that will be executed (no truncation).
- Highlight dangerous patterns (sudo, rm -rf, network operations, sensitive file access).
- Execute servers in sandboxed environments with minimal default privileges.
- Use platform-appropriate sandboxing (containers, chroot, application sandboxes).
- For local HTTP servers, prefer stdio transport or require authorization tokens.

### SSRF Prevention

MCP clients MUST consider SSRF risks when fetching OAuth-related URLs:
- Require HTTPS for all OAuth URLs in production.
- Block requests to private/reserved IP ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16).
- Validate redirect targets (do not blindly follow redirects to internal resources).
- Consider egress proxies for server-side deployments.
- Be aware of DNS rebinding / TOCTOU issues.

### Token Passthrough Prevention

Token passthrough is **explicitly forbidden**. An MCP server MUST NOT accept tokens from clients and pass them through to downstream APIs. Risks include:
- Bypassing security controls (rate limiting, validation, monitoring).
- Breaking audit trails and accountability.
- Trust boundary violations.
- If the MCP server calls upstream APIs, it must use separate tokens issued by the upstream authorization server.

---

## 8. Authentication and Authorization

### Overview

Authorization is OPTIONAL but recommended for production servers. The MCP spec defines a comprehensive OAuth 2.1-based authorization framework for HTTP transports.

### Transport-Specific Guidance

| Transport | Approach |
|-----------|----------|
| **HTTP-based** | SHOULD conform to the MCP authorization spec (OAuth 2.1) |
| **stdio** | SHOULD NOT use the OAuth spec; retrieve credentials from the environment instead |
| **Alternative transports** | MUST follow established security best practices for their protocol |

### OAuth 2.1 Implementation

When implementing OAuth:
- Authorization servers MUST implement OAuth 2.1 with appropriate security measures.
- MCP servers MUST implement OAuth 2.0 Protected Resource Metadata (RFC 9728).
- Authorization servers MUST provide OAuth 2.0 Authorization Server Metadata (RFC 8414).
- Support Dynamic Client Registration (RFC 7591) for seamless connection to new servers.
- Clients MUST implement PKCE to prevent authorization code interception.
- Clients MUST implement Resource Indicators (RFC 8707) to bind tokens to intended audiences.

### Access Token Requirements

- Use `Authorization: Bearer <token>` header on every HTTP request (even within a session).
- Access tokens MUST NOT be included in URI query strings.
- Servers MUST validate that tokens were issued specifically for them.
- Authorization servers SHOULD issue short-lived access tokens.
- For public clients, MUST rotate refresh tokens.

### Scope Minimization

- Start with minimal scope sets (e.g., `mcp:tools-basic` for discovery/read operations).
- Use incremental elevation via `WWW-Authenticate` challenges when privileged operations are attempted.
- Avoid wildcard or omnibus scopes (`*`, `all`, `full-access`).
- Do not bundle unrelated privileges.
- Accept reduced-scope tokens gracefully.

---

## 9. Pagination and Large Result Sets

### Cursor-Based Pagination

MCP uses opaque cursor-based pagination (not numbered pages):
- The cursor is an opaque string token representing a position in the result set.
- Page size is determined by the server; clients MUST NOT assume a fixed page size.
- Absence of `nextCursor` indicates the end of results.

### Supported Operations

Pagination applies to:
- `resources/list`
- `resources/templates/list`
- `prompts/list`
- `tools/list`

### Implementation Guidelines

**Servers SHOULD:**
- Provide stable cursors that survive concurrent modifications.
- Handle invalid cursors gracefully (return error code `-32602`).
- Choose appropriate page sizes based on the data volume and expected client behavior.

**Clients SHOULD:**
- Treat a missing `nextCursor` as the end of results.
- Support both paginated and non-paginated flows.

**Clients MUST:**
- Treat cursors as opaque tokens.
- Not make assumptions about cursor format.
- Not attempt to parse or modify cursors.
- Not persist cursors across sessions.

---

## 10. Performance Considerations

### Transport Performance

- **stdio** has zero network overhead and is optimal for local operations. Always prefer it for same-machine communication.
- **Streamable HTTP** adds HTTP overhead but enables remote access, load balancing, and multi-client support.

### Tool Design for Performance

- Keep tool response payloads focused and minimal. Return only what the LLM needs.
- For large results, consider returning resource links instead of embedding full content.
- Use `outputSchema` to enable efficient structured parsing on the client side.
- Implement progress notifications for long-running operations so clients can track status and reset timeouts.

### Resource Design for Performance

- Use pagination for large resource lists.
- Include `size` metadata so clients can make informed decisions about fetching.
- Use `priority` annotations (0.0-1.0) so clients can prioritize which resources to include in context.
- Use `audience` annotations to avoid sending assistant-only data to user interfaces and vice versa.
- Leverage subscriptions instead of polling for resource updates.

### Connection Management

- Implement timeouts on all requests with per-request configurability.
- Use cancellation notifications when abandoning timed-out requests.
- For Streamable HTTP, support session management to avoid repeated initialization overhead.
- For SSE streams, implement resumability with event IDs to handle disconnections gracefully without data loss.

### Capability Negotiation Efficiency

- Only declare capabilities you actually support. This reduces the surface area clients need to manage.
- Use `listChanged` notifications to push updates instead of requiring clients to poll.

---

## 11. Testing Strategies

### Use the MCP Inspector

The official **MCP Inspector** (github.com/modelcontextprotocol/inspector) is the primary development tool for testing MCP servers. It allows you to:
- Connect to your server via stdio or HTTP.
- Inspect capability negotiation.
- Browse and invoke tools, resources, and prompts.
- View raw JSON-RPC messages.
- Test error handling and edge cases.

### Unit Testing Tools

- Test each tool handler independently with valid, invalid, and edge-case inputs.
- Verify that tool outputs conform to declared `outputSchema`.
- Test that `isError: true` is returned for expected failure conditions.
- Validate that input schema validation catches malformed arguments.

### Integration Testing

- Test the full lifecycle: initialization, capability negotiation, operation, shutdown.
- Verify capability negotiation works correctly (server only exposes negotiated capabilities).
- Test pagination with various cursor states (initial, mid-stream, invalid, expired).
- Test notification delivery (tool list changes, resource updates).

### Transport Testing

- Test both stdio and HTTP transports if your server supports both.
- For HTTP, test session management (creation, reuse, expiration, invalid session IDs).
- Test SSE streaming and resumability.
- Test concurrent client connections for HTTP servers.

### Security Testing

- Verify input validation rejects malformed or malicious inputs.
- Test that access controls are enforced.
- Verify token validation (audience binding, expiration, scope).
- Test DNS rebinding protection for local HTTP servers.
- Verify that sensitive data is not leaked in error messages.

### Error Path Testing

- Test protocol error responses (unknown tool, invalid params).
- Test tool execution error responses (API failures, rate limits).
- Test timeout behavior and cancellation flows.
- Test behavior when capabilities are not negotiated (server should reject unsupported operations).

---

## 12. Common Anti-Patterns

### Anti-Pattern: Token Passthrough

Accepting a client's access token and forwarding it directly to downstream APIs. This bypasses security controls, breaks audit trails, and creates confused deputy vulnerabilities. MCP servers MUST validate that tokens are issued specifically for them and MUST NOT pass them through.

### Anti-Pattern: Overly Broad Tool Design

Creating a single "do everything" tool instead of focused, composable tools. Each tool should have a clear, specific purpose. The LLM selects tools based on descriptions -- ambiguous or overly broad tools lead to misuse.

### Anti-Pattern: Missing Input Validation

Trusting that the LLM or client will always provide valid inputs. Servers MUST validate all inputs against the declared schema and implement additional business logic validation.

### Anti-Pattern: Exposing Everything as Tools

Using tools for read-only context data that should be resources, or for reusable templates that should be prompts. Misusing primitives confuses the control model (model-controlled vs. application-driven vs. user-controlled).

### Anti-Pattern: Wildcard Scopes

Publishing all possible scopes in `scopes_supported` or using omnibus scopes like `*`, `all`, or `full-access`. This maximizes blast radius when tokens are compromised.

### Anti-Pattern: Polling Instead of Notifications

Having clients poll for changes instead of implementing `listChanged` notifications and resource subscriptions. Polling wastes bandwidth and introduces latency.

### Anti-Pattern: Non-Opaque Cursors

Designing pagination cursors that clients can parse, predict, or modify. Cursors MUST be opaque tokens. Do not use sequential integers or predictable formats that clients might depend on.

### Anti-Pattern: Ignoring Capability Negotiation

Sending requests for capabilities that were not negotiated. Both client and server MUST respect the negotiated capability set.

### Anti-Pattern: Logging to stdout (stdio transport)

Writing diagnostic output to stdout when using stdio transport. The server MUST NOT write anything to stdout that is not a valid MCP message. Use stderr for logging.

### Anti-Pattern: Binding HTTP Servers to 0.0.0.0

When running a local HTTP server, binding to all interfaces instead of localhost. This exposes the server to the network and enables DNS rebinding attacks.

### Anti-Pattern: No Human in the Loop

Allowing the LLM to invoke arbitrary tools without user confirmation. There SHOULD always be a human in the loop with the ability to deny tool invocations, especially for operations with side effects.

### Anti-Pattern: Hardcoding Model Names

In sampling requests, specifying exact model names. Use model preference hints and capability priorities instead, as the client may have different models available. Hints are advisory; clients make the final selection.

---

## 13. Lifecycle Management

### Initialization Phase

1. Client sends `initialize` request with protocol version, capabilities, and client info.
2. Server responds with its protocol version, capabilities, server info, and optional `instructions`.
3. Client sends `initialized` notification to signal readiness.
4. Client SHOULD NOT send requests (other than pings) before receiving the server's initialize response.
5. Server SHOULD NOT send requests (other than pings and logging) before receiving the `initialized` notification.

### Version Negotiation

- Client sends the latest protocol version it supports.
- If the server supports it, it responds with the same version.
- Otherwise, the server responds with the latest version it supports.
- If the client does not support the server's version, it SHOULD disconnect.

### Operation Phase

- Both parties MUST respect the negotiated protocol version.
- Both parties MUST only use capabilities that were successfully negotiated.
- Real-time notifications keep both sides synchronized (tool list changes, resource updates).

### Shutdown Phase

**stdio:**
1. Client closes stdin to the server process.
2. Client waits for the server to exit.
3. Client sends SIGTERM if the server does not exit in a reasonable time.
4. Client sends SIGKILL as a last resort.

**HTTP:**
- Client sends HTTP DELETE to the MCP endpoint with the session ID to explicitly terminate.
- Server MAY respond with 405 if it does not allow client-initiated termination.
- Server MAY terminate sessions at any time (responding with 404 to subsequent requests).

---

## Summary of Key Recommendations

1. **Choose the right primitive** for each capability (tools for actions, resources for context, prompts for templates).
2. **Write excellent tool descriptions** -- they are consumed by LLMs and directly affect tool selection quality.
3. **Validate everything** -- inputs, outputs, URIs, tokens, cursors.
4. **Keep humans in the loop** -- always provide a way for users to review and deny tool invocations.
5. **Use stdio for local, Streamable HTTP for remote** -- match the transport to the deployment model.
6. **Implement proper OAuth 2.1** for HTTP-based servers with scope minimization and token audience binding.
7. **Never pass through tokens** -- each service boundary needs its own token.
8. **Use notifications instead of polling** -- implement `listChanged` and subscriptions.
9. **Paginate large result sets** with opaque cursor-based pagination.
10. **Test with the MCP Inspector** and cover the full lifecycle in integration tests.
11. **Implement timeouts and cancellation** for all requests.
12. **Secure local servers** with sandboxing, consent dialogs, and localhost binding.

---

## Sources

- [MCP Specification - Architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
- [MCP Specification - Tools](https://modelcontextprotocol.io/docs/concepts/tools)
- [MCP Specification - Resources](https://modelcontextprotocol.io/docs/concepts/resources)
- [MCP Specification - Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
- [MCP Specification - Transports](https://modelcontextprotocol.io/docs/concepts/transports)
- [MCP Specification - Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
- [MCP Specification - Lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [MCP Specification - Pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination)
- [MCP Specification - Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [MCP Specification - Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers)
