import { ErrorCode, McpError } from "@modelcontextprotocol/sdk/types.js";
import { GraphQLClient } from "graphql-request";
import {
  FEATURE_REF_REGEX,
  REQUIREMENT_REF_REGEX,
  NOTE_REF_REGEX,
  Record,
  FeatureResponse,
  RequirementResponse,
  PageResponse,
  SearchResponse,
  CreateFeatureResponse,
  UpdateFeatureResponse,
  DeleteFeatureResponse,
  ListFeaturesResponse,
  GetFeatureDetailsResponse,
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
  introspectionQuery,
  simpleIntrospectionQuery,
  queryTypeIntrospectionQuery,
  mutationTypeIntrospectionQuery,
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
      let result: Record | undefined;

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
      } else {
        throw new McpError(
          ErrorCode.InvalidParams,
          "Invalid reference number format. Expected DEVELOP-123 or ADT-123-1"
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
    const { queryType = "full" } = request.params.arguments as {
      queryType?: "full" | "simple" | "query" | "mutation";
    };

    try {
      let query: string;
      switch (queryType) {
        case "simple":
          query = simpleIntrospectionQuery;
          break;
        case "query":
          query = queryTypeIntrospectionQuery;
          break;
        case "mutation":
          query = mutationTypeIntrospectionQuery;
          break;
        case "full":
        default:
          query = introspectionQuery;
          break;
      }

      const data = await this.client.request(query);

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(data, null, 2),
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
}
