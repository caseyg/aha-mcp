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
          description: "Perform GraphQL introspection to explore the Aha! API schema",
          inputSchema: {
            type: "object",
            properties: {
              queryType: {
                type: "string",
                enum: ["full", "simple", "query", "mutation"],
                description: "Type of introspection query to run (default: full)",
                default: "full",
              },
            },
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
