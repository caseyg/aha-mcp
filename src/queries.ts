export const getPageQuery = `
  query GetPage($id: ID!, $includeParent: Boolean!) {
    note(id: $id) {
      referenceNum
      name
      description {
        htmlBody
      }
      children {
        name
        referenceNum
      }
      parent @include(if: $includeParent) {
        name
        referenceNum
      }
    }
  }
`;

export const getFeatureQuery = `
  query GetFeature($id: ID!) {
    feature(id: $id) {
      referenceNum
      name
      description {
        htmlBody
      }
    }
  }
`;

export const getRequirementQuery = `
  query GetRequirement($id: ID!) {
    requirement(id: $id) {
      referenceNum
      name
      description {
        htmlBody
      }
    }
  }
`;

export const searchDocumentsQuery = `
  query SearchDocuments($query: String!, $searchableType: [String!]!) {
    searchDocuments(filters: {query: $query, searchableType: $searchableType}) {
      nodes {
        name
        url
        searchableId
        searchableType
      }
      currentPage
      totalCount
      totalPages
      isLastPage
    }
  }
`;

export const createFeatureQuery = `
  mutation CreateFeature($attributes: FeatureAttributes!) {
    createFeature(attributes: $attributes) {
      feature {
        id
        referenceNum
        name
        description {
          htmlBody
        }
        workflowStatus {
          id
          name
        }
        assignedToUser {
          id
          name
        }
        tags {
          id
          name
        }
        release {
          id
          referenceNum
          name
        }
      }
      errors {
        message
        attribute
      }
    }
  }
`;

export const updateFeatureQuery = `
  mutation UpdateFeature($id: ID!, $attributes: FeatureAttributes!) {
    updateFeature(id: $id, attributes: $attributes) {
      feature {
        id
        referenceNum
        name
        description {
          htmlBody
        }
        workflowStatus {
          id
          name
        }
        assignedToUser {
          id
          name
        }
        tags {
          id
          name
        }
      }
      errors {
        message
        attribute
      }
    }
  }
`;

export const deleteFeatureQuery = `
  mutation DeleteFeature($id: ID!) {
    deleteFeature(id: $id) {
      errors {
        message
        attribute
      }
    }
  }
`;

export const listFeaturesQuery = `
  query ListFeatures($filters: FeatureFilters!, $page: Int = 1, $per: Int = 20) {
    features(filters: $filters, page: $page, per: $per) {
      nodes {
        id
        referenceNum
        name
        description {
          htmlBody
        }
        workflowStatus {
          id
          name
        }
        release {
          id
          referenceNum
          name
        }
        epic {
          id
          referenceNum
          name
        }
        assignedToUser {
          id
          name
        }
        tags {
          id
          name
        }
      }
      currentPage
      totalCount
      totalPages
    }
  }
`;

export const getFeatureDetailsQuery = `
  query GetFeatureDetails($id: ID!) {
    feature(id: $id) {
      id
      referenceNum
      name
      description {
        htmlBody
      }
      workflowStatus {
        id
        name
      }
      release {
        id
        referenceNum
        name
      }
      epic {
        id
        referenceNum
        name
      }
      assignedToUser {
        id
        name
        email
      }
      tags {
        id
        name
      }
      startDate
      dueDate
      score
      progress
      createdAt
      updatedAt
      goals {
        id
        name
        referenceNum
      }
      watchers {
        id
        name
        email
      }
      customFieldValues {
        id
        value
        customField {
          id
          name
          apiKey
        }
      }
    }
  }
`;

// Import introspection queries
export { 
  introspectionQuery, 
  simpleIntrospectionQuery, 
  queryTypeIntrospectionQuery,
  mutationTypeIntrospectionQuery 
} from './introspectionQuery.js';
