#!/usr/bin/env node
import 'dotenv/config';
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";
import { GraphQLClient } from "graphql-request";
import { Handlers } from "./handlers.js";

const AHA_API_TOKEN = process.env.AHA_API_TOKEN;
const AHA_DOMAIN = process.env.AHA_DOMAIN;

if (!AHA_API_TOKEN) {
  throw new Error("AHA_API_TOKEN environment variable is required");
}

if (!AHA_DOMAIN) {
  throw new Error("AHA_DOMAIN environment variable is required");
}

const client = new GraphQLClient(
  `https://${AHA_DOMAIN}.aha.io/api/v2/graphql`,
  {
    headers: {
      Authorization: `Bearer ${AHA_API_TOKEN}`,
    },
  }
);

class AhaMcp {
  private server: Server;
  private handlers: Handlers;

  constructor() {
    this.server = new Server(
      {
        name: "aha-mcp",
        version: "1.0.0",
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.handlers = new Handlers(client);
    this.setupToolHandlers();

    this.server.onerror = (error) => console.error("[MCP Error]", error);
    process.on("SIGINT", async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: "get_record",
          description: "Get an Aha! feature or requirement by reference number",
          inputSchema: {
            type: "object",
            properties: {
              reference: {
                type: "string",
                description:
                  "Reference number (e.g., DEVELOP-123 or ADT-123-1)",
              },
            },
            required: ["reference"],
          },
        },
        {
          name: "get_page",
          description:
            "Get an Aha! page by reference number with optional relationships",
          inputSchema: {
            type: "object",
            properties: {
              reference: {
                type: "string",
                description: "Reference number (e.g., ABC-N-213)",
              },
              includeParent: {
                type: "boolean",
                description: "Include parent page in the response",
                default: false,
              },
            },
            required: ["reference"],
          },
        },
        {
          name: "search_documents",
          description: "Search for Aha! documents",
          inputSchema: {
            type: "object",
            properties: {
              query: {
                type: "string",
                description: "Search query string",
              },
              searchableType: {
                type: "string",
                description: "Type of document to search for (e.g., Page)",
                default: "Page",
              },
            },
            required: ["query"],
          },
        },
        {
          name: "create_feature",
          description: "Create a new feature in Aha!",
          inputSchema: {
            type: "object",
            properties: {
              releaseId: {
                type: "string",
                description: "ID or reference number of the release",
              },
              name: {
                type: "string",
                description: "Name of the feature",
              },
              description: {
                type: "string",
                description: "Description of the feature (supports markdown)",
              },
              assignedToUserId: {
                type: "string",
                description: "ID of the user to assign the feature to",
              },
              tags: {
                type: "array",
                items: { type: "string" },
                description: "Tags to add to the feature",
              },
              workflowStatusId: {
                type: "string",
                description: "ID of the workflow status",
              },
              epicId: {
                type: "string",
                description: "ID or reference number of the epic",
              },
              teamId: {
                type: "string",
                description: "ID of the team to assign the feature to",
              },
            },
            required: ["releaseId", "name"],
          },
        },
        {
          name: "update_feature",
          description: "Update an existing feature in Aha!",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the feature",
              },
              name: {
                type: "string",
                description: "New name for the feature",
              },
              description: {
                type: "string",
                description: "New description for the feature (supports markdown)",
              },
              workflowStatusId: {
                type: "string",
                description: "ID of the new workflow status",
              },
              assignedToUserId: {
                type: "string",
                description: "ID of the user to reassign the feature to",
              },
              tags: {
                type: "array",
                items: { type: "string" },
                description: "New tags for the feature",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "delete_feature",
          description: "Delete a feature from Aha!",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the feature to delete",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "list_features",
          description: "List features in Aha! with optional filters",
          inputSchema: {
            type: "object",
            properties: {
              releaseId: {
                type: "string",
                description: "Filter by release ID or reference",
              },
              epicId: {
                type: "string",
                description: "Filter by epic ID or reference",
              },
              productId: {
                type: "string",
                description: "Filter by product ID or reference",
              },
              goalId: {
                type: "string",
                description: "Filter by goal ID or reference",
              },
              initiativeId: {
                type: "string",
                description: "Filter by initiative ID or reference",
              },
              page: {
                type: "number",
                description: "Page number for pagination",
              },
              perPage: {
                type: "number",
                description: "Number of items per page",
              },
            },
          },
        },
        {
          name: "get_feature_details",
          description: "Get detailed information about a specific feature",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the feature",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "introspection",
          description: "Perform GraphQL introspection to explore the Aha! API schema with size-limited responses",
          inputSchema: {
            type: "object",
            properties: {
              queryType: {
                type: "string",
                enum: ["list-types", "simple", "query", "mutation", "type", "search-queries", "search-mutations"],
                description: "Type of introspection query. 'list-types' shows available types, 'type' explores a specific type, 'query'/'mutation' list operations",
                default: "list-types",
              },
              typeName: {
                type: "string",
                description: "Name of the type to introspect (required when queryType is 'type'). Examples: Idea, Feature, Project, User",
              },
              searchTerm: {
                type: "string",
                description: "Search term to filter results by name/description",
              },
              maxResults: {
                type: "number",
                description: "Maximum number of results to return (default: 50)",
                default: 50,
              },
            },
          },
        },
        {
          name: "get_idea",
          description: "Get an Aha! idea by ID or reference number",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the idea (e.g., ABC-I-123)",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "list_ideas",
          description: "List ideas in Aha! with optional filters",
          inputSchema: {
            type: "object",
            properties: {
              projectId: {
                type: "string",
                description: "Filter by project ID or reference (required)",
              },
              assignedToUserId: {
                type: "string",
                description: "Filter by assigned user ID",
              },
              visibility: {
                type: "string",
                description: "Filter by visibility (e.g., public, private)",
              },
              promoted: {
                type: "boolean",
                description: "Filter for promoted/not promoted ideas",
              },
              page: {
                type: "number",
                description: "Page number for pagination",
              },
              perPage: {
                type: "number",
                description: "Number of items per page",
              },
            },
            required: ["projectId"],
          },
        },
        {
          name: "create_idea",
          description: "Create a new idea in Aha!",
          inputSchema: {
            type: "object",
            properties: {
              projectId: {
                type: "string",
                description: "ID or reference number of the project",
              },
              name: {
                type: "string",
                description: "Name of the idea",
              },
              description: {
                type: "string",
                description: "Description of the idea (supports markdown)",
              },
              visibility: {
                type: "string",
                description: "Visibility of the idea (e.g., public, private)",
              },
              assignedToUserId: {
                type: "string",
                description: "ID of the user to assign the idea to",
              },
            },
            required: ["projectId", "name"],
          },
        },
        {
          name: "update_idea",
          description: "Update an existing idea in Aha!",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the idea",
              },
              name: {
                type: "string",
                description: "New name for the idea",
              },
              description: {
                type: "string",
                description: "New description for the idea (supports markdown)",
              },
              visibility: {
                type: "string",
                description: "New visibility for the idea",
              },
              assignedToUserId: {
                type: "string",
                description: "ID of the user to reassign the idea to",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "delete_idea",
          description: "Delete an idea from Aha!",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the idea to delete",
              },
            },
            required: ["id"],
          },
        },
        {
          name: "promote_idea",
          description: "Promote an idea to a feature, epic, or requirement",
          inputSchema: {
            type: "object",
            properties: {
              id: {
                type: "string",
                description: "ID or reference number of the idea to promote",
              },
              type: {
                type: "string",
                enum: ["feature", "epic", "requirement"],
                description: "Type to promote the idea to",
              },
              projectId: {
                type: "string",
                description: "ID or reference of the project (required for feature promotion if releaseId not provided)",
              },
              releaseId: {
                type: "string",
                description: "ID or reference of the release (required for feature promotion if projectId not provided)",
              },
              featureId: {
                type: "string",
                description: "ID or reference of the feature to link to",
              },
            },
            required: ["id", "type"],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name === "get_record") {
        return this.handlers.handleGetRecord(request);
      } else if (request.params.name === "get_page") {
        return this.handlers.handleGetPage(request);
      } else if (request.params.name === "search_documents") {
        return this.handlers.handleSearchDocuments(request);
      } else if (request.params.name === "create_feature") {
        return this.handlers.handleCreateFeature(request);
      } else if (request.params.name === "update_feature") {
        return this.handlers.handleUpdateFeature(request);
      } else if (request.params.name === "delete_feature") {
        return this.handlers.handleDeleteFeature(request);
      } else if (request.params.name === "list_features") {
        return this.handlers.handleListFeatures(request);
      } else if (request.params.name === "get_feature_details") {
        return this.handlers.handleGetFeatureDetails(request);
      } else if (request.params.name === "introspection") {
        return this.handlers.handleIntrospection(request);
      } else if (request.params.name === "get_idea") {
        return this.handlers.handleGetIdea(request);
      } else if (request.params.name === "list_ideas") {
        return this.handlers.handleListIdeas(request);
      } else if (request.params.name === "create_idea") {
        return this.handlers.handleCreateIdea(request);
      } else if (request.params.name === "update_idea") {
        return this.handlers.handleUpdateIdea(request);
      } else if (request.params.name === "delete_idea") {
        return this.handlers.handleDeleteIdea(request);
      } else if (request.params.name === "promote_idea") {
        return this.handlers.handlePromoteIdea(request);
      }

      throw new McpError(
        ErrorCode.MethodNotFound,
        `Unknown tool: ${request.params.name}`
      );
    });
  }

  async run() {
    const transportType = process.env.TRANSPORT || "stdio";
    
    // For now, only support stdio transport as SSE requires HTTP server setup
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error("Aha! MCP server running on stdio");
  }
}

const server = new AhaMcp();
server.run().catch(console.error);
