# TODO - Aha! MCP Server Enhancements

## REST API Integration for Extended Functionality

The Aha! GraphQL API has limitations for certain operations that are available through their REST API. The following features could be implemented by adding REST API support alongside the existing GraphQL implementation:

### 1. Idea Score Updates

Currently, the GraphQL API doesn't support updating idea scores directly. Aha! uses a REST API for this:

- **Endpoint**: `PATCH https://{domain}.aha.io/ideas/ideas/{reference_num}`
- **Example**: `PATCH https://caseys-company.use3.aha.io/ideas/ideas/DEMO-I-26`
- **Request Body**:
```json
{
  "ideas_idea": {
    "score": "28",
    "score_facts_attributes": [
      {
        "scoring_system_metric_id": "6001166983756125437",
        "value": 28
      },
      {
        "scoring_system_metric_id": "6001166988050612717",
        "value": 0
      }
    ]
  }
}
```

**Implementation Notes**:
- Need to discover how to get scoring_system_metric_ids
- Score is sent as a string, not a number
- score_facts_attributes appears to be an array of metric values

### 2. Tag Management

Tags cannot be updated through GraphQL for ideas. Aha! uses a separate REST endpoint:

- **Endpoint**: `POST https://{domain}.aha.io/taggable/{numeric_id}/tags/set`
- **Example**: `POST https://caseys-company.use3.aha.io/taggable/7528931497935092063/tags/set`
- **Request Body**:
```json
[
  {
    "label": "test",
    "value": "7528935782288118517"
  }
]
```

**Implementation Notes**:
- Uses the numeric ID of the idea, not the reference number
- `value` is the tag ID (not the tag name)
- `label` is the display name of the tag
- Need to implement tag lookup/creation to get tag IDs

### 3. Other Potential REST Endpoints to Investigate

- **Description updates** - Ideas have descriptions through the Note system, but GraphQL doesn't expose update methods
- **Visibility updates** - The visibility field exists but isn't updateable through GraphQL
- **File attachments** - How to upload and attach files to ideas/features
- **Custom field updates** - More complex custom field operations

### 4. Implementation Approach

To add REST API support:

1. Add REST client alongside the existing GraphQL client
2. Use the same authentication token for both APIs
3. Create hybrid functions that use GraphQL for reads and REST for specific updates
4. Maintain backward compatibility with existing function signatures
5. Add configuration option to enable/disable REST API features

### 5. Authentication Considerations

- REST API uses the same Bearer token authentication as GraphQL
- Need to handle both API token and OAuth token scenarios
- May need to add proper error handling for REST-specific errors

### 6. Testing Requirements

- Need to test with different Aha! account types (some features may be plan-specific)
- Verify REST endpoints are stable across Aha! updates
- Test error handling for both authentication methods
- Ensure REST operations don't break existing GraphQL functionality

## MCP Enhancements

### 7. Add MCP Prompts

Add predefined prompts to guide users in common Aha! workflows:

- **Feature Management**: Prompts for creating, updating, and tracking features
- **Idea Processing**: Prompts for reviewing, scoring, and promoting ideas
- **Project Planning**: Prompts for release planning and roadmap management
- **Reporting**: Prompts for generating reports and analytics

### 8. Add MCP Resources

Expose Aha! data as MCP resources for better integration:

- **Active Releases**: List of current releases with their features
- **Idea Backlog**: Pending ideas requiring review
- **My Work**: Items assigned to the current user
- **Recent Updates**: Recently modified items across the workspace

### 9. Add More Aha! Endpoints

#### GraphQL vs REST API Comparison

Based on analysis of available GraphQL mutations and REST API endpoints, here's a comprehensive comparison:

| Resource | GraphQL Mutations Available | REST API Endpoints | Implementation Notes |
|----------|---------------------------|-------------------|---------------------|
| **Features** | ✅ createFeature<br>✅ updateFeature<br>✅ deleteFeature | ✅ Full CRUD<br>✅ Convert to epic<br>✅ Tags, scores, watchers | GraphQL covers basic needs; REST adds conversion & metadata |
| **Ideas** | ✅ createIdea<br>✅ updateIdea<br>✅ promoteIdea | ✅ Full CRUD<br>✅ Promote to feature/epic<br>❌ Score updates (REST only)<br>❌ Tags (REST only) | **REST needed for scores & tags** |
| **Releases** | ✅ createRelease<br>✅ updateRelease<br>❌ deleteRelease | ✅ Full CRUD<br>✅ Duplicate release<br>✅ Sub-releases | GraphQL missing delete; REST has duplication |
| **Epics** | ✅ createEpic<br>✅ updateEpic<br>✅ deleteEpic | ✅ Full CRUD<br>✅ Multiple parent contexts | GraphQL fully functional |
| **Requirements** | ✅ createRequirement<br>✅ updateRequirement<br>✅ deleteRequirement | ✅ Full CRUD<br>✅ Convert to feature | GraphQL covers needs; REST adds conversion |
| **Comments** | ✅ createComment<br>❌ updateComment<br>❌ deleteComment | ✅ Full CRUD on all resources | **GraphQL incomplete; REST needed** |
| **Tasks/To-dos** | ✅ createTask<br>✅ updateTask<br>✅ deleteTask | ✅ Full CRUD | GraphQL fully functional |
| **Goals** | ✅ createGoal<br>✅ updateGoal<br>❌ deleteGoal | ✅ Full CRUD | GraphQL missing delete |
| **Initiatives** | ✅ createInitiative<br>✅ updateInitiative<br>❌ deleteInitiative | ✅ Full CRUD | GraphQL missing delete |
| **Pages** | ✅ createPage<br>✅ updatePage<br>✅ deletePage<br>✅ createPageFromTemplate | ✅ Full CRUD | GraphQL fully functional with templates |
| **Workflows** | ✅ createWorkflowStatus<br>✅ updateWorkflowStatus<br>✅ deleteWorkflowStatus | ✅ List workflows<br>✅ Get workflow details | GraphQL manages statuses; REST for workflow info |
| **Custom Fields** | ✅ setCustomFieldValue | ✅ List definitions<br>✅ Get options<br>✅ Update values | GraphQL can set values; REST for metadata |
| **Attachments** | ❌ No mutations | ✅ Create on various resources<br>✅ Delete | **REST only for file uploads** |
| **Users** | ❌ No mutations | ✅ Full CRUD<br>✅ Role management | **REST only for user management** |
| **Teams** | ✅ assignToTeam<br>✅ setWipLimits | ✅ Full CRUD | GraphQL for assignment; REST for team CRUD |
| **Iterations** | ✅ createIteration<br>✅ updateIteration<br>✅ deleteIteration<br>✅ completeIteration | Not documented | GraphQL only (Agile features) |
| **Record Links** | ✅ createRecordLink | ✅ Full CRUD | GraphQL can create; REST for full management |
| **Bookmarks** | ✅ Multiple update mutations | Not documented | GraphQL only (UI features) |
| **Extensions** | ✅ Multiple mutations | Not documented | GraphQL only (Platform features) |

#### Priority Implementation Recommendations

1. **High Priority (REST Required)**:
   - **Idea Scores & Tags**: No GraphQL support
   - **Attachments/File Uploads**: No GraphQL support
   - **User Management**: No GraphQL support
   - **Comments CRUD**: GraphQL only has create

2. **Medium Priority (GraphQL Incomplete)**:
   - **Release Delete**: Missing in GraphQL
   - **Goal Delete**: Missing in GraphQL
   - **Initiative Delete**: Missing in GraphQL
   - **Comment Update/Delete**: Missing in GraphQL

3. **Low Priority (GraphQL Sufficient)**:
   - Features, Epics, Requirements, Tasks, Pages: Fully covered
   - Iterations, Bookmarks, Extensions: GraphQL-only features

4. **Nice to Have (REST Enhancements)**:
   - Convert operations (feature→epic, requirement→feature)
   - Duplicate release
   - Bulk operations
   - Advanced filtering/search