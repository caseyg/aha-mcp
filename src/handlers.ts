import { ErrorCode, McpError } from "@modelcontextprotocol/sdk/types.js";
import { GraphQLClient } from "graphql-request";
import {
  FEATURE_REF_REGEX,
  REQUIREMENT_REF_REGEX,
  NOTE_REF_REGEX,
  IDEA_REF_REGEX,
  FeatureResponse,
  RequirementResponse,
  PageResponse,
  SearchResponse,
  CreateFeatureResponse,
  UpdateFeatureResponse,
  DeleteFeatureResponse,
  ListFeaturesResponse,
  GetFeatureDetailsResponse,
  IdeaResponse,
  CreateIdeaResponse,
  UpdateIdeaResponse,
  DeleteIdeaResponse,
  ListIdeasResponse,
  PromoteIdeaResponse,
} from "./types.js";
import {
  getFeatureQuery,
  getRequirementQuery,
  getPageQuery,
  searchDocumentsQuery,
  createFeatureQuery,
  updateFeatureQuery,
  deleteFeatureQuery,
  listFeaturesQuery,
  getFeatureDetailsQuery,
  getIdeaQuery,
  createIdeaQuery,
  updateIdeaQuery,
  deleteIdeaQuery,
  listIdeasQuery,
  promoteIdeaQuery,
  introspectionQuery,
  simpleIntrospectionQuery,
  listTypesQuery,
  queryTypeIntrospectionQuery,
  mutationTypeIntrospectionQuery,
  typeIntrospectionQuery,
  searchQueriesIntrospectionQuery,
  searchMutationsIntrospectionQuery,
} from "./queries.js";

export class Handlers {
  constructor(private client: GraphQLClient) {}

  async handleGetRecord(request: any) {
    const { reference } = request.params.arguments as { reference: string };

    if (!reference) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Reference number is required"
      );
    }

    try {
      let result: any;

      if (FEATURE_REF_REGEX.test(reference)) {
        const data = await this.client.request<FeatureResponse>(
          getFeatureQuery,
          {
            id: reference,
          }
        );
        result = data.feature;
      } else if (REQUIREMENT_REF_REGEX.test(reference)) {
        const data = await this.client.request<RequirementResponse>(
          getRequirementQuery,
          { id: reference }
        );
        result = data.requirement;
      } else if (IDEA_REF_REGEX.test(reference)) {
        const data = await this.client.request<IdeaResponse>(
          getIdeaQuery,
          { id: reference }
        );
        result = data.idea;
      } else {
        throw new McpError(
          ErrorCode.InvalidParams,
          "Invalid reference number format. Expected DEVELOP-123, ADT-123-1, or ABC-I-123"
        );
      }

      if (!result) {
        return {
          content: [
            {
              type: "text",
              text: `No record found for reference ${reference}`,
            },
          ],
        };
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(result, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to fetch record: ${errorMessage}`
      );
    }
  }

  async handleGetPage(request: any) {
    const { reference, includeParent = false } = request.params.arguments as {
      reference: string;
      includeParent?: boolean;
    };

    if (!reference) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Reference number is required"
      );
    }

    if (!NOTE_REF_REGEX.test(reference)) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Invalid reference number format. Expected ABC-N-213"
      );
    }

    try {
      const data = await this.client.request<PageResponse>(getPageQuery, {
        id: reference,
        includeParent,
      });

      if (!data.note) {
        return {
          content: [
            {
              type: "text",
              text: `No page found for reference ${reference}`,
            },
          ],
        };
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.note, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to fetch page: ${errorMessage}`
      );
    }
  }

  async handleSearchDocuments(request: any) {
    const { query, searchableType = "Page" } = request.params.arguments as {
      query: string;
      searchableType?: string;
    };

    if (!query) {
      throw new McpError(ErrorCode.InvalidParams, "Search query is required");
    }

    try {
      const data = await this.client.request<SearchResponse>(
        searchDocumentsQuery,
        {
          query,
          searchableType: [searchableType],
        }
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.searchDocuments, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to search documents: ${errorMessage}`
      );
    }
  }

  async handleCreateFeature(request: any) {
    const {
      releaseId,
      name,
      description,
      assignedToUserId,
      tags,
      workflowStatusId,
      epicId,
      teamId,
    } = request.params.arguments;

    if (!name) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Feature name is required"
      );
    }

    try {
      // Build attributes object
      const attributes: any = {
        name,
      };

      if (description) attributes.description = description;
      if (tags) attributes.tagList = tags.join(", ");
      
      // Handle relationships
      if (releaseId) {
        attributes.release = { id: releaseId };
      }
      if (workflowStatusId) {
        attributes.workflowStatus = { id: workflowStatusId };
      }
      if (assignedToUserId) {
        attributes.assignedToUser = { id: assignedToUserId };
      }
      if (epicId) {
        attributes.epic = { id: epicId };
      }
      if (teamId) {
        attributes.team = { id: teamId };
      }

      const data = await this.client.request<CreateFeatureResponse>(
        createFeatureQuery,
        {
          attributes,
        }
      );

      // Check for errors
      if (data.createFeature.errors && data.createFeature.errors.length > 0) {
        const errorMessages = data.createFeature.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to create feature: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.createFeature.feature, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to create feature: ${errorMessage}`
      );
    }
  }

  async handleUpdateFeature(request: any) {
    const {
      id,
      name,
      description,
      workflowStatusId,
      assignedToUserId,
      tags,
    } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Feature ID is required"
      );
    }

    try {
      // Build attributes object
      const attributes: any = {};

      if (name !== undefined) attributes.name = name;
      if (description !== undefined) attributes.description = description;
      if (tags !== undefined) attributes.tagList = tags.join(", ");
      
      // Handle relationships
      if (workflowStatusId !== undefined) {
        attributes.workflowStatus = { id: workflowStatusId };
      }
      if (assignedToUserId !== undefined) {
        attributes.assignedToUser = { id: assignedToUserId };
      }

      const data = await this.client.request<UpdateFeatureResponse>(
        updateFeatureQuery,
        {
          id,
          attributes,
        }
      );

      // Check for errors
      if (data.updateFeature.errors && data.updateFeature.errors.length > 0) {
        const errorMessages = data.updateFeature.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to update feature: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.updateFeature.feature, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to update feature: ${errorMessage}`
      );
    }
  }

  async handleDeleteFeature(request: any) {
    const { id } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Feature ID is required"
      );
    }

    try {
      const data = await this.client.request<DeleteFeatureResponse>(
        deleteFeatureQuery,
        { id }
      );

      // Check for errors
      if (data.deleteFeature.errors && data.deleteFeature.errors.length > 0) {
        const errorMessages = data.deleteFeature.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to delete feature: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({ success: true, id }, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to delete feature: ${errorMessage}`
      );
    }
  }

  async handleListFeatures(request: any) {
    const {
      releaseId,
      epicId,
      productId,
      goalId,
      initiativeId,
      teamId,
      assignedToUserId,
      page,
      perPage,
    } = request.params.arguments;

    // Check if at least one required filter is provided
    if (!releaseId && !productId && !epicId) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "At least one filter is required: releaseId, productId, or epicId"
      );
    }

    try {
      // Build filters object
      const filters: any = {};
      
      if (releaseId) filters.releaseId = releaseId;
      if (epicId) filters.epicId = epicId;
      if (productId) filters.projectId = productId; // Note: API uses projectId
      if (teamId) filters.teamId = teamId;
      if (assignedToUserId) filters.assignedToUserId = assignedToUserId;
      
      // Note: goalId and initiativeId filtering might need to be done differently
      // as they're not part of FeatureFilters in the schema

      const data = await this.client.request<ListFeaturesResponse>(
        listFeaturesQuery,
        {
          filters,
          page: page || 1,
          per: perPage || 20,
        }
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.features, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to list features: ${errorMessage}`
      );
    }
  }

  async handleGetFeatureDetails(request: any) {
    const { id } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Feature ID is required"
      );
    }

    try {
      const data = await this.client.request<GetFeatureDetailsResponse>(
        getFeatureDetailsQuery,
        { id }
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.feature, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to get feature details: ${errorMessage}`
      );
    }
  }

  async handleIntrospection(request: any) {
    const { queryType = "list-types", typeName, searchTerm, maxResults = 50 } = request.params.arguments as {
      queryType?: "full" | "simple" | "query" | "mutation" | "type" | "search-queries" | "search-mutations" | "list-types";
      typeName?: string;
      searchTerm?: string;
      maxResults?: number;
    };

    try {
      let query: string;
      let filterResults = false;
      
      switch (queryType) {
        case "list-types":
        case "simple":
          query = simpleIntrospectionQuery;
          filterResults = true; // Apply filtering to reduce size
          break;
        case "query":
          query = queryTypeIntrospectionQuery;
          filterResults = true;
          break;
        case "mutation":
          query = mutationTypeIntrospectionQuery;
          filterResults = true;
          break;
        case "type":
          if (!typeName) {
            throw new McpError(
              ErrorCode.InvalidParams,
              "typeName is required when queryType is 'type'"
            );
          }
          query = typeIntrospectionQuery(typeName);
          break;
        case "search-queries":
          query = searchQueriesIntrospectionQuery(searchTerm || "");
          filterResults = true;
          break;
        case "search-mutations":
          query = searchMutationsIntrospectionQuery(searchTerm || "");
          filterResults = true;
          break;
        case "full":
          throw new McpError(
            ErrorCode.InvalidParams,
            "Full introspection is not supported due to response size limits. Please use 'list-types' to see available types, then 'type' to explore specific types."
          );
        default:
          query = simpleIntrospectionQuery;
          filterResults = true;
          break;
      }

      const data = await this.client.request<any>(query);

      // Prepare pagination metadata
      let paginationInfo: any = null;
      
      // Filter and limit results
      if (filterResults) {
        const searchLower = searchTerm?.toLowerCase() || "";
        
        // Filter types list
        if ((queryType === "list-types" || queryType === "simple") && data.__schema?.types) {
          let types = data.__schema.types;
          const originalCount = types.length;
          
          // Filter out internal types unless searching for them
          if (!searchTerm || !searchTerm.startsWith("__")) {
            types = types.filter((type: any) => !type.name.startsWith("__"));
          }
          
          // Apply search filter
          if (searchTerm) {
            types = types.filter((type: any) => 
              type.name.toLowerCase().includes(searchLower)
            );
          }
          
          const filteredCount = types.length;
          
          // Sort and limit
          types.sort((a: any, b: any) => a.name.localeCompare(b.name));
          const hasMore = types.length > maxResults;
          data.__schema.types = types.slice(0, maxResults);
          
          // Add pagination info
          paginationInfo = {
            totalCount: originalCount,
            filteredCount: filteredCount,
            returnedCount: data.__schema.types.length,
            hasMore: hasMore,
            maxResults: maxResults
          };
        }
        
        // Filter queries
        else if ((queryType === "query" || queryType === "search-queries") && data.__schema?.queryType?.fields) {
          let fields = data.__schema.queryType.fields;
          const originalCount = fields.length;
          
          if (searchTerm) {
            fields = fields.filter(
              (field: any) => 
                field.name.toLowerCase().includes(searchLower) ||
                (field.description && field.description.toLowerCase().includes(searchLower))
            );
          }
          
          const filteredCount = fields.length;
          
          fields.sort((a: any, b: any) => a.name.localeCompare(b.name));
          const hasMore = fields.length > maxResults;
          data.__schema.queryType.fields = fields.slice(0, maxResults);
          
          // Add pagination info
          paginationInfo = {
            totalCount: originalCount,
            filteredCount: filteredCount,
            returnedCount: data.__schema.queryType.fields.length,
            hasMore: hasMore,
            maxResults: maxResults
          };
        }
        
        // Filter mutations
        else if ((queryType === "mutation" || queryType === "search-mutations") && data.__schema?.mutationType?.fields) {
          let fields = data.__schema.mutationType.fields;
          const originalCount = fields.length;
          
          if (searchTerm) {
            fields = fields.filter(
              (field: any) => 
                field.name.toLowerCase().includes(searchLower) ||
                (field.description && field.description.toLowerCase().includes(searchLower))
            );
          }
          
          const filteredCount = fields.length;
          
          fields.sort((a: any, b: any) => a.name.localeCompare(b.name));
          const hasMore = fields.length > maxResults;
          data.__schema.mutationType.fields = fields.slice(0, maxResults);
          
          // Add pagination info
          paginationInfo = {
            totalCount: originalCount,
            filteredCount: filteredCount,
            returnedCount: data.__schema.mutationType.fields.length,
            hasMore: hasMore,
            maxResults: maxResults
          };
        }
      }
      
      // Wrap response with pagination metadata if available
      const response = paginationInfo ? {
        data: data,
        pagination: paginationInfo
      } : data;

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(response, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      
      // Check if introspection is disabled
      if (errorMessage.includes("introspection") || errorMessage.includes("__schema")) {
        throw new McpError(
          ErrorCode.InternalError,
          "GraphQL introspection appears to be disabled on this API. This is a common security practice for production APIs."
        );
      }

      console.error("Introspection Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to perform introspection: ${errorMessage}`
      );
    }
  }

  async handleGetIdea(request: any) {
    const { id } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Idea ID or reference number is required"
      );
    }

    try {
      const data = await this.client.request<IdeaResponse>(
        getIdeaQuery,
        { id }
      );

      if (!data.idea) {
        return {
          content: [
            {
              type: "text",
              text: `No idea found for ID ${id}`,
            },
          ],
        };
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.idea, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to fetch idea: ${errorMessage}`
      );
    }
  }

  async handleListIdeas(request: any) {
    const {
      projectId,
      assignedToUserId,
      visibility,
      promoted,
      page,
      perPage,
    } = request.params.arguments;

    if (!projectId) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "projectId is required to list ideas"
      );
    }

    try {
      // Build filters object
      const filters: any = {
        projectId,
      };

      if (assignedToUserId) filters.assignedToUserId = assignedToUserId;
      if (visibility) filters.visibility = visibility;
      if (promoted !== undefined) filters.promoted = promoted;

      const data = await this.client.request<ListIdeasResponse>(
        listIdeasQuery,
        {
          filters,
          page: page || 1,
          per: perPage || 20,
        }
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.ideas, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to list ideas: ${errorMessage}`
      );
    }
  }

  async handleCreateIdea(request: any) {
    const {
      projectId,
      name,
      description,
      visibility,
      assignedToUserId,
    } = request.params.arguments;

    if (!projectId || !name) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "projectId and name are required"
      );
    }

    try {
      // Build attributes object
      const attributes: any = {
        name,
        project: { id: projectId },
      };

      if (description) attributes.description = description;
      if (visibility) attributes.visibility = visibility;
      if (assignedToUserId) {
        attributes.assignedToUser = { id: assignedToUserId };
      }

      const data = await this.client.request<CreateIdeaResponse>(
        createIdeaQuery,
        {
          attributes,
        }
      );

      // Check for errors
      if (data.createIdea.errors && data.createIdea.errors.length > 0) {
        const errorMessages = data.createIdea.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to create idea: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.createIdea.idea, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to create idea: ${errorMessage}`
      );
    }
  }

  async handleUpdateIdea(request: any) {
    const {
      id,
      name,
      description,
      visibility,
      assignedToUserId,
    } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Idea ID is required"
      );
    }

    try {
      // Build attributes object
      const attributes: any = {};

      if (name !== undefined) attributes.name = name;
      if (description !== undefined) attributes.description = description;
      if (visibility !== undefined) attributes.visibility = visibility;
      if (assignedToUserId !== undefined) {
        attributes.assignedToUser = { id: assignedToUserId };
      }

      const data = await this.client.request<UpdateIdeaResponse>(
        updateIdeaQuery,
        {
          id,
          attributes,
        }
      );

      // Check for errors
      if (data.updateIdea.errors && data.updateIdea.errors.length > 0) {
        const errorMessages = data.updateIdea.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to update idea: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data.updateIdea.idea, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to update idea: ${errorMessage}`
      );
    }
  }

  async handleDeleteIdea(request: any) {
    const { id } = request.params.arguments;

    if (!id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Idea ID is required"
      );
    }

    try {
      const data = await this.client.request<DeleteIdeaResponse>(
        deleteIdeaQuery,
        { id }
      );

      // Check for errors
      if (data.deleteIdea.errors && data.deleteIdea.errors.length > 0) {
        const errorMessages = data.deleteIdea.errors
          .map((e: any) => `${e.attribute}: ${e.message}`)
          .join(", ");
        throw new McpError(
          ErrorCode.InvalidParams,
          `Failed to delete idea: ${errorMessages}`
        );
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({ success: true, id }, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to delete idea: ${errorMessage}`
      );
    }
  }

  async handlePromoteIdea(request: any) {
    const { id, type, projectId, releaseId, featureId } = request.params.arguments;

    if (!id || !type) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "Idea ID and promotion type are required"
      );
    }

    // Validate required parameters based on promotion type
    if (type.toLowerCase() === 'feature' && !releaseId && !projectId) {
      throw new McpError(
        ErrorCode.InvalidParams,
        "When promoting to Feature, either releaseId or projectId is required"
      );
    }

    // Convert to proper enum values (capitalized)
    const typeMap: { [key: string]: string } = {
      'feature': 'Feature',
      'epic': 'Epic',
      'requirement': 'Requirement'
    };
    
    const promotionType = typeMap[type.toLowerCase()];
    if (!promotionType) {
      throw new McpError(
        ErrorCode.InvalidParams,
        `Invalid promotion type: "${type}". Must be one of: feature, epic, requirement`
      );
    }

    try {
      const data = await this.client.request<PromoteIdeaResponse>(
        promoteIdeaQuery,
        {
          id,
          type: promotionType,
          projectId,
          releaseId,
          featureId,
        }
      );

      // The mutation returns the idea if successful
      const idea = data.promoteIdea.idea;

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({
              success: true,
              message: `Successfully promoted idea ${id} to ${type.toLowerCase()}`,
              idea: {
                id: idea.id,
                referenceNum: idea.referenceNum
              }
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      if (error instanceof McpError) {
        throw error;
      }

      const errorMessage =
        error instanceof Error ? error.message : String(error);
      console.error("API Error:", errorMessage);
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to promote idea: ${errorMessage}`
      );
    }
  }
}
