"""MCP resources for Aha! data access."""

import json
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
from fastmcp import FastMCP, Context
from client import graphql, check_auth

# This will be set by the main module
mcp: Optional[FastMCP] = None


def register_resources(mcp_instance: FastMCP):
    """Register all resources with the MCP instance"""
    global mcp
    mcp = mcp_instance
    
    # Register all resources with meaningful parameters
    mcp.resource(
        uri="aha://releases/{status}",  # status: active, all, parking-lot
        name="Releases by Status",
        description="Get releases filtered by status (active, all, parking-lot)",
        tags={"releases", "features", "planning"}
    )(releases_by_status)
    
    mcp.resource(
        uri="aha://ideas/{filter}",  # filter: review, new, all
        name="Ideas by Filter",
        description="Get ideas filtered by type (review, new, all)",
        tags={"ideas", "backlog", "planning"}
    )(ideas_by_filter)
    
    mcp.resource(
        uri="aha://work/assigned/{user_email}",
        name="Assigned Work",
        description="Get all work assigned to a specific user email",
        tags={"assignments", "work", "user", "tasks"}
    )(my_assigned_work)
    
    mcp.resource(
        uri="aha://updates/recent/{days}",
        name="Recent Updates",
        description="Get recent updates across the workspace (default: 7 days)",
        tags={"updates", "activity", "recent", "changes"}
    )(recent_updates)


async def releases_by_status(status: str = "active", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Get releases filtered by status
    
    Args:
        status: Filter type - 'active' (default), 'all', or 'parking-lot'
    
    Returns releases that are:
    - Not in parking lot
    - Either have no release date or release date is in the future
    - Includes all features for each release
    """
    auth_error = check_auth()
    if auth_error:
        return {"error": auth_error}
    
    try:
        # Query for active releases
        releases_query = """query($filters: ReleaseFilters!) {
            releases(filters: $filters, per: 50) {
                nodes {
                    id
                    referenceNum
                    name
                    startDate
                    releaseDate
                    parkingLot
                    description { htmlBody }
                    workflowStatus { id name color }
                    owner { id name email }
                    project {
                        id
                        referencePrefix
                        name
                    }
                    features(per: 100) {
                        nodes {
                            id
                            referenceNum
                            name
                            workflowStatus { id name color complete }
                            assignedToUser { id name email }
                            score
                            tags { id name color }
                        }
                        pageInfo {
                            hasNextPage
                            totalCount
                        }
                    }
                }
                pageInfo {
                    hasNextPage
                    totalCount
                }
            }
        }"""
        
        # Build filters based on status parameter
        today = datetime.now().strftime("%Y-%m-%d")
        filters = {}
        
        if status == "parking-lot":
            filters["parkingLot"] = True
        elif status == "active":
            filters["parkingLot"] = False
        # For "all", don't filter by parking lot
        
        data = await graphql(ctx, releases_query, {"filters": filters})
        
        if not data or "releases" not in data:
            return {"error": "Failed to fetch releases"}
        
        releases = data["releases"]["nodes"]
        
        # Filter releases client-side based on status
        filtered_releases = []
        for release in releases:
            # Apply status-specific filtering
            if status == "active":
                # Include if not in parking lot AND (no release date or release date is in the future)
                if not release.get("parkingLot", False) and (not release.get("releaseDate") or release["releaseDate"] >= today):
                    pass  # Will be included
                else:
                    continue
            # For "all" and "parking-lot", include everything from the query
            
            # Calculate feature statistics
                feature_stats = {
                    "total": release["features"]["pageInfo"]["totalCount"],
                    "by_status": {},
                    "completed": 0,
                    "in_progress": 0,
                    "not_started": 0
                }
                
                for feature in release["features"]["nodes"]:
                    status_name = feature["workflowStatus"]["name"]
                    is_complete = feature["workflowStatus"].get("complete", False)
                    
                    if status_name not in feature_stats["by_status"]:
                        feature_stats["by_status"][status_name] = 0
                    feature_stats["by_status"][status_name] += 1
                    
                    if is_complete:
                        feature_stats["completed"] += 1
                    elif status_name.lower() in ["in progress", "in development", "coding"]:
                        feature_stats["in_progress"] += 1
                    else:
                        feature_stats["not_started"] += 1
                
                release["feature_stats"] = feature_stats
                filtered_releases.append(release)
        
        # Sort by release date (nearest first)
        filtered_releases.sort(key=lambda r: r.get("releaseDate", "9999-12-31"))
        
        return {
            "releases": filtered_releases,
            "metadata": {
                "filter": status,
                "total_releases": len(filtered_releases),
                "total_features": sum(r["feature_stats"]["total"] for r in filtered_releases),
                "generated_at": datetime.utcnow().isoformat() + "Z"
            }
        }
        
    except Exception as e:
        return {"error": f"Failed to fetch active releases: {str(e)}"}


async def ideas_by_filter(filter: str = "review", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Get ideas filtered by type
    
    Args:
        filter: Filter type - 'review' (default), 'new', or 'all'
    
    Returns ideas that are:
    - In "New" or "Future consideration" status
    - Sorted by creation date (newest first)
    - Includes vote counts, comments, and tags
    """
    auth_error = check_auth()
    if auth_error:
        return {"error": auth_error}
    
    try:
        # Query for ideas needing review
        ideas_query = """query($filters: IdeaFilters!) {
            ideas(filters: $filters, sortBy: { field: CREATED_AT, direction: DESC }, per: 100) {
                nodes {
                    id
                    referenceNum
                    name
                    description { htmlBody }
                    createdAt
                    updatedAt
                    score
                    visibility
                    workflowStatus { id name color }
                    assignedToUser { id name email }
                    tags { id name color }
                    creator {
                        ... on User { id name email }
                        ... on IdeaUser { id name email }
                    }
                    endorsementCount
                    commentCount
                    categories { id name }
                    project {
                        id
                        referencePrefix
                        name
                    }
                }
                pageInfo {
                    hasNextPage
                    totalCount
                }
            }
        }"""
        
        # Build filters based on filter parameter
        filters = {}
        
        data = await graphql(ctx, ideas_query, {"filters": filters})
        
        if not data or "ideas" not in data:
            return {"error": "Failed to fetch ideas"}
        
        all_ideas = data["ideas"]["nodes"]
        
        # Apply filtering based on filter parameter
        if filter == "review":
            # Filter for ideas needing review
            review_statuses = ["New", "Future consideration", "Needs review", "Under consideration"]
            filtered_ideas = [
                idea for idea in all_ideas
                if idea.get("workflowStatus", {}).get("name", "").lower() in [s.lower() for s in review_statuses]
            ]
        elif filter == "new":
            # Filter for only new ideas (created in last 7 days)
            seven_days_ago = datetime.now() - timedelta(days=7)
            filtered_ideas = []
            for idea in all_ideas:
                try:
                    created_at = datetime.fromisoformat(idea["createdAt"].replace('Z', '+00:00'))
                    if created_at.replace(tzinfo=None) >= seven_days_ago:
                        filtered_ideas.append(idea)
                except:
                    pass
        else:  # filter == "all"
            filtered_ideas = all_ideas
        
        # Categorize by age
        now = datetime.now(tz=datetime.now().astimezone().tzinfo)
        for idea in filtered_ideas:
            # Parse ISO datetime string
            try:
                created_at = datetime.fromisoformat(idea["createdAt"].replace('Z', '+00:00'))
                age_days = (now - created_at).days
                if age_days <= 7:
                    idea["age_category"] = "new"
                elif age_days <= 30:
                    idea["age_category"] = "recent"
                elif age_days <= 90:
                    idea["age_category"] = "aging"
                else:
                    idea["age_category"] = "old"
                idea["age_days"] = age_days
            except (ValueError, AttributeError):
                idea["age_category"] = "unknown"
                idea["age_days"] = -1
        
        # Sort by score (if available) and then by creation date
        filtered_ideas.sort(key=lambda i: (-(i.get("score") or 0), i.get("createdAt", "")), reverse=True)
        
        # Group by status for summary
        by_status = {}
        for idea in filtered_ideas:
            status = idea["workflowStatus"]["name"]
            if status not in by_status:
                by_status[status] = 0
            by_status[status] += 1
        
        # Calculate age breakdown
        age_breakdown = {
            "new": len([i for i in filtered_ideas if i.get("age_category") == "new"]),
            "recent": len([i for i in filtered_ideas if i.get("age_category") == "recent"]),
            "aging": len([i for i in filtered_ideas if i.get("age_category") == "aging"]),
            "old": len([i for i in filtered_ideas if i.get("age_category") == "old"]),
            "unknown": len([i for i in filtered_ideas if i.get("age_category") == "unknown"])
        }
        
        return {
            "ideas": filtered_ideas,
            "metadata": {
                "filter": filter,
                "total_ideas": len(filtered_ideas),
                "by_status": by_status,
                "by_age": age_breakdown,
                "generated_at": datetime.utcnow().isoformat() + "Z"
            }
        }
        
    except Exception as e:
        return {"error": f"Failed to fetch idea backlog: {str(e)}"}


async def my_assigned_work(user_email: str = "current", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Get all work assigned to a specific user
    
    Args:
        user_email: Email of the user or "current" for authenticated user
        
    Returns work items:
    - Features
    - Requirements
    - Tasks/To-dos
    - Epics
    - Ideas
    Grouped by type and status
    """
    auth_error = check_auth()
    if auth_error:
        return {"error": auth_error}
    
    try:
        # If user_email is "current", we need to get the current user
        # For now, we'll require an explicit email
        if user_email == "current":
            return {"error": "Please specify a user email. 'current' user detection not yet implemented."}
        
        work_items = {
            "features": [],
            "requirements": [],
            "tasks": [],
            "epics": [],
            "ideas": []
        }
        
        # Query features assigned to user
        features_query = """query($assigneeEmail: String!) {
            features(filters: { assignedToUser: { emails: [$assigneeEmail] } }, per: 100) {
                nodes {
                    id
                    referenceNum
                    name
                    workflowStatus { id name color complete }
                    release {
                        id
                        referenceNum
                        name
                        releaseDate
                    }
                    dueDate
                    tags { id name color }
                    score
                    updatedAt
                }
            }
        }"""
        
        features_data = await graphql(ctx, features_query, {"assigneeEmail": user_email})
        if features_data and "features" in features_data:
            work_items["features"] = features_data["features"]["nodes"]
        
        # Query requirements assigned to user
        requirements_query = """query($assigneeEmail: String!) {
            requirements(filters: { assignedToUser: { emails: [$assigneeEmail] } }, per: 100) {
                nodes {
                    id
                    referenceNum
                    name
                    workflowStatus { id name color complete }
                    feature {
                        id
                        referenceNum
                        name
                    }
                    updatedAt
                }
            }
        }"""
        
        requirements_data = await graphql(ctx, requirements_query, {"assigneeEmail": user_email})
        if requirements_data and "requirements" in requirements_data:
            work_items["requirements"] = requirements_data["requirements"]["nodes"]
        
        # Query epics assigned to user
        epics_query = """query($assigneeEmail: String!) {
            epics(filters: { assignedToUser: { emails: [$assigneeEmail] } }, per: 100) {
                nodes {
                    id
                    referenceNum
                    name
                    workflowStatus { id name color complete }
                    release {
                        id
                        referenceNum
                        name
                    }
                    dueDate
                    updatedAt
                }
            }
        }"""
        
        epics_data = await graphql(ctx, epics_query, {"assigneeEmail": user_email})
        if epics_data and "epics" in epics_data:
            work_items["epics"] = epics_data["epics"]["nodes"]
        
        # Query ideas assigned to user
        ideas_query = """query($assigneeEmail: String!) {
            ideas(filters: { assignedToUser: { emails: [$assigneeEmail] } }, per: 100) {
                nodes {
                    id
                    referenceNum
                    name
                    workflowStatus { id name color }
                    score
                    visibility
                    updatedAt
                }
            }
        }"""
        
        ideas_data = await graphql(ctx, ideas_query, {"assigneeEmail": user_email})
        if ideas_data and "ideas" in ideas_data:
            work_items["ideas"] = ideas_data["ideas"]["nodes"]
        
        # Calculate summary statistics
        summary = {
            "total_items": sum(len(items) for items in work_items.values()),
            "by_type": {k: len(v) for k, v in work_items.items()},
            "incomplete_items": 0,
            "overdue_items": 0
        }
        
        # Check for incomplete and overdue items
        today = datetime.now().strftime("%Y-%m-%d")
        for item_type, items in work_items.items():
            for item in items:
                # Check if incomplete
                if not item.get("workflowStatus", {}).get("complete", False):
                    summary["incomplete_items"] += 1
                    
                    # Check if overdue (features and epics have due dates)
                    if item.get("dueDate") and item["dueDate"] < today:
                        summary["overdue_items"] += 1
        
        return {
            "user_email": user_email,
            "work_items": work_items,
            "summary": summary,
            "metadata": {
                "generated_at": datetime.utcnow().isoformat() + "Z"
            }
        }
        
    except Exception as e:
        return {"error": f"Failed to fetch assigned work: {str(e)}"}


async def recent_updates(days: int = 7, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Get recent updates across the workspace
    
    Args:
        days: Number of days to look back (default: 7)
        
    Returns recently updated:
    - Features
    - Ideas  
    - Releases
    - Epics
    Sorted by update time (newest first)
    """
    auth_error = check_auth()
    if auth_error:
        return {"error": auth_error}
    
    try:
        # Calculate the cutoff date
        cutoff_date = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
        
        all_updates = []
        
        # Query recently updated features
        features_query = """query($updatedSince: String!) {
            features(filters: { updatedAt: { gte: $updatedSince } }, sortBy: { field: UPDATED_AT, direction: DESC }, per: 50) {
                nodes {
                    id
                    referenceNum
                    name
                    updatedAt
                    workflowStatus { id name color }
                    assignedToUser { id name email }
                    release {
                        id
                        referenceNum
                        name
                    }
                    tags { id name color }
                }
            }
        }"""
        
        features_data = await graphql(ctx, features_query, {"updatedSince": cutoff_date})
        if features_data and "features" in features_data:
            for feature in features_data["features"]["nodes"]:
                feature["_type"] = "feature"
                all_updates.append(feature)
        
        # Query recently updated ideas
        ideas_query = """query($updatedSince: String!) {
            ideas(filters: { updatedAt: { gte: $updatedSince } }, sortBy: { field: UPDATED_AT, direction: DESC }, per: 50) {
                nodes {
                    id
                    referenceNum
                    name
                    updatedAt
                    workflowStatus { id name color }
                    assignedToUser { id name email }
                    score
                    visibility
                }
            }
        }"""
        
        ideas_data = await graphql(ctx, ideas_query, {"updatedSince": cutoff_date})
        if ideas_data and "ideas" in ideas_data:
            for idea in ideas_data["ideas"]["nodes"]:
                idea["_type"] = "idea"
                all_updates.append(idea)
        
        # Query recently updated releases
        releases_query = """query($updatedSince: String!) {
            releases(filters: { updatedAt: { gte: $updatedSince } }, sortBy: { field: UPDATED_AT, direction: DESC }, per: 50) {
                nodes {
                    id
                    referenceNum
                    name
                    updatedAt
                    releaseDate
                    parkingLot
                    workflowStatus { id name color }
                    owner { id name email }
                }
            }
        }"""
        
        releases_data = await graphql(ctx, releases_query, {"updatedSince": cutoff_date})
        if releases_data and "releases" in releases_data:
            for release in releases_data["releases"]["nodes"]:
                release["_type"] = "release"
                all_updates.append(release)
        
        # Query recently updated epics
        epics_query = """query($updatedSince: String!) {
            epics(filters: { updatedAt: { gte: $updatedSince } }, sortBy: { field: UPDATED_AT, direction: DESC }, per: 50) {
                nodes {
                    id
                    referenceNum
                    name
                    updatedAt
                    workflowStatus { id name color }
                    assignedToUser { id name email }
                    release {
                        id
                        referenceNum
                        name
                    }
                }
            }
        }"""
        
        epics_data = await graphql(ctx, epics_query, {"updatedSince": cutoff_date})
        if epics_data and "epics" in epics_data:
            for epic in epics_data["epics"]["nodes"]:
                epic["_type"] = "epic"
                all_updates.append(epic)
        
        # Sort all updates by update time
        all_updates.sort(key=lambda x: x.get("updatedAt", ""), reverse=True)
        
        # Group by day for easier consumption
        updates_by_day = {}
        for update in all_updates:
            update_date = update.get("updatedAt", "")[:10]  # Get YYYY-MM-DD
            if update_date not in updates_by_day:
                updates_by_day[update_date] = []
            updates_by_day[update_date].append(update)
        
        # Calculate summary
        summary = {
            "total_updates": len(all_updates),
            "by_type": {},
            "by_day": {day: len(items) for day, items in updates_by_day.items()}
        }
        
        for update in all_updates:
            update_type = update.get("_type", "unknown")
            if update_type not in summary["by_type"]:
                summary["by_type"][update_type] = 0
            summary["by_type"][update_type] += 1
        
        return {
            "days_back": days,
            "cutoff_date": cutoff_date,
            "updates": all_updates,
            "updates_by_day": updates_by_day,
            "summary": summary,
            "metadata": {
                "generated_at": datetime.utcnow().isoformat() + "Z"
            }
        }
        
    except Exception as e:
        return {"error": f"Failed to fetch recent updates: {str(e)}"}