# Aha! Model API Documentation

## Overview

The Model API provides an ActiveRecord-style ORM interface for working with the Aha! Develop GraphQL API. It offers a familiar, object-oriented approach to accessing and manipulating data within your Aha! account.

## Key Features

Models can communicate with the Aha! Develop GraphQL API in a way that should feel familiar if you've used an ActiveRecord-style ORM. The Model API:

- Provides object-oriented access to Aha! data
- Handles relationships between different types of records
- Simplifies common CRUD operations
- Integrates seamlessly with Aha! Develop extensions

## Integration with GraphQL

The Model API is built on top of the GraphQL API, providing a higher-level abstraction that:
- Automatically constructs GraphQL queries
- Maps GraphQL responses to model objects
- Handles type conversions and validations
- Manages relationships between models

## Using with Extensions

When building Aha! Develop extensions, the Model API provides a more intuitive way to work with data compared to raw GraphQL queries. Models abstract away the complexity of GraphQL while still providing full access to the underlying data.

## Documentation Access

The complete Model API documentation is available within your Aha! Develop account. This includes:
- Available models and their attributes
- Relationship definitions
- Method references
- Code examples

## Relationship to This MCP Server

While this MCP server primarily uses direct GraphQL queries (found in `src/queries.ts`), understanding the Model API can help when:
- Designing new GraphQL queries
- Understanding the data structure
- Planning extensions that complement this MCP server

## Additional Resources

- [GraphQL API Documentation](./aha-graphql-api.md) - Underlying GraphQL API
- [Extension API Reference](https://www.aha.io/support/develop/develop/extensions/extension-api-reference)
- GraphQL schema file: `docs/aha-graphql-api/aha-graphql-api.json` (contains full schema definition)