#!/usr/bin/env node
import 'dotenv/config';
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";
import { GraphQLClient } from "graphql-request";
import { Handlers } from "./handlers.js";
import { OAuthHandler, OAuthConfig } from "./oauth.js";
import express from "express";
import cors from "cors";
import crypto from "crypto";

// Environment variables
const AHA_API_TOKEN = process.env.AHA_API_TOKEN;
const AHA_DOMAIN = process.env.AHA_DOMAIN;
const OAUTH_CLIENT_ID = process.env.OAUTH_CLIENT_ID;
const OAUTH_CLIENT_SECRET = process.env.OAUTH_CLIENT_SECRET;
const OAUTH_REDIRECT_URI = process.env.OAUTH_REDIRECT_URI || 'http://localhost:3000/oauth/callback';

console.error("OAuth Environment Variables:", {
  clientId: OAUTH_CLIENT_ID ? `${OAUTH_CLIENT_ID.substring(0, 10)}...` : "NOT SET",
  clientSecret: OAUTH_CLIENT_SECRET ? "SET" : "NOT SET",
  redirectUri: OAUTH_REDIRECT_URI,
  domain: AHA_DOMAIN
});

// Determine authentication mode
const useOAuth = !!(OAUTH_CLIENT_ID && OAUTH_CLIENT_SECRET);

if (!useOAuth && !AHA_API_TOKEN) {
  throw new Error("Either AHA_API_TOKEN or OAuth credentials (OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET) must be provided");
}

if (!useOAuth && !AHA_DOMAIN) {
  throw new Error("AHA_DOMAIN environment variable is required when using API token authentication");
}

// Create GraphQL client for API token mode
const apiTokenClient = AHA_API_TOKEN ? new GraphQLClient(
  `https://${AHA_DOMAIN}.aha.io/api/v2/graphql`,
  {
    headers: {
      Authorization: `Bearer ${AHA_API_TOKEN}`,
    },
  }
) : null;

class AhaMcp {
  private server: Server;
  private handlers: Handlers | null = null;
  private oauthHandler: OAuthHandler | null = null;
  private sessionClients: Map<string, GraphQLClient> = new Map();

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

    // Initialize OAuth handler if in OAuth mode
    if (useOAuth) {
      const port = parseInt(process.env.PORT || "3000");
      const oauthConfig: OAuthConfig = {
        clientId: OAUTH_CLIENT_ID,
        clientSecret: OAUTH_CLIENT_SECRET,
        redirectUri: OAUTH_REDIRECT_URI,
        ahaDomain: AHA_DOMAIN,
        serverUrl: `http://localhost:${port}` // Canonical URL of this MCP server
      };
      this.oauthHandler = new OAuthHandler(oauthConfig);
      
      // Clean up expired tokens periodically
      setInterval(() => {
        this.oauthHandler?.cleanupExpiredTokens();
      }, 60 * 60 * 1000); // Every hour
    } else {
      // Use API token mode
      this.handlers = new Handlers(apiTokenClient!);
    }

    this.setupToolHandlers();

    this.server.onerror = (error) => console.error("[MCP Error]", error);
    process.on("SIGINT", async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private getOrCreateClient(sessionId: string): GraphQLClient | null {
    if (!useOAuth) {
      return apiTokenClient;
    }

    if (!this.oauthHandler) {
      return null;
    }

    // Check if we have a cached client
    if (this.sessionClients.has(sessionId)) {
      return this.sessionClients.get(sessionId)!;
    }

    // Get token and subdomain for session
    const token = this.oauthHandler.getToken(sessionId);
    const subdomain = this.oauthHandler.getSubdomain(sessionId);

    if (!token || !subdomain) {
      return null;
    }

    // Create new client for this session
    const client = new GraphQLClient(
      `https://${subdomain}.aha.io/api/v2/graphql`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    this.sessionClients.set(sessionId, client);
    return client;
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      const tools = [];

      // OAuth authentication is now handled by MCP Inspector's built-in OAuth flow
      // No need for manual auth tools

      // Add all the API tools
      tools.push(
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
        }
      );

      return { tools };
    });

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      // OAuth authentication is now handled by MCP Inspector's built-in OAuth flow

      // Debug: log the request structure
      console.error("Tool request received:", {
        name: request.params.name,
        requestKeys: Object.keys(request),
        requestProto: Object.keys(Object.getPrototypeOf(request)),
        meta: (request as any)._meta,
        sessionId: (request as any).sessionId,
        _sessionId: (request as any)._sessionId
      });

      // For OAuth mode, check if session is authenticated
      let handlers = this.handlers;

      if (useOAuth) {
        // Check if we have a client from Bearer token (Inspector flow)
        // Look for bearer token clients stored during SSE setup
        let bearerClient: GraphQLClient | undefined;
        
        // Try to find bearer token client from global context
        if ((global as any).bearerTokenClients) {
          const bearerTokenClientsMap = (global as any).bearerTokenClients as Map<string, GraphQLClient>;
          
          // If there's only one client, use it (common case)
          if (bearerTokenClientsMap.size === 1) {
            bearerClient = Array.from(bearerTokenClientsMap.values())[0];
            console.error(`Using single Bearer token client`);
          } else if (bearerTokenClientsMap.size > 0) {
            // Try to get the most recently added client
            const entries = Array.from(bearerTokenClientsMap.entries());
            const [sessionId, client] = entries[entries.length - 1];
            bearerClient = client;
            console.error(`Using most recent Bearer token client from session: ${sessionId}`);
          }
        } else {
          console.error(`No bearerTokenClients in global context`);
        }
        
        if (bearerClient) {
          // Use the Bearer token client
          handlers = new Handlers(bearerClient);
        } else {
          // Fall back to session-based auth
          // Use 'default' session as fallback when we can't determine the actual session
          const fallbackSessionId = 'default';
          const client = this.getOrCreateClient(fallbackSessionId);
          if (!client) {
            throw new McpError(
              ErrorCode.InvalidRequest,
              "Not authenticated. Please authenticate using OAuth in the MCP client."
            );
          }
          handlers = new Handlers(client);
        }
      }

      if (!handlers) {
        throw new McpError(
          ErrorCode.InternalError,
          "Handlers not initialized"
        );
      }

      // Handle API requests
      if (request.params.name === "get_record") {
        return handlers.handleGetRecord(request);
      } else if (request.params.name === "get_page") {
        return handlers.handleGetPage(request);
      } else if (request.params.name === "search_documents") {
        return handlers.handleSearchDocuments(request);
      } else if (request.params.name === "create_feature") {
        return handlers.handleCreateFeature(request);
      } else if (request.params.name === "update_feature") {
        return handlers.handleUpdateFeature(request);
      } else if (request.params.name === "delete_feature") {
        return handlers.handleDeleteFeature(request);
      } else if (request.params.name === "list_features") {
        return handlers.handleListFeatures(request);
      } else if (request.params.name === "get_feature_details") {
        return handlers.handleGetFeatureDetails(request);
      } else if (request.params.name === "introspection") {
        return handlers.handleIntrospection(request);
      } else if (request.params.name === "get_idea") {
        return handlers.handleGetIdea(request);
      } else if (request.params.name === "list_ideas") {
        return handlers.handleListIdeas(request);
      } else if (request.params.name === "create_idea") {
        return handlers.handleCreateIdea(request);
      } else if (request.params.name === "update_idea") {
        return handlers.handleUpdateIdea(request);
      } else if (request.params.name === "delete_idea") {
        return handlers.handleDeleteIdea(request);
      } else if (request.params.name === "promote_idea") {
        return handlers.handlePromoteIdea(request);
      }

      throw new McpError(
        ErrorCode.MethodNotFound,
        `Unknown tool: ${request.params.name}`
      );
    });
  }


  async run() {
    const transportType = process.env.TRANSPORT || "stdio";
    const port = parseInt(process.env.PORT || "3000");
    
    if (transportType === "sse") {
      await this.runSSEServer(port);
    } else {
      const transport = new StdioServerTransport();
      await this.server.connect(transport);
      console.error("Aha! MCP server running on stdio");
      console.error(`Authentication mode: ${useOAuth ? "OAuth2" : "API Token"}`);
    }
  }

  private async runSSEServer(port: number) {
    const app = express();
    app.use(cors());
    app.use(express.json({ limit: "100mb" }));
    app.use(express.urlencoded({ extended: true, limit: "100mb" }));

    // Middleware to handle ngrok's browser warning
    app.use((req, res, next) => {
      res.setHeader('ngrok-skip-browser-warning', 'true');
      next();
    });

    const transports = new Map<string, SSEServerTransport>();
    const bearerTokenClients = new Map<string, GraphQLClient>();
    const serverUrl = `http://localhost:${port}`;

    // Get the public URL (ngrok or localhost)
    const publicUrl = OAUTH_REDIRECT_URI ? new URL(OAUTH_REDIRECT_URI).origin : serverUrl;

    // OAuth 2.0 Protected Resource Metadata endpoint (RFC 9728)
    app.get("/.well-known/oauth-protected-resource", (req, res) => {
      // Always use localhost for the resource server
      const resourceUrl = `http://localhost:${port}`;
      const metadata = {
        resource: resourceUrl,
        authorization_servers: [
          // But use ngrok URL for the authorization server
          publicUrl
        ]
      };
      res.setHeader('Content-Type', 'application/json');
      res.json(metadata);
    });

    // Handle MCP Inspector's SSE-specific OAuth discovery
    app.get("/.well-known/oauth-protected-resource/sse", (req, res) => {
      const metadata = {
        resource: `${publicUrl}/sse`,
        authorization_servers: [
          publicUrl
        ]
      };
      res.setHeader('Content-Type', 'application/json');
      res.json(metadata);
    });

    // OAuth 2.0 Authorization Server Metadata endpoint (RFC 8414)
    // We implement this because Aha! doesn't provide discovery endpoints
    app.get("/.well-known/oauth-authorization-server", (_req, res) => {
      const metadata = {
        issuer: publicUrl,
        authorization_endpoint: `${publicUrl}/oauth/authorize`,
        token_endpoint: `${publicUrl}/oauth/token`,
        registration_endpoint: `${publicUrl}/oauth/register`,
        response_types_supported: ["code"],
        grant_types_supported: ["authorization_code"],
        code_challenge_methods_supported: ["S256"],
        token_endpoint_auth_methods_supported: ["client_secret_post", "client_secret_basic", "none"],
        scopes_supported: ["openid", "profile", "email", "read", "write"],
        response_modes_supported: ["query", "fragment"],
        subject_types_supported: ["public"],
        id_token_signing_alg_values_supported: ["RS256"],
        claims_supported: ["sub", "iss", "aud", "exp", "iat"]
      };
      res.setHeader('Content-Type', 'application/json');
      res.json(metadata);
    });

    // Handle path-based discovery (RFC 8414 Section 3.1)
    const pathMatch = publicUrl.match(/^(https?:\/\/[^\/]+)(\/.*)?$/);
    if (pathMatch && pathMatch[2]) {
      const basePath = pathMatch[2];
      app.get(`/.well-known/oauth-authorization-server${basePath}`, (_req, res) => {
        res.redirect('/.well-known/oauth-authorization-server');
      });
    }

    // Handle MCP Inspector's SSE-specific authorization server discovery
    app.get("/.well-known/oauth-authorization-server/sse", (_req, res) => {
      const metadata = {
        issuer: `${publicUrl}/sse`,
        authorization_endpoint: `${publicUrl}/oauth/authorize`,
        token_endpoint: `${publicUrl}/oauth/token`,
        registration_endpoint: `${publicUrl}/oauth/register`,
        response_types_supported: ["code"],
        grant_types_supported: ["authorization_code"],
        code_challenge_methods_supported: ["S256"],
        token_endpoint_auth_methods_supported: ["client_secret_post", "client_secret_basic", "none"],
        scopes_supported: ["openid", "profile", "email", "read", "write"],
        response_modes_supported: ["query", "fragment"],
        subject_types_supported: ["public"],
        id_token_signing_alg_values_supported: ["RS256"],
        claims_supported: ["sub", "iss", "aud", "exp", "iat"]
      };
      res.setHeader('Content-Type', 'application/json');
      res.json(metadata);
    });

    // OpenID Connect Discovery endpoint (for compatibility)
    app.get("/.well-known/openid-configuration", (_req, res) => {
      const metadata = {
        issuer: publicUrl,
        authorization_endpoint: `${publicUrl}/oauth/authorize`,
        token_endpoint: `${publicUrl}/oauth/token`,
        userinfo_endpoint: `${publicUrl}/oauth/userinfo`,
        jwks_uri: `${publicUrl}/oauth/jwks`,
        response_types_supported: ["code"],
        grant_types_supported: ["authorization_code"],
        code_challenge_methods_supported: ["S256"],
        token_endpoint_auth_methods_supported: ["client_secret_post", "client_secret_basic"],
        scopes_supported: ["openid", "profile", "email", "read", "write"],
        response_modes_supported: ["query", "fragment"],
        subject_types_supported: ["public"],
        id_token_signing_alg_values_supported: ["RS256"],
        claims_supported: ["sub", "iss", "aud", "exp", "iat"]
      };
      res.setHeader('Content-Type', 'application/json');
      res.json(metadata);
    });

    // OAuth endpoints when acting as authorization server
    if (useOAuth && this.oauthHandler) {
      // Dynamic Client Registration endpoint (RFC 7591)
      app.post("/oauth/register", (req, res) => {
        const { client_name, redirect_uris, grant_types, response_types } = req.body;
        
        // Generate a client ID for this registration
        const clientId = `mcp_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
        
        // Store registration (in production, this would be persisted)
        const registration = {
          client_id: clientId,
          client_secret: "not_required_for_public_clients",
          client_name: client_name || "MCP Inspector",
          redirect_uris: redirect_uris || [`${publicUrl}/oauth/callback`],
          grant_types: grant_types || ["authorization_code"],
          response_types: response_types || ["code"],
          token_endpoint_auth_method: "none",
          client_id_issued_at: Math.floor(Date.now() / 1000)
        };
        
        res.json(registration);
      });

      // OAuth callback endpoint
      app.get("/oauth/callback", async (req, res) => {
        const { code, state, error } = req.query;
        
        console.error("OAuth callback received:", {
          code: !!code,
          state,
          error,
          fullUrl: req.originalUrl
        });
        
        // If there's an error from Aha!
        if (error) {
          return res.status(400).json({ error: error as string });
        }
        
        // Check if this is from the Inspector
        const stateMap = (global as any).oauthStateMap;
        if (state && stateMap && stateMap.has(state as string)) {
          const { originalRedirectUri } = stateMap.get(state as string);
          stateMap.delete(state as string);
          
          // Redirect back to Inspector with the code
          const inspectorUrl = new URL(originalRedirectUri);
          inspectorUrl.searchParams.set("code", code as string);
          inspectorUrl.searchParams.set("state", state as string);
          
          return res.redirect(inspectorUrl.toString());
        }
        
        // For Inspector without state (which seems to be the case)
        if (code && !state) {
          // This is likely from the Inspector, but we don't have the original redirect URI
          // Return a simple success page with the code
          return res.send(`
            <html>
              <body>
                <h2>Authorization Code Received</h2>
                <p>Code: <code>${code}</code></p>
                <p>Copy this code and paste it in the MCP Inspector.</p>
              </body>
            </html>
          `);
        }
        
        // Otherwise handle normally for our auth tools
        await this.oauthHandler!.handleCallback(req, res);
      });

      // OAuth authorize endpoint - redirects to Aha!
      app.get("/oauth/authorize", (req, res) => {
        const { client_id, redirect_uri, response_type, state, code_challenge, code_challenge_method, subdomain } = req.query;
        
        console.error("Incoming OAuth authorize request:", {
          client_id,
          redirect_uri,
          response_type,
          state,
          subdomain,
          fullUrl: req.originalUrl
        });
        
        // Generate state if not provided
        const stateParam = state || crypto.randomBytes(16).toString('hex');
        
        // Store the original redirect_uri and state for later
        if (redirect_uri) {
          // Store mapping from state to original redirect_uri
          (global as any).oauthStateMap = (global as any).oauthStateMap || new Map();
          (global as any).oauthStateMap.set(stateParam as string, {
            originalRedirectUri: redirect_uri as string,
            originalState: state as string || null,
            codeChallenge: code_challenge as string
          });
        }
        
        // Use subdomain if provided, otherwise use the one from config or default to secure
        const ahaSubdomain = subdomain || AHA_DOMAIN || 'secure';
        
        // Build Aha! authorization URL
        const ahaAuthUrl = new URL(`https://${ahaSubdomain}.aha.io/oauth/authorize`);
        
        // Check for required parameters
        if (!OAUTH_CLIENT_ID || !OAUTH_REDIRECT_URI) {
          console.error("Missing OAuth configuration:", { 
            clientId: !!OAUTH_CLIENT_ID, 
            redirectUri: !!OAUTH_REDIRECT_URI 
          });
          return res.status(500).json({ error: "OAuth not properly configured" });
        }
        
        // Always use our registered Aha! client credentials
        ahaAuthUrl.searchParams.set("client_id", OAUTH_CLIENT_ID);
        // Always use our registered redirect URI
        ahaAuthUrl.searchParams.set("redirect_uri", OAUTH_REDIRECT_URI);
        // Use authorization code flow as requested by Inspector
        ahaAuthUrl.searchParams.set("response_type", response_type as string || "code");
        // Always include state for security
        ahaAuthUrl.searchParams.set("state", stateParam as string);
        // Note: Aha! doesn't support PKCE, so we don't send code_challenge/code_challenge_method
        
        console.error("OAuth authorize redirect:", {
          clientId: OAUTH_CLIENT_ID,
          redirectUri: OAUTH_REDIRECT_URI,
          subdomain: ahaSubdomain,
          url: ahaAuthUrl.toString()
        });
        
        // Redirect to Aha!
        res.redirect(ahaAuthUrl.toString());
      });

      // OAuth token endpoint - proxies to Aha!
      app.post("/oauth/token", async (req, res) => {
        try {
          console.error("Token exchange request:", {
            headers: req.headers,
            body: req.body,
            query: req.query
          });
          
          const { code, client_id, client_secret, grant_type, redirect_uri, code_verifier, subdomain } = req.body;
          
          // Use subdomain if provided, otherwise use the one from config
          const ahaSubdomain = subdomain || AHA_DOMAIN || 'secure';
          
          // Validate required parameters
          if (!code || !grant_type) {
            return res.status(400).json({ 
              error: "invalid_request",
              error_description: "Missing required parameters: code and grant_type" 
            });
          }
          
          // Exchange code with Aha!
          const tokenUrl = `https://${ahaSubdomain}.aha.io/oauth/token`;
          const params = new URLSearchParams({
            code,
            client_id: OAUTH_CLIENT_ID || "",
            client_secret: OAUTH_CLIENT_SECRET || "",
            grant_type,
            redirect_uri: OAUTH_REDIRECT_URI || "",
          });
          
          // Note: Aha! doesn't support PKCE, so we don't send code_verifier
          
          const response = await fetch(tokenUrl, {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: params,
          });
          
          const data = await response.json();
          res.json(data);
        } catch (error) {
          console.error("Token exchange error:", error);
          res.status(500).json({ error: "Token exchange failed" });
        }
      });
    }

    // Handle SSE connections
    app.get("/sse", async (req, res) => {
      const transport = new SSEServerTransport("/message", res);
      console.error(`New SSE connection, sessionId: ${transport.sessionId}`);
      
      // Add ngrok-skip-browser-warning header support
      res.setHeader('ngrok-skip-browser-warning', 'true');
      
      transports.set(transport.sessionId, transport);
      
      transport.onclose = () => {
        console.error(`SSE connection closed`);
        transports.delete(transport.sessionId);
        bearerTokenClients.delete(transport.sessionId);
      };
      
      // Store reference to bearer token clients
      (transport as any)._bearerTokenClients = bearerTokenClients;
      
      // connect() automatically calls start() on the transport
      await this.server.connect(transport);
    });

    // Handle message posting
    app.post("/message", async (req, res) => {
      const sessionId = req.query.sessionId as string;
      const transport = transports.get(sessionId);
      
      if (!transport) {
        return res.status(404).json({ error: "Session not found" });
      }
      
      // Store session ID in transport for tool handlers
      (transport as any)._sessionId = sessionId;
      
      // Check for Bearer token authentication
      const authHeader = req.headers.authorization;
      if (authHeader && authHeader.startsWith('Bearer ')) {
        const token = authHeader.substring(7);
        
        // For now, we'll accept any valid-looking Bearer token
        // In production, you'd validate this token against stored tokens
        console.error("Received Bearer token:", token.substring(0, 10) + "...");
        
        // Create a client with the token for this session
        // We'll use the default subdomain from config
        const client = new GraphQLClient(
          `https://${AHA_DOMAIN || 'secure'}.aha.io/api/v2/graphql`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        
        // Store client for this session
        bearerTokenClients.set(sessionId, client);
        // Also store globally for access in tool handlers
        (global as any).bearerTokenClients = bearerTokenClients;
        console.error(`Stored Bearer token for session: ${sessionId}`);
      }
      
      try {
        await transport.handlePostMessage(req, res, req.body);
      } catch (error) {
        console.error("Error handling message:", error);
        res.status(500).json({ error: "Internal server error" });
      }
    });

    // Health check endpoint
    app.get("/health", (_req, res) => {
      res.json({ 
        status: "healthy", 
        activeConnections: transports.size,
        timestamp: new Date().toISOString()
      });
    });

    app.listen(port, () => {
      console.error(`Aha! MCP server running on SSE at http://localhost:${port}/sse`);
      console.error(`Health check available at http://localhost:${port}/health`);
      if (useOAuth) {
        console.error(`OAuth callback URL: http://localhost:${port}/oauth/callback`);
        console.error(`Authentication mode: OAuth2`);
      } else {
        console.error(`Authentication mode: API Token`);
      }
    });
  }
}

const server = new AhaMcp();
server.run().catch(console.error);
