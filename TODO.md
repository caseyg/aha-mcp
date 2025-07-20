# Aha! MCP Server - TODO

## Current Status

**Completed:**
- ✅ 78 high-priority tools implemented
- ✅ 10 MCP prompts for common workflows
- ✅ OAuth2 authentication support
- ✅ FastMCP 2.0 migration
- ⚠️  Basic test suite (27 tests for ~25% coverage)

**In Progress:**
- 🚧 4 MCP resources (implemented but not visible in Claude)

## Remaining Work

### 1. Improve Test Coverage
- Current: ~27 tests covering only basic functionality
- Needed: Tests for remaining ~80 tools
- Priority areas: Tasks, Key Results, Record Links, Release Phases, Idea Votes

### 2. Fix MCP Resources (In Progress)
**Current Status:** Resources implemented but not visible in Claude interface

**Completed:**
- ✅ Created resources.py with 4 resource implementations
- ✅ Resources use parameterized URIs (required by FastMCP 2.0)
- ✅ Registered using @mcp.resource decorator in aha-mcp.py

**Issues to Resolve:**
- Resources not appearing in Claude @ mentions interface
- Need to debug visibility/registration issue

**Next Steps:**
1. Debug why resources aren't showing in Claude interface
2. Test resource functionality once visible
3. Add resource caching for performance

### 3. Tools to Implement (100+ tools remaining)
- **API Rate Limits** (2): get current usage, get limits
- **Audits** (3): list audit events, get audit details, export audit logs
- **Automation Rules** (5): list, create, update, delete, test automation rules
- **Backups** (3): list, create, restore backups
- **Capacity Management** (5): list, create, get, update, delete capacity investments
- **Competitors** (5): list, create, get, update, delete competitors
- **Creative Briefs** (5): list, create, get, update, delete creative briefs
- **Current User** (3): get current user, list assigned records, list pending tasks
- **Custom Field Options** (4): list, create, update, delete dropdown options
- **Custom Layouts** (4): list, create, update, delete UI layouts
- **Custom Pivots** (1): get custom pivot report data
- **Custom Table Record Links** (4): list, create, delete, bulk operations
- **Custom Tables** (5): list, create, get, update, delete custom table records
- **Deletions/Recycle Bin** (2): list recycle bin, restore deleted items
- **Historical Audits** (2): list historical audits, export audit history
- **Idea Organizations** (5): list, create, get, update, delete idea orgs
- **Identity Providers** (3): list, configure, test identity providers
- **Integration Changes** (1): send record to integration (push workflow)
- **Paid Seat Groups** (3): list, get details, manage assignments
- **Personas** (4): list, create, get, update personas
- **Roll-up Releases** (5): list, create, get, update, delete portfolio releases
- **Schedulable Changes** (3): list, create, delete future-dated changes
- **Schedules** (4): list, create, update, delete schedules
- **Scoring Systems** (4): list, create, update, delete scoring metrics
- **Team Memberships** (3): list, add, remove team member assignments
- **Teams** (6): list, create, get, update, delete teams; list team members
- **Time Tracking** (5): create, list, update, delete time entries; get time summary
- **Webhooks** (4): list, create, update, delete webhooks