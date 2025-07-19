# Aha! GraphQL API Documentation

## Overview

The Aha! Develop GraphQL API provides a flexible way to find and update information in your Aha! account. You can use the GraphQL API within extensions to closely integrate them with your Aha! Develop data.

## GraphQL API Explorer

The primary way to explore and test the GraphQL API is through the **GraphQL API Explorer**, where you can:
- Run GraphQL queries and requests against your live account
- Access documentation on all endpoints and fields
- Test queries before implementing them in your extensions

## Authentication

All API requests must be appropriately authenticated. If you are accessing the API through an extension, you can assume you are already authenticated as the user accessing that extension.

## API Methods

The API provides several methods for working with GraphQL:

- `aha.graphQuery` - Send a GraphQL query
- `aha.graphMutate` - Send a GraphQL mutation

Each method returns a promise containing the result.

## Note on Documentation

The complete GraphQL API documentation is available within the GraphQL API Explorer in your Aha! account. The explorer provides:
- Interactive query building
- Complete schema documentation
- Field descriptions and types
- Real-time query testing

## Additional Resources

- [Extension API Reference](https://www.aha.io/support/develop/develop/extensions/extension-api-reference) - Primary entrypoint for extensions
- [Model API](./aha-graphql-model-api.md) - ActiveRecord-style ORM for GraphQL
- [REST API](https://www.aha.io/api) - Alternative REST API documentation

## Integration with This MCP Server

This MCP server uses the GraphQL API to provide tools for:
- Fetching records (features, requirements, pages)
- Searching documents
- Creating, updating, and deleting features
- Listing features with filters
- GraphQL introspection

For the actual GraphQL queries used by this server, see `src/queries.ts`.