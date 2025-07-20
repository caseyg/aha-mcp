"""MCP prompts for common Aha! workflows."""

from typing import Optional, List
from fastmcp import FastMCP, Context
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent

# This will be set by the main module
mcp: Optional[FastMCP] = None


def register_prompts(mcp_instance: FastMCP):
    """Register all prompts with the MCP instance"""
    global mcp
    mcp = mcp_instance
    
    # Register all prompts
    mcp.prompt(analyze_feature_backlog)
    mcp.prompt(create_feature_spec)
    mcp.prompt(idea_evaluation)
    mcp.prompt(release_planning)
    mcp.prompt(bug_triage_session)
    mcp.prompt(feature_dependencies_analysis)
    mcp.prompt(sprint_retrospective)
    mcp.prompt(
        description="Generate a prompt to create weekly status report",
        tags={"reporting", "status", "weekly"}
    )(weekly_status_report)
    mcp.prompt(idea_to_feature_conversion)
    mcp.prompt(
        enabled=True,
        tags={"automation", "integration"}
    )(integration_checklist)


def analyze_feature_backlog(project_id: str, release_id: Optional[str] = None) -> list[Message]:
    """Generate a prompt to analyze your feature backlog"""
    messages = [
        Message(f"I need to analyze the feature backlog for project {project_id}.")
    ]
    
    if release_id:
        messages.append(Message(f"Please focus specifically on release {release_id}."))
    else:
        messages.append(Message("Please analyze features across all releases."))
    
    messages.extend([
        Message("For the analysis, please:"),
        Message("1. List all features grouped by workflow status"),
        Message("2. Identify any features without assigned users"),
        Message("3. Highlight features that might be blocked or at risk"),
        Message("4. Provide a summary of the overall backlog health"),
        Message("5. Suggest any items that need immediate attention")
    ])
    
    return messages


def create_feature_spec(
    feature_name: str, 
    release_id: str,
    user_story: str,
    acceptance_criteria: Optional[str] = None
) -> str:
    """Generate a prompt to create a detailed feature specification"""
    prompt = f"""Please help me create a comprehensive feature specification for:

Feature Name: {feature_name}
Target Release: {release_id}

User Story:
{user_story}

"""
    
    if acceptance_criteria:
        prompt += f"""Acceptance Criteria:
{acceptance_criteria}

"""
    
    prompt += """Based on this information, please:
1. Create a detailed feature description in HTML format suitable for Aha!
2. Break down the feature into clear implementation requirements
3. Identify potential technical challenges or dependencies
4. Suggest appropriate tags for categorization
5. Recommend a workflow status to start with

Format the response so I can easily create the feature in Aha! using the create_feature tool."""
    
    return prompt


def idea_evaluation(
    project_id: str,
    evaluation_criteria: str = "value, effort, risk"
) -> list[Message]:
    """Generate a prompt to evaluate ideas in a project"""
    return [
        Message(f"I need to evaluate ideas in project {project_id}."),
        Message(f"Please analyze the ideas based on these criteria: {evaluation_criteria}"),
        Message("For each idea, provide:"),
        Message("1. A brief summary of what it proposes"),
        Message("2. An evaluation score for each criterion (1-10)"),
        Message("3. Potential implementation challenges"),
        Message("4. Recommendation on whether to promote to a feature"),
        Message("5. If promoting, suggest which release it should target"),
        Message("Create a prioritized list with your top recommendations.")
    ]


def release_planning(
    release_id: str,
    team_capacity: Optional[str] = None,
    focus_areas: Optional[str] = None
) -> str:
    """Generate a prompt for release planning and capacity analysis"""
    prompt = f"""I need help with release planning for release {release_id}.

"""
    
    if team_capacity:
        prompt += f"Team Capacity: {team_capacity}\n"
    
    if focus_areas:
        prompt += f"Focus Areas: {focus_areas}\n"
    
    prompt += """
Please analyze the current release and provide:

1. **Current State Analysis**
   - Total number of features and their status breakdown
   - Features by assignee
   - High-risk or blocked items

2. **Capacity Planning**
   - Estimate if the current scope fits within capacity
   - Identify any overallocated team members
   - Suggest features that could be moved if needed

3. **Release Readiness**
   - Features still in early stages that might not complete
   - Dependencies between features
   - Testing and deployment considerations

4. **Recommendations**
   - Priority adjustments needed
   - Features to accelerate or defer
   - Resource reallocation suggestions

Please be specific with feature references (e.g., PROJ-123) in your analysis."""
    
    return prompt


def bug_triage_session(
    tag: Optional[str] = None,
    severity_threshold: str = "high",
    age_days: int = 7
) -> list[Message]:
    """Generate a prompt for bug triage session"""
    messages = [
        Message("I need to conduct a bug triage session."),
        Message(f"Focus on bugs with severity {severity_threshold} or higher that are at least {age_days} days old.")
    ]
    
    if tag:
        messages.append(Message(f"Filter to bugs tagged with: {tag}"))
    
    messages.extend([
        Message("For each bug, please determine:"),
        Message("1. Current severity assessment - is it still accurate?"),
        Message("2. Root cause category (UI, backend, data, integration, etc.)"),
        Message("3. Estimated effort (S/M/L/XL)"),
        Message("4. Priority recommendation (P0/P1/P2/P3)"),
        Message("5. Suggested assignee based on expertise area"),
        Message("Group the bugs by root cause category and provide a summary of patterns.")
    ])
    
    return messages


def feature_dependencies_analysis(
    feature_reference: str,
    check_upstream: bool = True,
    check_downstream: bool = True
) -> str:
    """Generate a prompt to analyze feature dependencies"""
    directions = []
    if check_upstream:
        directions.append("upstream (what this feature depends on)")
    if check_downstream:
        directions.append("downstream (what depends on this feature)")
    
    direction_text = " and ".join(directions)
    
    return f"""Please analyze the dependencies for feature {feature_reference}.

I need to understand the {direction_text} dependencies.

For each dependency found, provide:
1. The feature/requirement reference and name
2. The type of dependency (blocks, relates to, child of, etc.)
3. Current status of the dependent item
4. Risk assessment if the dependency is not resolved
5. Suggested mitigation strategies

Also create a visual representation using text/ASCII that shows the dependency chain.

Finally, provide recommendations on:
- Critical path items that could block {feature_reference}
- Optimal sequence for implementation
- Any circular dependencies detected
- Resource conflicts across dependent features"""


def sprint_retrospective(
    sprint_name: str,
    team_name: Optional[str] = None
) -> list[Message]:
    """Generate a prompt for sprint retrospective analysis"""
    messages = [
        Message(f"Let's conduct a retrospective analysis for sprint: {sprint_name}")
    ]
    
    if team_name:
        messages.append(Message(f"Focusing on team: {team_name}"))
    
    messages.extend([
        Message("Please analyze the sprint data and provide insights on:"),
        Message("1. **Velocity Metrics**"),
        Message("   - Planned vs completed features"),
        Message("   - Story points delivered (if available)"),
        Message("   - Carry-over items to next sprint"),
        Message("2. **Quality Indicators**"),
        Message("   - Bugs found during sprint"),
        Message("   - Features that required rework"),
        Message("   - Test coverage concerns"),
        Message("3. **Team Performance**"),
        Message("   - Individual contribution balance"),
        Message("   - Collaboration patterns"),
        Message("   - Blocker resolution time"),
        Message("4. **Process Observations**"),
        Message("   - What went well?"),
        Message("   - What could be improved?"),
        Message("   - Action items for next sprint"),
        Message("Format as a retrospective report with specific examples and actionable recommendations.")
    ])
    
    return messages


def weekly_status_report(
    project_id: str,
    week_ending: str,
    include_metrics: bool = True
) -> str:
    """Generate a prompt for creating a weekly status report"""
    prompt = f"""Please generate a comprehensive weekly status report for project {project_id} for the week ending {week_ending}.

Structure the report as follows:

## Executive Summary
- Key accomplishments this week
- Critical issues or blockers
- Overall project health (Green/Yellow/Red)

## Progress Update
- Features completed this week (with references)
- Features in progress (with % complete)
- Features starting next week

"""
    
    if include_metrics:
        prompt += """## Key Metrics
- Features delivered vs planned
- Bug discovery rate
- Team velocity trend
- Release burndown status

"""
    
    prompt += """## Risks and Issues
- New risks identified
- Existing risk status updates
- Mitigation actions needed

## Upcoming Milestones
- Next week's priorities
- Upcoming release dates
- Key decisions needed

## Team Updates
- Resource changes
- PTO/availability impacts
- Recognition/achievements

Please format this in a professional manner suitable for stakeholder distribution."""
    
    return prompt


async def idea_to_feature_conversion(
    idea_reference: str,
    target_release: str,
    ctx: Context
) -> list[Message]:
    """Generate a prompt to guide converting an idea to a feature"""
    # We can use async and access context if needed
    return [
        Message(f"I need to convert idea {idea_reference} into a feature for release {target_release}."),
        Message("Please help me by:"),
        Message("1. First, retrieve and analyze the idea details"),
        Message("2. Enhance the description with implementation details"),
        Message("3. Break down into specific requirements or tasks"),
        Message("4. Suggest appropriate feature metadata:"),
        Message("   - Feature name (refined from idea)"),
        Message("   - Initial workflow status"),
        Message("   - Tags for categorization"),
        Message("   - Effort estimation"),
        Message("   - Assignee recommendation"),
        Message("5. Create the feature creation command with all details"),
        Message("Please ensure all context from the idea is preserved and enhanced in the feature.")
    ]


def integration_checklist(
    feature_reference: str,
    integration_type: str = "API"
) -> str:
    """Generate an integration checklist for a feature"""
    return f"""Create a comprehensive integration checklist for feature {feature_reference} which involves {integration_type} integration.

Generate a checklist covering:

1. **Pre-Integration Requirements**
   - [ ] API/Interface documentation reviewed
   - [ ] Authentication method confirmed
   - [ ] Rate limits understood
   - [ ] Data formats agreed upon
   - [ ] Error handling strategy defined

2. **Implementation Checklist**
   - [ ] Connection configuration
   - [ ] Data mapping completed
   - [ ] Error scenarios handled
   - [ ] Retry logic implemented
   - [ ] Monitoring hooks added

3. **Testing Requirements**
   - [ ] Unit tests for integration logic
   - [ ] Integration tests with mock services
   - [ ] End-to-end testing plan
   - [ ] Performance testing needs
   - [ ] Failure scenario testing

4. **Deployment Considerations**
   - [ ] Environment-specific configs
   - [ ] Secrets management
   - [ ] Rollback strategy
   - [ ] Monitoring and alerts
   - [ ] Documentation updates

5. **Post-Deployment Validation**
   - [ ] Health check verification
   - [ ] Data flow validation
   - [ ] Performance benchmarks met
   - [ ] Error rates within tolerance
   - [ ] User acceptance criteria

Please customize this checklist based on the specific feature requirements and mark any items that need special attention."""