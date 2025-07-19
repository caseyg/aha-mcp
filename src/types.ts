export interface Description {
  htmlBody: string;
  markdownBody?: string;
}

export interface Record {
  name: string;
  description: Description;
}

export interface FeatureResponse {
  feature: Record;
}

export interface RequirementResponse {
  requirement: Record;
}

export interface PageResponse {
  note: {
    referenceNum: string;
    name: string;
    description: {
      htmlBody: string;
    };
    children: Array<{
      name: string;
      referenceNum: string;
    }>;
    parent?: {
      name: string;
      referenceNum: string;
    };
  };
}

// Regular expressions for validating reference numbers
export const FEATURE_REF_REGEX = /^([A-Z][A-Z0-9]*)-(\d+)$/;
export const REQUIREMENT_REF_REGEX = /^([A-Z][A-Z0-9]*)-(\d+)-(\d+)$/;
export const NOTE_REF_REGEX = /^([A-Z][A-Z0-9]*)-N-(\d+)$/;
export const IDEA_REF_REGEX = /^([A-Z][A-Z0-9]*)-I-(\d+)$/;

export interface SearchNode {
  name: string | null;
  url: string;
  searchableId: string;
  searchableType: string;
}

export interface SearchResponse {
  searchDocuments: {
    nodes: SearchNode[];
    currentPage: number;
    totalCount: number;
    totalPages: number;
    isLastPage: boolean;
  };
}

export interface WorkflowStatus {
  id: string;
  name: string;
}

export interface User {
  id: string;
  name: string;
  email?: string;
}

export interface Tag {
  id: string;
  name: string;
}

export interface Release {
  id: string;
  referenceNum: string;
  name: string;
}

export interface Epic {
  id: string;
  referenceNum: string;
  name: string;
}

export interface Goal {
  id: string;
  referenceNum: string;
  name: string;
}

export interface Feature {
  id: string;
  referenceNum: string;
  name: string;
  description?: {
    htmlBody: string;
  };
  workflowStatus?: WorkflowStatus;
  release?: Release;
  epic?: Epic;
  assignedToUser?: User;
  tags?: Tag[];
  startDate?: string;
  dueDate?: string;
  score?: number;
  progress?: number;
  createdAt?: string;
  updatedAt?: string;
  goals?: Goal[];
  watchers?: User[];
  customFieldValues?: Array<{
    id: string;
    value: any;
    customField: {
      id: string;
      name: string;
      apiKey: string;
    };
  }>;
}

export interface CreateFeatureResponse {
  createFeature: {
    feature: Feature;
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface UpdateFeatureResponse {
  updateFeature: {
    feature: Feature;
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface DeleteFeatureResponse {
  deleteFeature: {
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface ListFeaturesResponse {
  features: {
    nodes: Feature[];
    currentPage: number;
    totalCount: number;
    totalPages: number;
  };
}

export interface GetFeatureDetailsResponse {
  feature: Feature;
}

export interface Portal {
  id: string;
  name: string;
}

export interface Idea {
  id: string;
  referenceNum: string;
  name: string;
  description?: {
    htmlBody: string;
  };
  visibility?: string;
  score?: number;
  createdAt?: string;
  updatedAt?: string;
  promotedAt?: string;
  portal?: Portal;
  assignedToUser?: User;
}

export interface IdeaResponse {
  idea: Idea;
}

export interface CreateIdeaResponse {
  createIdea: {
    idea: Idea;
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface UpdateIdeaResponse {
  updateIdea: {
    idea: Idea;
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface DeleteIdeaResponse {
  deleteIdea: {
    errors: Array<{
      message: string;
      attribute: string;
    }>;
  };
}

export interface ListIdeasResponse {
  ideas: {
    nodes: Idea[];
    currentPage: number;
    totalCount: number;
    totalPages: number;
  };
}

export interface PromoteIdeaResponse {
  promoteIdea: {
    idea: {
      id: string;
      referenceNum: string;
    };
  };
}
