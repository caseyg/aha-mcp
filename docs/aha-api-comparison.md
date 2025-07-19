# Aha! GraphQL vs REST API Comparison

## GraphQL API Overview

The Aha! GraphQL API provides a modern, flexible approach with:
- **307 object types** covering all aspects of product management
- **106 query operations** for data retrieval
- **108 mutation operations** for data modification
- **65 enums** and **127 input types** for type safety
- **31 interfaces** for shared behavior patterns

### Major Object Types

**Core Product Management Objects:**
- `Feature` - Main work items
- `Epic` - Groups of features
- `Initiative` - Strategic projects
- `Goal` - Strategic objectives
- `Release` - Product releases
- `Requirement` - Feature requirements
- `Task` - Work tasks
- `Idea` - Product ideas
- `IdeaTheme` - Groups of ideas

**Planning & Organization:**
- `Project` - Product/project containers
- `Iteration` - Sprint/iteration management
- `ProgramIncrement` - PI planning
- `Workflow` / `WorkflowStatus` - Workflow management
- `Bookmark` - Various visualization bookmarks (boards, charts, etc.)

**Documentation & Knowledge:**
- `Page` - Documentation pages
- `Note` / `NoteTemplate` - Notes and templates
- `KnowledgeBase` - Knowledge management
- `Whiteboard` - Visual collaboration

**Discovery & Research:**
- `DiscoveryInterview` - User interviews
- `DiscoveryScript` - Research scripts
- `DiscoveryStudy` - Research studies
- `Persona` - User personas
- `Competitor` - Competitive analysis

**User & Permissions:**
- `User` - System users
- `Account` - Account management
- `ResourcePermissions` - Access control
- `UserRestrictionOverride` - Permission overrides

### Query Operations

The API provides **106 query operations** for fetching data, including:

**Record Queries (singular & plural):**
- `feature` / `features`
- `epic` / `epics`
- `initiative` / `initiatives`
- `goal` / `goals`
- `release` / `releases`
- `requirement` / `requirements`
- `idea` / `ideas`
- `task` / `tasks`

**Specialized Queries:**
- `searchDocuments` - Search across documents
- `workRecords` - Work item queries
- `recordEvents` - Activity tracking
- Various bookmark queries for different views

### Mutation Operations

The API provides **108 mutation operations** for data modification:

**Create Operations:**
- `createFeature`, `createEpic`, `createInitiative`
- `createIdea`, `createIdeaTheme`
- `createPage`, `createPageFromTemplate`
- `createTask`, `createRequirement`

**Update Operations:**
- `updateFeature`, `updateEpic`, `updateInitiative`
- `updateIdea`, `updateIdeaTheme`
- `updatePage`, `updateRelease`

**Delete Operations:**
- `deleteFeature`, `deleteEpic`
- `deletePage`, `deleteTask`
- `deleteRequirement`

**Specialized Operations:**
- `promoteIdea` - Convert idea to feature
- `assignToTeam` - Team assignment
- `bulkPrioritizeRecords` - Bulk prioritization
- `triggerExtensionAutomation` - Extension triggers

### Key Patterns

1. **Consistent Naming**: Operations follow patterns like `create*`, `update*`, `delete*`
2. **Page Suffix**: Many types have corresponding `*Page` types for pagination
3. **Payload Pattern**: Mutations return `*Payload` types
4. **Filter/Order Pattern**: Most queries support filtering and ordering
5. **Relationship Management**: Clear patterns for managing relationships between entities
6. **Extension Support**: Built-in support for extensions and custom fields
7. **Comprehensive Bookmarks**: Multiple visualization types (boards, charts, roadmaps)

## REST API Overview

The Aha! REST API offers traditional RESTful endpoints with:
- **50+ resource types** organized hierarchically
- Standard CRUD operations (GET, POST, PUT, DELETE)
- Consistent URL patterns and reference number formats
- Query parameters for filtering and pagination

### Available REST Endpoints

**Core Product Management Resources:**
- **Products** - Workspaces and product lines
- **Features** - Core work items for product development
- **Requirements** - Detailed specifications within features
- **Releases** - Product release planning and tracking
- **Epics** - Large bodies of work spanning multiple features
- **Initiatives** - Strategic projects and programs
- **Goals** (Strategic Imperatives) - High-level strategic objectives

**Idea Management:**
- **Ideas** - Customer/user suggestions
- **Idea Portals** - Public-facing idea submission interfaces
- **Idea Comments** - Discussion on ideas
- **Idea Votes** - Voting mechanism for ideas
- **Idea Users** - Users who submit ideas
- **Idea Categories** - Categorization of ideas

**Collaboration & Work Management:**
- **Comments** - Discussions on various records
- **To-dos** (Tasks) - Action items and approvals
- **Notes** (Pages) - Documentation and knowledge base
- **Attachments** - File uploads and links

**User & Team Management:**
- **Users** - System users and permissions
- **Teams** - Team organization and capacity
- **Team Members** & **Team Memberships**
- **Identity Providers** - SSO configuration

**Integration & Automation:**
- **Integrations** - Third-party tool connections (Jira, GitHub, etc.)
- **Integration Fields** - Custom field mappings
- **Workflows** - Status workflows for different record types
- **Audits** - Activity tracking

**Planning & Strategy:**
- **Capacity Planning** - Resource allocation
- **Personas** - User/customer personas
- **Competitors** - Competitive analysis
- **Strategic Models**, **Visions**, **Positionings**

**Customization:**
- **Custom Fields** - Configurable fields for records
- **Custom Tables** - Custom data structures
- **Custom Layouts** - UI customization

### REST API Structure

The API endpoints are organized by resource type, with a consistent URL structure:
- Base URL: `https://{domain}.aha.io/api/v1/`
- Resource collections: `/api/v1/{resources}`
- Specific resources: `/api/v1/{resources}/{id}`
- Nested resources: `/api/v1/{parent_resources}/{parent_id}/{child_resources}`

### Reference Number Formats

- Features: `{PREFIX}-{NUMBER}` (e.g., `PRJ1-123`)
- Requirements: `{PREFIX}-{FEATURE_NUMBER}-{REQ_NUMBER}` (e.g., `PRJ1-123-1`)
- Pages/Notes: `{PREFIX}-N-{NUMBER}` (e.g., `PRJ1-N-213`)
- Releases: `{PREFIX}-R-{NUMBER}` (e.g., `PRJ1-R-1`)
- Epics: `{PREFIX}-E-{NUMBER}` (e.g., `PRJ1-E-1`)
- Ideas: `{PREFIX}-I-{NUMBER}` (e.g., `PRJ1-I-1`)

## Key Differences

### 1. Query Flexibility
- **GraphQL**: Request exactly what fields you need, reducing over/under-fetching
- **REST**: Fixed response structures, may include unnecessary data

### 2. API Surface
- **GraphQL**: Single endpoint with schema introspection
- **REST**: Multiple endpoints for each resource type

### 3. Advanced Features in GraphQL
- Discovery tools (interviews, scripts, studies)
- Bookmarks for various visualizations (boards, charts, roadmaps)
- Rich extension support with automation triggers
- More granular permission controls

### 4. Consistency
- **GraphQL**: Strong typing with consistent patterns (*Attributes, *Filters, *Payload)
- **REST**: Consistent URL patterns but varying response structures

### 5. Relationships
- **GraphQL**: Can fetch related data in single query
- **REST**: Requires multiple API calls for related resources

## Coverage Comparison

Both APIs cover core product management features, but GraphQL appears more comprehensive with:
- Enhanced discovery/research capabilities
- Better support for modern workflows (AI features, whiteboards)
- More sophisticated querying (bulk operations, complex filters)
- Richer metadata and extension points

## MCP Server Implementation

The MCP server currently uses GraphQL for its three tools:
- `get_record` - Fetches features (DEVELOP-123) or requirements (ADT-123-1)
- `get_page` - Fetches pages (ABC-N-213) with optional parent info
- `search_documents` - Searches Aha! documents by query and type

This leverages GraphQL's flexibility to fetch precisely the needed data with minimal requests, making it well-suited for the MCP protocol's requirements.