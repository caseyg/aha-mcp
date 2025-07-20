# Aha! MCP Server

The Aha! MCP Server connects AI tools directly to Aha!'s product management platform. This gives AI agents, assistants, and chatbots the ability to read and manage features, ideas, releases, and other Aha! records through natural language interactions.

### Use Cases

- **Product Management**: Browse and manage features, releases, epics, and initiatives. Create and update product roadmaps, track progress, and maintain product documentation.
- **Idea Management**: Create, evaluate, and manage product ideas. Convert promising ideas to features, track votes and feedback, manage idea workflows.
- **Development Planning**: Manage requirements, track dependencies between features, analyze release capacity, and coordinate development efforts.
- **Team Collaboration**: Create and manage tasks, track key results and OKRs, manage team assignments, and generate status reports.
- **Strategic Planning**: Access strategic models, visions, and positioning. Link features to goals and initiatives for comprehensive product strategy.

Built for product managers and developers who want to connect their AI tools to Aha! context and capabilities, from simple natural language queries to complex multi-step workflows.

## Prerequisites

- Python 3.10 or higher
- An Aha! account with API access
- API token or OAuth credentials from Aha!

## Installation

```bash
# Clone the repository
git clone https://github.com/aha-develop/aha-mcp.git
cd aha-mcp

# Install Python dependencies
pip install -r requirements.txt
```

## Configuration

### Option 1: API Token (Recommended for Personal Use)

1. Get your API token from Aha!:
   - Log in to your Aha! account
   - Visit Settings → Personal → API
   - Generate a new token

2. Create a `.env` file:
   ```env
   AHA_API_TOKEN=your-api-token
   AHA_DOMAIN=yoursubdomain
   ```

### Option 2: OAuth (For Team/Application Use)

1. Create an OAuth application in Aha!:
   - Go to Settings → Account → OAuth applications
   - Create a new application
   - Note the Client ID and Client Secret

2. Create a `.env` file:
   ```env
   OAUTH_CLIENT_ID=your-oauth-client-id
   OAUTH_CLIENT_SECRET=your-oauth-client-secret
   AHA_DOMAIN=yoursubdomain
   ```

## Running the Server

```bash
# Run with FastMCP (recommended)
fastmcp run aha-mcp.py --transport http

# Or run directly
python aha-mcp.py
```

The server runs on HTTP transport at `http://localhost:8000`. When OAuth credentials are configured, it provides OAuth discovery endpoints for MCP-compliant authentication.

## IDE Integration

<details>
<summary><b>VSCode</b></summary>

Add this to your `.vscode/settings.json`:

```json
{
  "mcp": {
    "servers": {
      "aha-mcp": {
        "command": "python",
        "args": ["/path/to/aha-mcp.py"],
        "env": {
          "AHA_API_TOKEN": "your-api-token",
          "AHA_DOMAIN": "yoursubdomain"
        }
      }
    }
  }
}
```

For more secure token management, consider using environment variables or a secure credential store instead of hardcoding tokens.
</details>

<details>
<summary><b>Cursor</b></summary>

1. Go to Cursor Settings > MCP
2. Click + Add new Global MCP Server
3. Add a configuration similar to:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"],
      "env": {
        "AHA_API_TOKEN": "your-api-token",
        "AHA_DOMAIN": "yoursubdomain"
      }
    }
  }
}
```
</details>

<details>
<summary><b>Claude Desktop</b></summary>

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"],
      "env": {
        "AHA_API_TOKEN": "your-api-token",
        "AHA_DOMAIN": "yoursubdomain"
      }
    }
  }
}
```
</details>

<details>
<summary><b>Other IDEs (Cline, RooCode, etc.)</b></summary>

Most MCP-compatible IDEs follow a similar configuration pattern. Add to your IDE's MCP configuration:

```json
{
  "mcpServers": {
    "aha-mcp": {
      "command": "python",
      "args": ["/path/to/aha-mcp.py"],
      "env": {
        "AHA_API_TOKEN": "your-api-token",
        "AHA_DOMAIN": "yoursubdomain"
      }
    }
  }
}
```
</details>

## Tools

<!-- START AUTOMATED TOOLS -->
<details>
<summary><b>Core Features (14 tools)</b></summary>

- **get_record** - Get an Aha! record by reference (features, requirements, ideas)
  - `reference`: Reference number (e.g., "DEVELOP-123", "ADT-123-1", "ABC-I-123") (string, required)

- **get_page** - Get an Aha! page by reference
  - `reference`: Page reference number (e.g., "ABC-N-213") (string, required)
  - `includeParent`: Include parent page information (boolean, optional)

- **search_documents** - Search Aha! documents
  - `query`: Search query string (string, required)
  - `searchableType`: Type of document to search (default: "Page") (string, optional)

- **create_feature** - Create a new feature
  - `releaseId`: ID or reference of the release (string, required)
  - `name`: Feature name (string, required)
  - `description`: Feature description in markdown (string, optional)
  - `assignedToUserId`: ID of user to assign to (string, optional)
  - `tags`: Array of tags (string[], optional)
  - `workflowStatusId`: Workflow status ID (string, optional)
  - `epicId`: Epic ID or reference (string, optional)
  - `teamId`: Team ID (string, optional)

- **update_feature** - Update an existing feature
  - `id`: Feature ID or reference (string, required)
  - `name`: New feature name (string, optional)
  - `description`: New description (string, optional)
  - `workflowStatusId`: New workflow status ID (string, optional)
  - `assignedToUserId`: User ID to reassign to (string, optional)
  - `assignedToUserEmail`: User email to reassign to (string, optional)
  - `tags`: New tags (string[], optional)

- **delete_feature** - Delete a feature
  - `id`: Feature ID or reference to delete (string, required)

- **list_features** - List features with filters
  - `releaseId`: Filter by release (string, optional)
  - `epicId`: Filter by epic (string, optional)
  - `projectId`: Filter by project (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_feature_details** - Get detailed feature information
  - `id`: Feature ID or reference (string, required)

- **get_idea** - Get an idea by ID or reference
  - `id`: Idea ID or reference (e.g., "ABC-I-123") (string, required)

- **list_ideas** - List ideas for a project
  - `projectId`: Project ID or reference (string, required)
  - `assignedToUserId`: Filter by assigned user (string, optional)
  - `promoted`: Filter by promotion status (boolean, optional)
  - `visibility`: Filter by visibility (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_idea** - Create a new idea
  - `projectId`: Project ID or reference (string, required)
  - `name`: Idea name (string, required)
  - `assignedToUserId`: User ID to assign to (string, optional)
  - `workflowStatusId`: Workflow status ID (string, optional)

- **update_idea** - Update an existing idea
  - `id`: Idea ID or reference (string, required)
  - `name`: New idea name (string, optional)
  - `assignedToUserId`: User ID to reassign to (string, optional)
  - `workflowStatusId`: New workflow status ID (string, optional)

- **delete_idea** - Delete an idea
  - `id`: Idea ID or reference to delete (string, required)

- **introspection** - Explore Aha! GraphQL API schema
  - `queryType`: Type of introspection (default: "list-types") (string, optional)
  - `typeName`: Name of type to explore (string, optional)
  - `searchTerm`: Search term for filtering (string, optional)
  - `maxResults`: Maximum results to return (number, optional)
</details>

<details>
<summary><b>Project Management (14 tools)</b></summary>

- **list_projects** - List projects/workspaces
  - `teamsOnly`: Show only teams (boolean, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **list_epics** - List epics
  - `projectId`: Filter by project (string, optional)
  - `releaseId`: Filter by release (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_epic** - Create an epic
  - `releaseId`: Release ID or reference (string, required)
  - `name`: Epic name (string, required)
  - `description`: Epic description (string, optional)
  - `assignedToUserId`: User ID to assign to (string, optional)

- **update_epic** - Update an epic
  - `id`: Epic ID or reference (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `workflowStatusId`: New workflow status (string, optional)
  - `assignedToUserId`: User to reassign to (string, optional)

- **delete_epic** - Delete an epic
  - `id`: Epic ID or reference (string, required)

- **list_releases** - List releases
  - `projectId`: Filter by project (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_release** - Create a release
  - `projectId`: Project ID or reference (string, required)
  - `name`: Release name (string, required)
  - `description`: Release description (string, optional)
  - `releaseDate`: Release date (string, optional)
  - `startDate`: Start date (string, optional)

- **update_release** - Update a release
  - `id`: Release ID or reference (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `releaseDate`: New release date (string, optional)
  - `startDate`: New start date (string, optional)

- **delete_release** - Delete a release
  - `id`: Release ID or reference (string, required)

- **duplicate_release** - Copy release structure
  - `id`: Release ID to duplicate (string, required)

- **list_initiatives** - List initiatives
  - `projectId`: Filter by project (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_initiative** - Create an initiative
  - `projectId`: Project ID or reference (string, required)
  - `name`: Initiative name (string, required)
  - `description`: Initiative description (string, optional)
  - `assignedToUserId`: User ID to assign to (string, optional)

- **update_initiative** - Update an initiative
  - `id`: Initiative ID or reference (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `workflowStatusId`: New workflow status (string, optional)
  - `assignedToUserId`: User to reassign to (string, optional)

- **delete_initiative** - Delete an initiative
  - `id`: Initiative ID or reference (string, required)
</details>

<details>
<summary><b>Goals & OKRs (11 tools)</b></summary>

- **list_goals** - List goals
  - `projectId`: Filter by project (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_goal** - Create a goal
  - `projectId`: Project ID or reference (string, required)
  - `name`: Goal name (string, required)
  - `metricName`: Metric name (string, optional)
  - `workflowStatusId`: Workflow status ID (string, optional)

- **update_goal** - Update a goal
  - `id`: Goal ID or reference (string, required)
  - `name`: New name (string, optional)
  - `metricName`: New metric name (string, optional)
  - `workflowStatusId`: New workflow status (string, optional)

- **delete_goal** - Delete a goal
  - `id`: Goal ID or reference (string, required)

- **list_key_results** - List key results for a goal
  - `goalId`: Goal ID or reference (string, required)

- **create_key_result** - Create a key result
  - `goalId`: Goal ID or reference (string, required)
  - `name`: Key result name (string, required)
  - `startingMetric`: Starting metric value (string, optional)
  - `targetMetric`: Target metric value (string, optional)
  - `assignedToUserEmail`: User email to assign to (string, optional)
  - `workflowStatusName`: Workflow status name (string, optional)

- **get_key_result** - Get key result details
  - `keyResultId`: Key result ID (string, required)

- **update_key_result** - Update a key result
  - `keyResultId`: Key result ID (string, required)
  - `name`: New name (string, optional)
  - `currentMetric`: Current metric value (string, optional)
  - `startingMetric`: New starting metric (string, optional)
  - `targetMetric`: New target metric (string, optional)
  - `assignedToUserEmail`: User to reassign to (string, optional)
  - `workflowStatusName`: New workflow status (string, optional)

- **delete_key_result** - Delete a key result
  - `keyResultId`: Key result ID (string, required)

- **update_key_result_progress** - Update key result progress
  - `keyResultId`: Key result ID (string, required)
  - `currentMetric`: Current metric value (string, required)

- **convert_feature_to_epic** - Convert feature to epic
  - `id`: Feature ID or reference (string, required)
</details>

<details>
<summary><b>Requirements & Dependencies (10 tools)</b></summary>

- **list_requirements** - List requirements
  - `projectId`: Filter by project (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_requirement** - Create a requirement
  - `featureId`: Feature ID or reference (string, required)
  - `name`: Requirement name (string, required)
  - `description`: Requirement description (string, optional)
  - `assignedToUserId`: User ID to assign to (string, optional)
  - `originalEstimate`: Original estimate (string, optional)
  - `initialEstimate`: Initial estimate (string, optional)
  - `position`: Position in list (number, optional)

- **update_requirement** - Update a requirement
  - `id`: Requirement ID or reference (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `workflowStatusId`: New workflow status (string, optional)
  - `assignedToUserId`: User to reassign to (string, optional)
  - `originalEstimate`: New original estimate (string, optional)
  - `remainingEstimate`: Remaining estimate (string, optional)
  - `workDone`: Work done (string, optional)

- **delete_requirement** - Delete a requirement
  - `id`: Requirement ID or reference (string, required)

- **list_record_links** - List dependencies between records
  - `recordType`: Type of record (string, required)
  - `recordId`: Record ID or reference (string, required)
  - `parentAndChildLinks`: Include both directions (boolean, optional)

- **create_record_link** - Create dependency relationship
  - `parentRecordType`: Parent record type (string, required)
  - `parentRecordId`: Parent record ID (string, required)
  - `childRecordType`: Child record type (string, required)
  - `childRecordId`: Child record ID (string, required)
  - `linkType`: Type of link (number, required)

- **get_record_link** - Get link details
  - `recordLinkId`: Record link ID (string, required)

- **delete_record_link** - Remove dependency
  - `recordLinkId`: Record link ID (string, required)

- **list_record_links_for_type** - Get links by record type
  - `recordType`: Type of record (string, required)
  - `linkType`: Filter by link type (number, optional)

- **update_feature_tags** - Update feature tags
  - `id`: Feature ID or reference (string, required)
  - `tags`: Comma-separated tags (string, required)
</details>

<details>
<summary><b>Tasks & To-dos (7 tools)</b></summary>

- **create_task** - Create a task
  - `recordType`: Type of record to attach to (string, required)
  - `recordId`: Record ID to attach to (string, required)
  - `name`: Task name (string, required)
  - `description`: Task description (string, optional)
  - `dueDate`: Due date (string, optional)
  - `assignedToUserEmail`: User email to assign to (string, optional)

- **list_tasks** - List tasks
  - `assignedToUserId`: Filter by assigned user (string, optional)
  - `completed`: Filter by completion status (boolean, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_task** - Get task details
  - `taskId`: Task ID (string, required)

- **update_task** - Update a task
  - `taskId`: Task ID (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `dueDate`: New due date (string, optional)
  - `completed`: Completion status (boolean, optional)
  - `assignedToUserEmail`: User to reassign to (string, optional)

- **delete_task** - Delete a task
  - `taskId`: Task ID (string, required)

- **complete_task** - Mark task complete/incomplete
  - `taskId`: Task ID (string, required)
  - `completed`: Completion status (boolean, optional)

- **list_tasks_for_record** - Get tasks for specific record
  - `recordType`: Type of record (string, required)
  - `recordId`: Record ID (string, required)
  - `assignedToUserId`: Filter by assigned user (string, optional)
  - `completed`: Filter by completion status (boolean, optional)
</details>

<details>
<summary><b>Comments & Collaboration (4 tools)</b></summary>

- **create_comment** - Add comment to record
  - `recordId`: Record ID to comment on (string, required)
  - `body`: Comment content (string, required)
  - `recordType`: Type of record (default: "feature") (string, optional)

- **update_comment** - Edit existing comment
  - `id`: Comment ID (string, required)
  - `body`: New comment content (string, required)

- **delete_comment** - Remove comment
  - `id`: Comment ID (string, required)

- **list_comments** - Get comments for a record
  - `recordId`: Record ID (string, required)
  - `recordType`: Type of record (default: "feature") (string, optional)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)
</details>

<details>
<summary><b>Release Management (5 tools)</b></summary>

- **list_release_phases** - List phases for a release
  - `releaseId`: Release ID or reference (string, required)
  - `phaseType`: Filter by phase type (string, optional)

- **create_release_phase** - Create release phase/milestone
  - `releaseId`: Release ID or reference (string, required)
  - `name`: Phase name (string, required)
  - `description`: Phase description (string, optional)
  - `phaseType`: Type of phase (default: "phase") (string, optional)
  - `startOn`: Start date (string, optional)
  - `endOn`: End date (string, optional)

- **get_release_phase** - Get phase details
  - `phaseId`: Phase ID (string, required)

- **update_release_phase** - Update phase dates/status
  - `phaseId`: Phase ID (string, required)
  - `name`: New name (string, optional)
  - `description`: New description (string, optional)
  - `startOn`: New start date (string, optional)
  - `endOn`: New end date (string, optional)
  - `progress`: Progress percentage (number, optional)

- **delete_release_phase** - Remove phase
  - `phaseId`: Phase ID (string, required)
</details>

<details>
<summary><b>Idea Portal Management (14 tools)</b></summary>

- **create_idea_vote** - Vote for an idea
  - `ideaId`: Idea ID or reference (string, required)
  - `value`: Vote value (number, optional)
  - `userEmail`: Voter email (string, optional)
  - `description`: Vote description (string, optional)
  - `link`: Related link (string, optional)

- **list_idea_votes** - List votes for an idea
  - `ideaId`: Idea ID or reference (string, required)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_idea_vote** - Get vote details
  - `ideaId`: Idea ID or reference (string, required)
  - `voteId`: Vote ID (string, required)

- **update_idea_vote** - Modify vote value
  - `ideaId`: Idea ID or reference (string, required)
  - `voteId`: Vote ID (string, required)
  - `value`: New vote value (number, optional)
  - `description`: New description (string, optional)
  - `link`: New link (string, optional)

- **delete_idea_vote** - Remove vote
  - `ideaId`: Idea ID or reference (string, required)
  - `voteId`: Vote ID (string, required)

- **create_proxy_vote** - Create vote on behalf of portal users
  - `ideaId`: Idea ID or reference (string, required)
  - `value`: Vote value (number, required)
  - `voterEmails`: Array of voter emails (string[], required)
  - `description`: Vote description (string, optional)
  - `link`: Related link (string, optional)
  - `ideaOrganizationId`: Organization ID (string, optional)

- **list_idea_portals** - List idea portals
  - `productId`: Product ID or reference (string, required)

- **list_idea_portal_users** - List portal users
  - `ideaPortalId`: Portal ID (string, required)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_idea_portal_user** - Add portal user
  - `ideaPortalId`: Portal ID (string, required)
  - `email`: User email (string, required)
  - `firstName`: First name (string, optional)
  - `lastName`: Last name (string, optional)
  - `enabled`: Account enabled status (boolean, optional)
  - `permission`: Permission level (string, optional)
  - `maxEndorsementOverride`: Max endorsement override (number, optional)

- **update_idea_portal_user** - Update user details
  - `ideaPortalId`: Portal ID (string, required)
  - `userId`: User ID (string, required)
  - `firstName`: New first name (string, optional)
  - `lastName`: New last name (string, optional)
  - `enabled`: New enabled status (boolean, optional)
  - `unsubscribed`: Unsubscribe status (boolean, optional)
  - `maxEndorsementOverride`: New max endorsement (number, optional)

- **list_idea_subscriptions** - List idea subscriptions
  - `ideaId`: Idea ID or reference (string, required)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_idea_subscription** - Subscribe user to idea
  - `ideaId`: Idea ID or reference (string, required)
  - `userEmail`: User email (string, required)

- **delete_idea_subscription** - Remove subscription
  - `ideaId`: Idea ID or reference (string, required)
  - `subscriptionId`: Subscription ID (string, required)

- **list_idea_categories** - List idea categories
  - `productId`: Product ID or reference (string, required)
</details>

<details>
<summary><b>Strategic Planning (6 tools)</b></summary>

- **list_strategic_models** - List strategy models
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_strategic_model** - Get model details
  - `modelId`: Model ID (string, required)

- **list_strategic_visions** - List strategic visions
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_strategic_vision** - Get vision details
  - `visionId`: Vision ID (string, required)

- **list_strategic_positions** - List strategic positions
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **get_strategic_position** - Get position details
  - `positionId`: Position ID (string, required)
</details>

<details>
<summary><b>Other Management Tools (17 tools)</b></summary>

- **list_users** - Get workspace users
  - `projectId`: Filter by project (string, optional)
  - `email`: Filter by email (string, optional)

- **create_user** - Add new user
  - `projectId`: Project ID or reference (string, required)
  - `email`: User email (string, required)
  - `firstName`: First name (string, required)
  - `lastName`: Last name (string, required)
  - `role`: User role (string, required)
  - `identityProviderId`: Identity provider ID (string, optional)

- **upload_attachment** - Upload file to record
  - `resourceType`: Type of resource (string, required)
  - `resourceId`: Resource ID (string, required)
  - `fileUrl`: URL of file to attach (string, required)
  - `fileName`: Name for attachment (string, required)
  - `contentType`: MIME type (string, optional)

- **delete_attachment** - Remove file attachment
  - `attachmentId`: Attachment ID (string, required)

- **get_all_tags** - Get all tags in Aha!
  - `nameFilter`: Filter tags by name (string, optional)

- **list_workflows** - Get available workflows
  - `projectId`: Project ID or reference (string, required)

- **list_custom_fields** - Get custom field definitions

- **list_products** - List products in account
  - `updatedSince`: Filter by update date (string, optional)

- **get_product** - Get product details
  - `productId`: Product ID or reference (string, required)

- **list_pages** - List pages/notes in products
  - `productId`: Product ID or reference (string, required)
  - `page`: Page number (number, optional)
  - `perPage`: Items per page (number, optional)

- **create_page** - Create documentation page
  - `productId`: Product ID or reference (string, required)
  - `name`: Page name (string, required)
  - `body`: Page content (string, optional)
  - `pageType`: Type of page (default: "page") (string, optional)
  - `parentId`: Parent page ID (string, optional)

- **update_page** - Update page content
  - `pageId`: Page ID (string, required)
  - `name`: New name (string, optional)
  - `body`: New content (string, optional)

- **delete_page** - Remove page
  - `pageId`: Page ID (string, required)

- **list_integrations** - List configured integrations

- **create_integration_field** - Map integration field
  - `recordType`: Type of record (string, required)
  - `recordId`: Record ID (string, required)
  - `integrationId`: Integration ID (string, required)
  - `fieldName`: Field name (string, required)
  - `fieldValue`: Field value (string, required)

- **update_integration_field** - Update field mapping
  - `recordType`: Type of record (string, required)
  - `recordId`: Record ID (string, required)
  - `integrationId`: Integration ID (string, required)
  - `fieldName`: Field name (string, required)
  - `fieldValue`: New field value (string, required)

- **delete_integration_field** - Remove field mapping
  - `fieldId`: Field ID (string, required)
</details>

<details>
<summary><b>Idea Management Extensions (6 tools)</b></summary>

- **promote_idea** - Convert idea to feature/epic
  - `id`: Idea ID or reference (string, required)
  - `targetType`: Target type ("feature" or "epic") (string, required)
  - `releaseId`: Target release ID (string, optional)
  - `name`: Feature/epic name (string, optional)
  - `description`: Feature/epic description (string, optional)
  - `assignedToUserId`: User to assign to (string, optional)

- **update_idea_score** - Update idea score
  - `id`: Idea ID or reference (string, required)
  - `score`: New score value (number, required)

- **update_idea_tags** - Set/update idea tags
  - `id`: Idea ID or reference (string, required)
  - `tags`: Array of tags (string[], required)
</details>
<!-- END AUTOMATED TOOLS -->

## Prompts

The server provides pre-defined prompts to help with common Aha! workflows:

<details>
<summary><b>Available Prompts (10 prompts)</b></summary>

- **analyze_feature_backlog** - Comprehensive backlog analysis
  - `project_id`: Project to analyze (required)
  - `release_id`: Specific release focus (optional)

- **create_feature_spec** - Detailed feature specification
  - `feature_name`: Name of the feature (required)
  - `release_id`: Target release (required)
  - `user_story`: User story description (required)
  - `acceptance_criteria`: Acceptance criteria (optional)

- **idea_evaluation** - Evaluate and prioritize ideas
  - `project_id`: Project containing ideas (required)
  - `evaluation_criteria`: Criteria to use (optional)

- **release_planning** - Release planning and capacity analysis
  - `release_id`: Release to plan (required)
  - `team_capacity`: Team capacity info (optional)
  - `focus_areas`: Areas to focus on (optional)

- **bug_triage_session** - Bug triage with filtering
  - `tag`: Filter by tag (optional)
  - `severity_threshold`: Minimum severity (optional)
  - `age_days`: Minimum age in days (optional)

- **feature_dependencies_analysis** - Analyze feature dependencies
  - `feature_reference`: Feature to analyze (required)
  - `check_upstream`: Check dependencies (optional)
  - `check_downstream`: Check dependents (optional)

- **sprint_retrospective** - Sprint retrospective analysis
  - `sprint_name`: Sprint name (required)
  - `team_name`: Team to focus on (optional)

- **weekly_status_report** - Generate status report
  - `project_id`: Project to report on (required)
  - `week_ending`: Week ending date (required)
  - `include_metrics`: Include metrics (optional)

- **idea_to_feature_conversion** - Convert idea to feature
  - `idea_reference`: Idea to convert (required)
  - `target_release`: Target release (required)

- **integration_checklist** - Integration planning checklist
  - `feature_reference`: Feature requiring integration (required)
  - `integration_type`: Type of integration (optional)
</details>

## Example Usage

### Common Queries
- "Get feature DEVELOP-123"
- "List all features in release PRJ1-R-1"
- "Create a new feature called 'User Authentication' for the Q1 release"
- "Update the status of feature DEVELOP-456 to 'In Progress'"
- "Show me all ideas in project PRJ1 that haven't been promoted"
- "Convert idea ABC-I-789 to a feature"
- "What dependencies does feature DEVELOP-123 have?"
- "Generate a weekly status report for project PRJ1"

### Complex Workflows
- "Analyze the feature backlog for project PRJ1 and identify blocked items"
- "Evaluate all ideas in project PRJ1 based on value, effort, and risk"
- "Plan the capacity for release PRJ1-R-2 considering team availability"
- "Create a comprehensive integration checklist for feature DEVELOP-456"

## Development

### Running Tests

```bash
# Run all tests
pytest test_aha_mcp.py -v

# Run specific test
pytest test_aha_mcp.py -k "test_name"

# Run with coverage
pytest test_aha_mcp.py --cov=aha-mcp
```

### Debug Mode

```bash
# Run with debug logging
LOG_LEVEL=debug python aha-mcp.py
```

## Troubleshooting

### Authentication Issues
- Verify your API token is correct and has necessary permissions
- For OAuth, ensure both CLIENT_ID and CLIENT_SECRET are set
- Check you're using the correct Aha! domain (subdomain only)

### Common Errors
- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **Python version error**: Requires Python 3.10+ (check with `python --version`)
- **Connection refused**: Use `--transport http` with fastmcp
- **Invalid reference format**: Use correct formats (e.g., PROJ-123, ABC-I-456)

### Performance Tips
- Use filters in list operations to reduce response size
- Paginate through large result sets
- Cache frequently accessed data when appropriate

## Architecture

This Python implementation uses:
- **FastMCP 2.0** for simplified MCP protocol handling
- **GraphQL API** for most operations with REST API fallback
- **OAuth2 Support** with discovery endpoints for MCP compliance
- **Modular Design** with separate files for tools, prompts, and client
- **Comprehensive Testing** with pytest and mocked responses
- **78 Tools** covering features, ideas, releases, tasks, goals, and more
- **10 Prompts** for common product management workflows

## License

MIT License - see LICENSE file for details

## Contributing

This implementation is based on the [original TypeScript MCP server by Aha!](https://github.com/aha-develop/aha-mcp) but has been rewritten in Python using the FastMCP framework for enhanced functionality.

Contributions are welcome! Please submit issues and pull requests on GitHub.