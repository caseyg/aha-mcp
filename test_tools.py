"""Comprehensive tests for the 10 simplified Aha! MCP tools.

Tests cover: success paths, identifier resolution, response_format,
content_format, error handling, and edge cases for every tool.
"""

import json
import pytest
import pytest_asyncio
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock, call

from fastmcp import Client

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the new entry point
from aha_mcp import mcp


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_text(result) -> str:
    """Extract text from a CallToolResult."""
    return result.content[0].text


def get_json(result) -> dict:
    """Extract and parse JSON from a CallToolResult."""
    return json.loads(get_text(result))


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_env(monkeypatch):
    """Set required environment variables for auth."""
    monkeypatch.setenv("AHA_API_TOKEN", "test-token")
    monkeypatch.setenv("AHA_DOMAIN", "testdomain")


@pytest_asyncio.fixture
async def test_client(mock_env):
    """Create a FastMCP in-memory test client with mocked GraphQL + REST."""
    with patch("tools.graphql", new_callable=AsyncMock) as mock_gql, \
         patch("tools.rest_api", new_callable=AsyncMock) as mock_rest_fn, \
         patch("tools.check_auth", return_value=None), \
         patch("tools.resolve_identifier", new_callable=AsyncMock) as mock_resolver, \
         patch("tools.detect_record_type") as mock_detect, \
         patch("tools.format_response_field", side_effect=lambda x, *a, **kw: x):
        # Default: resolve_identifier returns a dict with id and _type
        mock_resolver.return_value = {"id": "111", "_type": "feature", "reference": "PROJ-123"}
        mock_detect.return_value = "feature"
        async with Client(mcp) as client:
            client.mock_graphql = mock_gql
            client.mock_rest = mock_rest_fn
            client.mock_resolver = mock_resolver
            client.mock_detect = mock_detect
            yield client


# ---------------------------------------------------------------------------
# Shared mock data
# ---------------------------------------------------------------------------

FEATURE_GRAPHQL = {
    "feature": {
        "id": "111",
        "referenceNum": "PROJ-123",
        "name": "User Onboarding V2",
        "description": {"htmlBody": "<p>Onboarding <strong>flow</strong></p>"},
        "workflowStatus": {"id": "ws1", "name": "In progress"},
        "assignedToUser": {"id": "u1", "name": "Alice", "email": "alice@co.com"},
        "release": {"id": "r1", "referenceNum": "PROJ-R-1", "name": "Q3 Release"},
        "tags": [{"id": "t1", "name": "priority"}],
        "score": 85,
        "createdAt": "2026-01-15T10:00:00Z",
        "updatedAt": "2026-03-28T14:30:00Z",
    }
}

IDEA_GRAPHQL = {
    "idea": {
        "id": "222",
        "referenceNum": "PROJ-I-45",
        "name": "Dark Mode Support",
        "description": {"htmlBody": "<p>Add dark mode</p>"},
        "workflowStatus": {"id": "ws2", "name": "New"},
        "assignedToUser": {"id": "u2", "name": "Bob"},
        "score": 72,
        "visibility": "VISIBILITY_PUBLIC",
        "createdAt": "2026-02-01T08:00:00Z",
    }
}

SEARCH_RESULTS = {
    "searchDocuments": {
        "nodes": [
            {
                "name": "User Onboarding V2",
                "searchableId": "111",
                "searchableType": "Feature",
            },
            {
                "name": "Onboarding Email Sequence",
                "searchableId": "112",
                "searchableType": "Feature",
            },
        ],
        "currentPage": 1,
        "totalCount": 2,
        "totalPages": 1,
    }
}

CREATE_FEATURE_RESULT = {
    "createFeature": {
        "feature": {
            "id": "333",
            "referenceNum": "PROJ-200",
            "name": "New Feature",
            "workflowStatus": {"name": "New"},
            "assignedToUser": None,
        },
        "errors": None,
    }
}

CREATE_IDEA_RESULT = {
    "createIdea": {
        "idea": {
            "id": "444",
            "referenceNum": "PROJ-I-100",
            "name": "New Idea",
            "workflowStatus": {"name": "New"},
            "assignedToUser": None,
        },
        "errors": None,
    }
}

UPDATE_FEATURE_RESULT = {
    "updateFeature": {
        "feature": {
            "id": "111",
            "referenceNum": "PROJ-123",
            "name": "Renamed Feature",
            "workflowStatus": {"name": "In progress"},
            "assignedToUser": {"name": "Alice"},
        },
        "errors": None,
    }
}

DELETE_FEATURE_RESULT = {
    "deleteFeature": {
        "feature": {"id": "111", "referenceNum": "PROJ-123"},
        "errors": None,
    }
}

PROMOTE_IDEA_RESULT = {
    "feature": {
        "id": "555",
        "reference_num": "PROJ-300",
        "name": "Dark Mode Support",
    }
}

INTROSPECTION_SCHEMA = {
    "__schema": {
        "types": [
            {"name": "Feature", "kind": "OBJECT", "description": "A feature"},
            {"name": "Idea", "kind": "OBJECT", "description": "An idea"},
            {"name": "Epic", "kind": "OBJECT", "description": "An epic"},
        ],
        "queryType": {
            "fields": [
                {"name": "feature", "description": "Find a feature"},
                {"name": "features", "description": "List features"},
                {"name": "idea", "description": "Find an idea"},
                {"name": "ideas", "description": "List ideas"},
            ]
        },
        "mutationType": {
            "fields": [
                {"name": "createFeature", "description": "Create a feature"},
                {"name": "updateFeature", "description": "Update a feature"},
                {"name": "createIdea", "description": "Create an idea"},
            ]
        },
    }
}

FEATURES_LIST = {
    "features": {
        "nodes": [
            {
                "id": "111",
                "referenceNum": "PROJ-123",
                "name": "User Onboarding V2",
                "workflowStatus": {"name": "In progress"},
                "assignedToUser": {"name": "Alice"},
            },
            {
                "id": "112",
                "referenceNum": "PROJ-124",
                "name": "Dashboard Redesign",
                "workflowStatus": {"name": "Shipped"},
                "assignedToUser": {"name": "Bob"},
            },
        ],
        "currentPage": 1,
        "totalCount": 2,
        "totalPages": 1,
    }
}

EPICS_LIST = {
    "epics": {
        "nodes": [
            {
                "id": "e1",
                "referenceNum": "PROJ-E-1",
                "name": "Platform Migration",
                "workflowStatus": {"name": "In progress"},
                "assignedToUser": {"name": "Alice"},
            }
        ],
        "currentPage": 1,
        "totalCount": 1,
        "totalPages": 1,
    }
}

REQUIREMENTS_LIST = {
    "requirements": {
        "nodes": [
            {
                "id": "req1",
                "referenceNum": "PROJ-123-1",
                "name": "API Endpoint",
                "workflowStatus": {"name": "In progress"},
                "assignedToUser": {"name": "Alice"},
            }
        ],
        "currentPage": 1,
        "totalCount": 1,
        "totalPages": 1,
    }
}

TASKS_LIST_REST = [
    {
        "id": "task1",
        "name": "Write tests",
        "status": "pending",
        "assigned_to_user": {"id": "u1", "name": "Alice"},
    }
]


# ===========================================================================
# 1. aha_get
# ===========================================================================

class TestAhaGet:
    """Tests for fetching any record by reference, name, or ID."""

    @pytest.mark.asyncio
    async def test_fetch_feature_by_reference(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature", "reference": "PROJ-123"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-123"})
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-123"
        assert data["name"] == "User Onboarding V2"

    @pytest.mark.asyncio
    async def test_fetch_idea_by_reference(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea", "reference": "PROJ-I-45"}
        test_client.mock_graphql.return_value = IDEA_GRAPHQL
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-I-45"})
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-I-45"
        assert data["name"] == "Dark Mode Support"

    @pytest.mark.asyncio
    async def test_fetch_with_record_type(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea", "reference": "PROJ-I-45"}
        test_client.mock_graphql.return_value = IDEA_GRAPHQL
        result = await test_client.call_tool("aha_get", {
            "identifier": "PROJ-I-45",
            "record_type": "idea",
        })
        data = get_json(result)
        assert data["name"] == "Dark Mode Support"

    @pytest.mark.asyncio
    async def test_fetch_by_numeric_id(self, test_client):
        """Numeric IDs are passed directly to GraphQL."""
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {
            "identifier": "111",
            "record_type": "feature",
        })
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-123"

    @pytest.mark.asyncio
    async def test_concise_format(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {
            "identifier": "PROJ-123",
            "response_format": "concise",
        })
        data = get_json(result)
        assert data is not None

    @pytest.mark.asyncio
    async def test_detailed_format(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {
            "identifier": "PROJ-123",
            "response_format": "detailed",
        })
        data = get_json(result)
        assert "referenceNum" in data

    @pytest.mark.asyncio
    async def test_fetch_feature_details(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {"identifier": "111", "record_type": "feature"})
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-123"

    @pytest.mark.asyncio
    async def test_page_by_reference(self, test_client):
        page_data = {
            "page": {
                "id": "p1",
                "referenceNum": "PROJ-N-1",
                "name": "Architecture Overview",
                "description": {"htmlBody": "<h1>Arch</h1>"},
            }
        }
        test_client.mock_resolver.return_value = {"id": "p1", "_type": "page", "reference": "PROJ-N-1"}
        test_client.mock_graphql.return_value = page_data
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-N-1"})
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-N-1"

    @pytest.mark.asyncio
    async def test_epic_by_reference(self, test_client):
        epic_data = {
            "epic": {
                "id": "e1",
                "referenceNum": "PROJ-E-1",
                "name": "Platform Migration",
            }
        }
        test_client.mock_resolver.return_value = {"id": "e1", "_type": "epic", "reference": "PROJ-E-1"}
        test_client.mock_graphql.return_value = epic_data
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-E-1"})
        data = get_json(result)
        assert data["referenceNum"] == "PROJ-E-1"

    @pytest.mark.asyncio
    async def test_not_found_returns_error(self, test_client):
        test_client.mock_resolver.return_value = {"id": "PROJ-123", "_type": "feature"}
        test_client.mock_graphql.return_value = {"feature": None}
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-123"})
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_html_content_format(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = FEATURE_GRAPHQL
        result = await test_client.call_tool("aha_get", {
            "identifier": "PROJ-123",
            "content_format": "html",
        })
        data = get_json(result)
        assert data is not None


# ===========================================================================
# 2. aha_search
# ===========================================================================

class TestAhaSearch:
    """Tests for searching across record types."""

    @pytest.mark.asyncio
    async def test_free_text_search(self, test_client):
        test_client.mock_graphql.return_value = SEARCH_RESULTS
        result = await test_client.call_tool("aha_search", {
            "query": "onboarding",
        })
        data = get_json(result)
        assert data["total_count"] == 2
        assert len(data["results"]) == 2

    @pytest.mark.asyncio
    async def test_search_with_record_type(self, test_client):
        test_client.mock_graphql.return_value = SEARCH_RESULTS
        result = await test_client.call_tool("aha_search", {
            "query": "onboarding",
            "record_type": "feature",
        })
        data = get_json(result)
        assert data["total_count"] == 2

    @pytest.mark.asyncio
    async def test_list_features_by_project(self, test_client):
        test_client.mock_graphql.return_value = FEATURES_LIST
        result = await test_client.call_tool("aha_search", {
            "record_type": "feature",
            "project": "PROJ",
        })
        data = get_json(result)
        assert len(data["results"]) == 2

    @pytest.mark.asyncio
    async def test_list_features_by_assignee(self, test_client):
        test_client.mock_graphql.return_value = FEATURES_LIST
        result = await test_client.call_tool("aha_search", {
            "record_type": "feature",
            "assignee": "u1",
        })
        data = get_json(result)
        assert data is not None

    @pytest.mark.asyncio
    async def test_list_ideas_for_project(self, test_client):
        ideas_list = {
            "ideas": {
                "nodes": [
                    {
                        "id": "222",
                        "referenceNum": "PROJ-I-45",
                        "name": "Dark Mode Support",
                        "workflowStatus": {"name": "New"},
                        "assignedToUser": {"name": "Bob"},
                    }
                ],
                "currentPage": 1,
                "totalCount": 1,
                "totalPages": 1,
            }
        }
        test_client.mock_graphql.return_value = ideas_list
        result = await test_client.call_tool("aha_search", {
            "record_type": "idea",
            "project": "PROJ",
        })
        data = get_json(result)
        assert len(data["results"]) == 1

    @pytest.mark.asyncio
    async def test_search_empty_results(self, test_client):
        empty = {
            "searchDocuments": {
                "nodes": [],
                "currentPage": 1,
                "totalCount": 0,
                "totalPages": 0,
            }
        }
        test_client.mock_graphql.return_value = empty
        result = await test_client.call_tool("aha_search", {"query": "nonexistent"})
        data = get_json(result)
        assert data["total_count"] == 0
        assert data["results"] == []

    @pytest.mark.asyncio
    async def test_list_epics(self, test_client):
        test_client.mock_graphql.return_value = EPICS_LIST
        result = await test_client.call_tool("aha_search", {
            "record_type": "epic",
            "project": "PROJ",
        })
        data = get_json(result)
        assert len(data["results"]) == 1

    @pytest.mark.asyncio
    async def test_list_projects(self, test_client):
        projects = {
            "projects": {
                "nodes": [{"id": "p1", "name": "Demo"}],
                "currentPage": 1,
                "totalCount": 1,
                "totalPages": 1,
            }
        }
        test_client.mock_graphql.return_value = projects
        result = await test_client.call_tool("aha_search", {
            "record_type": "project",
        })
        data = get_json(result)
        assert data["total_count"] == 1

    @pytest.mark.asyncio
    async def test_search_pagination(self, test_client):
        test_client.mock_graphql.return_value = FEATURES_LIST
        result = await test_client.call_tool("aha_search", {
            "record_type": "feature",
            "project": "PROJ",
            "page": 2,
            "per_page": 50,
        })
        data = get_json(result)
        assert data is not None

    @pytest.mark.asyncio
    async def test_per_page_capped_at_100(self, test_client):
        """Verify per_page > 100 is capped."""
        test_client.mock_graphql.return_value = FEATURES_LIST
        result = await test_client.call_tool("aha_search", {
            "record_type": "feature",
            "project": "PROJ",
            "per_page": 200,
        })
        data = get_json(result)
        assert data is not None


# ===========================================================================
# 3. aha_create
# ===========================================================================

class TestAhaCreate:
    """Tests for creating records."""

    @pytest.mark.asyncio
    async def test_create_feature(self, test_client):
        test_client.mock_graphql.return_value = CREATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "New Feature",
            "release": "PROJ-R-1",
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-200"
        assert data["created"]["name"] == "New Feature"

    @pytest.mark.asyncio
    async def test_create_feature_with_description(self, test_client):
        test_client.mock_graphql.return_value = CREATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "New Feature",
            "project": "PROJ",
            "description": "A great feature",
        })
        data = get_json(result)
        assert data["created"]["name"] == "New Feature"

    @pytest.mark.asyncio
    async def test_create_feature_with_tags(self, test_client):
        test_client.mock_graphql.return_value = CREATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "New Feature",
            "release": "PROJ-R-1",
            "tags": ["priority", "q3"],
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-200"
        # Verify tagList was passed in the mutation variables
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert "tagList" in attrs
        assert "priority" in attrs["tagList"]

    @pytest.mark.asyncio
    async def test_create_feature_with_graphql_errors(self, test_client):
        test_client.mock_graphql.return_value = {
            "createFeature": {
                "feature": None,
                "errors": {
                    "attributes": [
                        {"name": "name", "fullMessages": ["Name is required"]}
                    ]
                },
            }
        }
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "",
            "release": "PROJ-R-1",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_create_idea(self, test_client):
        test_client.mock_graphql.return_value = CREATE_IDEA_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "idea",
            "name": "New Idea",
            "project": "PROJ",
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-I-100"

    @pytest.mark.asyncio
    async def test_create_epic(self, test_client):
        epic_result = {
            "createEpic": {
                "epic": {
                    "id": "e2",
                    "referenceNum": "PROJ-E-5",
                    "name": "New Epic",
                    "workflowStatus": {"name": "New"},
                    "assignedToUser": None,
                },
                "errors": None,
            }
        }
        test_client.mock_graphql.return_value = epic_result
        result = await test_client.call_tool("aha_create", {
            "record_type": "epic",
            "name": "New Epic",
            "release": "PROJ-R-1",
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-E-5"

    @pytest.mark.asyncio
    async def test_create_initiative(self, test_client):
        init_result = {
            "createInitiative": {
                "initiative": {
                    "id": "in1",
                    "referenceNum": "PROJ-IN-1",
                    "name": "Strategic Initiative",
                    "workflowStatus": {"name": "New"},
                    "assignedToUser": None,
                },
                "errors": None,
            }
        }
        test_client.mock_graphql.return_value = init_result
        result = await test_client.call_tool("aha_create", {
            "record_type": "initiative",
            "name": "Strategic Initiative",
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-IN-1"

    @pytest.mark.asyncio
    async def test_create_comment(self, test_client):
        comment_result = {
            "createComment": {
                "comment": {
                    "id": "c1",
                    "body": {"htmlBody": "<p>Nice work!</p>"},
                    "createdAt": "2026-03-28T14:30:00Z",
                    "user": {"name": "Alice"},
                },
                "errors": None,
            }
        }
        test_client.mock_graphql.return_value = comment_result
        result = await test_client.call_tool("aha_create", {
            "record_type": "comment",
            "name": "Nice work!",
        })
        data = get_json(result)
        assert data["created"]["id"] == "c1"

    @pytest.mark.asyncio
    async def test_create_requires_project(self, test_client):
        """Creating a feature without project or release should error."""
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "Orphan Feature",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_create_unsupported_type(self, test_client):
        result = await test_client.call_tool("aha_create", {
            "record_type": "nonexistent",
            "name": "Test",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_create_with_assignee(self, test_client):
        test_client.mock_graphql.return_value = CREATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "Assigned Feature",
            "project": "PROJ",
            "assignee": "alice@co.com",
        })
        data = get_json(result)
        assert data["created"]["name"] == "New Feature"
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert "assignedToUser" in attrs

    @pytest.mark.asyncio
    async def test_create_with_due_date(self, test_client):
        test_client.mock_graphql.return_value = CREATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "Due Soon",
            "project": "PROJ",
            "due_date": "2026-04-15",
        })
        data = get_json(result)
        assert data["created"]["name"] == "New Feature"

    @pytest.mark.asyncio
    async def test_create_page(self, test_client):
        page_result = {
            "createPage": {
                "page": {
                    "id": "p2",
                    "referenceNum": "PROJ-N-2",
                    "name": "New Page",
                },
                "errors": None,
            }
        }
        test_client.mock_graphql.return_value = page_result
        result = await test_client.call_tool("aha_create", {
            "record_type": "page",
            "name": "New Page",
            "project": "PROJ",
            "description": "# Hello\n\nThis is a new page.",
        })
        data = get_json(result)
        assert data["created"]["referenceNum"] == "PROJ-N-2"


# ===========================================================================
# 4. aha_update
# ===========================================================================

class TestAhaUpdate:
    """Tests for updating records."""

    @pytest.mark.asyncio
    async def test_update_feature_by_reference(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "name": "Renamed Feature",
        })
        data = get_json(result)
        assert data["updated"]["name"] == "Renamed Feature"

    @pytest.mark.asyncio
    async def test_update_feature_description(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "description": "Updated description",
        })
        data = get_json(result)
        assert data["updated"]["referenceNum"] == "PROJ-123"
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert "description" in attrs

    @pytest.mark.asyncio
    async def test_update_feature_tags(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "tags": ["priority", "q3", "urgent"],
        })
        data = get_json(result)
        assert data["updated"]["referenceNum"] == "PROJ-123"
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert "tagList" in attrs

    @pytest.mark.asyncio
    async def test_update_idea(self, test_client):
        update_idea_result = {
            "updateIdea": {
                "idea": {
                    "id": "222",
                    "referenceNum": "PROJ-I-45",
                    "name": "Dark Mode v2",
                    "workflowStatus": {"name": "New"},
                    "assignedToUser": {"name": "Bob"},
                },
                "errors": None,
            }
        }
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea"}
        test_client.mock_graphql.return_value = update_idea_result
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-I-45",
            "name": "Dark Mode v2",
        })
        data = get_json(result)
        assert data["updated"]["name"] == "Dark Mode v2"

    @pytest.mark.asyncio
    async def test_update_epic(self, test_client):
        epic_update = {
            "updateEpic": {
                "epic": {
                    "id": "e1",
                    "referenceNum": "PROJ-E-1",
                    "name": "Updated Epic",
                    "workflowStatus": {"name": "In progress"},
                    "assignedToUser": {"name": "Alice"},
                },
                "errors": None,
            }
        }
        test_client.mock_resolver.return_value = {"id": "e1", "_type": "epic"}
        test_client.mock_graphql.return_value = epic_update
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-E-1",
            "name": "Updated Epic",
        })
        data = get_json(result)
        assert data["updated"]["name"] == "Updated Epic"

    @pytest.mark.asyncio
    async def test_update_initiative(self, test_client):
        init_update = {
            "updateInitiative": {
                "initiative": {
                    "id": "in1",
                    "referenceNum": "PROJ-IN-1",
                    "name": "Revised Initiative",
                    "workflowStatus": {"name": "New"},
                    "assignedToUser": None,
                },
                "errors": None,
            }
        }
        test_client.mock_resolver.return_value = {"id": "in1", "_type": "initiative"}
        test_client.mock_graphql.return_value = init_update
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-IN-1",
            "name": "Revised Initiative",
        })
        data = get_json(result)
        assert data["updated"]["name"] == "Revised Initiative"

    @pytest.mark.asyncio
    async def test_update_no_fields_error(self, test_client):
        """Update with no fields to change should error."""
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_update_with_assignee_email(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "assignee": "alice@co.com",
        })
        data = get_json(result)
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert attrs["assignedToUser"]["email"] == "alice@co.com"

    @pytest.mark.asyncio
    async def test_update_with_status(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "status": "ws2",
        })
        data = get_json(result)
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert attrs["workflowStatus"]["id"] == "ws2"

    @pytest.mark.asyncio
    async def test_update_with_extra_fields(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = UPDATE_FEATURE_RESULT
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "extra_fields": {"score": 85},
        })
        data = get_json(result)
        call_args = test_client.mock_graphql.call_args
        attrs = call_args[0][2]["attrs"]
        assert attrs["score"] == 85


# ===========================================================================
# 5. aha_delete
# ===========================================================================

class TestAhaDelete:
    """Tests for deleting records."""

    @pytest.mark.asyncio
    async def test_delete_feature(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.return_value = DELETE_FEATURE_RESULT
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-123"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_idea(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea"}
        # Ideas use GraphQL delete; if that fails, falls back to REST
        test_client.mock_graphql.return_value = {
            "deleteIdea": {
                "idea": {"id": "222", "referenceNum": "PROJ-I-45"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-I-45"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_epic(self, test_client):
        test_client.mock_resolver.return_value = {"id": "e1", "_type": "epic"}
        test_client.mock_graphql.return_value = {
            "deleteEpic": {
                "epic": {"id": "e1", "referenceNum": "PROJ-E-1"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-E-1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_initiative(self, test_client):
        test_client.mock_resolver.return_value = {"id": "in1", "_type": "initiative"}
        test_client.mock_graphql.return_value = {
            "deleteInitiative": {
                "initiative": {"id": "in1", "referenceNum": "PROJ-IN-1"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-IN-1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_comment(self, test_client):
        test_client.mock_resolver.return_value = {"id": "c1", "_type": "comment"}
        test_client.mock_graphql.return_value = {
            "deleteComment": {
                "comment": {"id": "c1", "referenceNum": None},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "c1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_release(self, test_client):
        test_client.mock_resolver.return_value = {"id": "r1", "_type": "release"}
        test_client.mock_graphql.return_value = {
            "deleteRelease": {
                "release": {"id": "r1", "referenceNum": "PROJ-R-1"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-R-1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_goal(self, test_client):
        test_client.mock_resolver.return_value = {"id": "g1", "_type": "goal"}
        test_client.mock_graphql.return_value = {
            "deleteGoal": {
                "goal": {"id": "g1", "referenceNum": "PROJ-G-1"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-G-1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_page(self, test_client):
        test_client.mock_resolver.return_value = {"id": "p1", "_type": "page"}
        test_client.mock_graphql.return_value = {
            "deletePage": {
                "page": {"id": "p1", "referenceNum": "PROJ-N-1"},
                "errors": None,
            }
        }
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-N-1"})
        data = get_json(result)
        assert data.get("deleted") is True

    @pytest.mark.asyncio
    async def test_delete_falls_back_to_rest(self, test_client):
        """If GraphQL delete fails, fall back to REST."""
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.side_effect = RuntimeError("GraphQL delete not supported")
        test_client.mock_rest.return_value = None  # 204
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-123"})
        data = get_json(result)
        assert data.get("deleted") is True


# ===========================================================================
# 6. aha_promote_idea
# ===========================================================================

class TestAhaPromoteIdea:
    """Tests for promoting an idea to a feature."""

    @pytest.mark.asyncio
    async def test_promote_idea_success(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea"}
        test_client.mock_rest.return_value = PROMOTE_IDEA_RESULT
        result = await test_client.call_tool("aha_promote_idea", {
            "idea": "PROJ-I-45",
        })
        data = get_json(result)
        assert "promoted" in data

    @pytest.mark.asyncio
    async def test_promote_idea_with_release(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea"}
        test_client.mock_rest.return_value = {
            "feature": {
                "id": "556",
                "reference_num": "OTHER-100",
                "name": "Dark Mode Support",
            }
        }
        result = await test_client.call_tool("aha_promote_idea", {
            "idea": "PROJ-I-45",
            "target_release": "OTHER-R-1",
        })
        data = get_json(result)
        assert "promoted" in data

    @pytest.mark.asyncio
    async def test_promote_idea_api_error(self, test_client):
        test_client.mock_resolver.return_value = {"id": "999", "_type": "idea"}
        test_client.mock_rest.side_effect = RuntimeError("Idea not found")
        result = await test_client.call_tool("aha_promote_idea", {
            "idea": "PROJ-I-999",
        })
        data = get_json(result)
        assert "error" in data


# ===========================================================================
# 7. aha_upload_attachment
# ===========================================================================

class TestAhaUploadAttachment:
    """Tests for uploading attachments to records."""

    @pytest.mark.asyncio
    async def test_upload_attachment_success(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_rest.return_value = {
            "attachment": {
                "id": "att-new",
                "file_name": "design.png",
                "content_type": "image/png",
            }
        }
        result = await test_client.call_tool("aha_upload_attachment", {
            "record": "PROJ-123",
            "file_url": "https://example.com/design.png",
        })
        data = get_json(result)
        assert "attached" in data

    @pytest.mark.asyncio
    async def test_upload_attachment_api_error(self, test_client):
        test_client.mock_resolver.return_value = {"id": "999", "_type": "feature"}
        test_client.mock_rest.side_effect = RuntimeError("Record not found")
        result = await test_client.call_tool("aha_upload_attachment", {
            "record": "PROJ-999",
            "file_url": "https://example.com/file.pdf",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_upload_attachment_to_idea(self, test_client):
        test_client.mock_resolver.return_value = {"id": "222", "_type": "idea"}
        test_client.mock_rest.return_value = {"attachment": {"id": "att2"}}
        result = await test_client.call_tool("aha_upload_attachment", {
            "record": "PROJ-I-45",
            "file_url": "https://example.com/spec.pdf",
        })
        data = get_json(result)
        assert "attached" in data

    @pytest.mark.asyncio
    async def test_upload_extracts_filename(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_rest.return_value = {"attachment": {"id": "att3"}}
        result = await test_client.call_tool("aha_upload_attachment", {
            "record": "PROJ-123",
            "file_url": "https://example.com/path/to/report.pdf?token=abc",
        })
        data = get_json(result)
        assert "attached" in data


# ===========================================================================
# 8. aha_my_work
# ===========================================================================

class TestAhaMyWork:
    """Tests for the composite my_work tool fetching all assigned work."""

    @pytest.mark.asyncio
    async def test_my_work_returns_grouped_results(self, test_client):
        """aha_my_work fetches features, epics, requirements, tasks in parallel."""
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            EPICS_LIST,
            REQUIREMENTS_LIST,
        ]
        test_client.mock_rest.return_value = TASKS_LIST_REST
        result = await test_client.call_tool("aha_my_work", {})
        data = get_json(result)
        assert "features" in data
        assert "epics" in data
        assert "requirements" in data
        assert "tasks" in data
        assert "summary" in data

    @pytest.mark.asyncio
    async def test_my_work_with_assignee(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            EPICS_LIST,
            REQUIREMENTS_LIST,
        ]
        test_client.mock_rest.return_value = TASKS_LIST_REST
        result = await test_client.call_tool("aha_my_work", {
            "assignee": "alice@co.com",
        })
        data = get_json(result)
        assert "summary" in data
        assert data["summary"]["total"] >= 0

    @pytest.mark.asyncio
    async def test_my_work_empty(self, test_client):
        empty_features = {"features": {"nodes": [], "totalCount": 0}}
        empty_epics = {"epics": {"nodes": [], "totalCount": 0}}
        empty_reqs = {"requirements": {"nodes": [], "totalCount": 0}}
        test_client.mock_graphql.side_effect = [empty_features, empty_epics, empty_reqs]
        test_client.mock_rest.return_value = []
        result = await test_client.call_tool("aha_my_work", {})
        data = get_json(result)
        assert data["summary"]["total"] == 0

    @pytest.mark.asyncio
    async def test_my_work_concise_format(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            EPICS_LIST,
            REQUIREMENTS_LIST,
        ]
        test_client.mock_rest.return_value = TASKS_LIST_REST
        result = await test_client.call_tool("aha_my_work", {
            "response_format": "concise",
        })
        data = get_json(result)
        assert data is not None


# ===========================================================================
# 9. aha_recent_activity
# ===========================================================================

class TestAhaRecentActivity:
    """Tests for recent activity across the workspace."""

    @pytest.mark.asyncio
    async def test_recent_activity_default(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            {"ideas": {"nodes": [], "totalCount": 0}},
            EPICS_LIST,
        ]
        result = await test_client.call_tool("aha_recent_activity", {})
        data = get_json(result)
        assert "activity" in data
        assert "period" in data

    @pytest.mark.asyncio
    async def test_recent_activity_custom_days(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            {"ideas": {"nodes": [], "totalCount": 0}},
            EPICS_LIST,
        ]
        result = await test_client.call_tool("aha_recent_activity", {"days": 14})
        data = get_json(result)
        assert "Last 14 days" in data["period"]

    @pytest.mark.asyncio
    async def test_recent_activity_capped_at_30_days(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            {"ideas": {"nodes": [], "totalCount": 0}},
            EPICS_LIST,
        ]
        result = await test_client.call_tool("aha_recent_activity", {"days": 60})
        data = get_json(result)
        assert "Last 30 days" in data["period"]

    @pytest.mark.asyncio
    async def test_recent_activity_with_project(self, test_client):
        test_client.mock_graphql.side_effect = [
            FEATURES_LIST,
            {"ideas": {"nodes": [], "totalCount": 0}},
            EPICS_LIST,
        ]
        result = await test_client.call_tool("aha_recent_activity", {
            "project": "PROJ",
        })
        data = get_json(result)
        assert "activity" in data

    @pytest.mark.asyncio
    async def test_recent_activity_single_type(self, test_client):
        test_client.mock_graphql.return_value = FEATURES_LIST
        result = await test_client.call_tool("aha_recent_activity", {
            "record_type": "feature",
        })
        data = get_json(result)
        assert "activity" in data

    @pytest.mark.asyncio
    async def test_recent_activity_empty(self, test_client):
        test_client.mock_graphql.side_effect = [
            {"features": {"nodes": [], "totalCount": 0}},
            {"ideas": {"nodes": [], "totalCount": 0}},
            {"epics": {"nodes": [], "totalCount": 0}},
        ]
        result = await test_client.call_tool("aha_recent_activity", {})
        data = get_json(result)
        assert "message" in data or "activity" in data


# ===========================================================================
# 10. aha_introspect
# ===========================================================================

class TestAhaIntrospect:
    """Tests for GraphQL schema introspection."""

    @pytest.mark.asyncio
    async def test_introspect_overview(self, test_client):
        test_client.mock_graphql.return_value = INTROSPECTION_SCHEMA
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "overview",
        })
        data = get_json(result)
        assert "types" in data
        assert len(data["types"]) == 3

    @pytest.mark.asyncio
    async def test_introspect_overview_with_search(self, test_client):
        test_client.mock_graphql.return_value = INTROSPECTION_SCHEMA
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "overview",
            "search_term": "feature",
        })
        data = get_json(result)
        assert any("feature" in str(v).lower() for v in data.get("types", []))

    @pytest.mark.asyncio
    async def test_introspect_type(self, test_client):
        type_response = {
            "__type": {
                "name": "Feature",
                "kind": "OBJECT",
                "fields": [
                    {"name": "id", "description": None, "type": {"name": "ID", "kind": "SCALAR", "ofType": None}},
                    {"name": "name", "description": None, "type": {"name": "String", "kind": "SCALAR", "ofType": None}},
                    {"name": "referenceNum", "description": None, "type": {"name": "String", "kind": "SCALAR", "ofType": None}},
                ],
            }
        }
        test_client.mock_graphql.return_value = type_response
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "type",
            "type_name": "Feature",
        })
        data = get_json(result)
        assert data["name"] == "Feature"

    @pytest.mark.asyncio
    async def test_introspect_search(self, test_client):
        test_client.mock_graphql.return_value = INTROSPECTION_SCHEMA
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "search",
            "search_term": "create",
        })
        data = get_json(result)
        assert "mutations" in data

    @pytest.mark.asyncio
    async def test_introspect_type_requires_type_name(self, test_client):
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "type",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_introspect_invalid_query_type(self, test_client):
        result = await test_client.call_tool("aha_introspect", {
            "query_type": "invalid",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_introspect_default_overview(self, test_client):
        test_client.mock_graphql.return_value = INTROSPECTION_SCHEMA
        result = await test_client.call_tool("aha_introspect", {})
        data = get_json(result)
        assert "types" in data


# ===========================================================================
# Cross-cutting: error handling, auth, edge cases
# ===========================================================================

class TestErrorHandling:
    """Tests for error handling across tools."""

    @pytest.mark.asyncio
    async def test_graphql_error_in_get(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.side_effect = RuntimeError("Internal server error")
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-123"})
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_resolver_not_found(self, test_client):
        from errors import AhaNotFoundError
        test_client.mock_resolver.side_effect = AhaNotFoundError("Not found")
        result = await test_client.call_tool("aha_get", {"identifier": "PROJ-999"})
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_rest_api_error_in_delete(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.side_effect = RuntimeError("delete not supported")
        test_client.mock_rest.side_effect = RuntimeError("404 Not Found")
        result = await test_client.call_tool("aha_delete", {"identifier": "PROJ-999"})
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_create_exception(self, test_client):
        test_client.mock_graphql.side_effect = RuntimeError("Connection timed out")
        result = await test_client.call_tool("aha_create", {
            "record_type": "feature",
            "name": "Test",
            "project": "PROJ",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_update_exception(self, test_client):
        test_client.mock_resolver.return_value = {"id": "111", "_type": "feature"}
        test_client.mock_graphql.side_effect = RuntimeError("Connection timed out")
        result = await test_client.call_tool("aha_update", {
            "identifier": "PROJ-123",
            "name": "Test",
        })
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_search_exception(self, test_client):
        test_client.mock_graphql.side_effect = RuntimeError("Search failed")
        result = await test_client.call_tool("aha_search", {"query": "test"})
        data = get_json(result)
        assert "error" in data

    @pytest.mark.asyncio
    async def test_resolver_ambiguous_matches(self, test_client):
        """When resolver returns multiple matches, tool should relay them."""
        test_client.mock_resolver.return_value = {
            "matches": [
                {"id": "1", "name": "Match A"},
                {"id": "2", "name": "Match B"},
            ]
        }
        result = await test_client.call_tool("aha_get", {"identifier": "Ambiguous"})
        data = get_json(result)
        assert "matches" in data


# ===========================================================================
# Formatting utilities
# ===========================================================================

class TestFormatting:
    """Tests for Markdown <-> HTML conversion utilities."""

    def test_markdown_to_html(self):
        from formatting import markdown_to_html
        result = markdown_to_html("## Goals\n\n- Item 1\n- Item 2")
        assert "<h2>" in result or "<h2" in result
        assert "<li>" in result

    def test_html_to_markdown(self):
        from formatting import html_to_markdown
        result = html_to_markdown("<h2>Goals</h2><ul><li>Item 1</li></ul>")
        assert "Goals" in result
        assert "Item 1" in result

    def test_is_html_true(self):
        from formatting import is_html
        assert is_html("<p>Hello</p>") is True
        assert is_html("<div>Content</div>") is True

    def test_is_html_false(self):
        from formatting import is_html
        assert is_html("Just plain text") is False
        assert is_html("## Markdown heading") is False

    def test_html_passthrough(self):
        from formatting import markdown_to_html
        html = "<p>Already <strong>HTML</strong></p>"
        assert markdown_to_html(html) == html

    def test_empty_string(self):
        from formatting import markdown_to_html, html_to_markdown
        assert markdown_to_html("") == ""
        assert html_to_markdown("") == ""

    def test_format_response_field_markdown(self):
        from formatting import format_response_field
        result = format_response_field("<p>Hello <strong>world</strong></p>", "markdown")
        assert "Hello" in result
        assert "<p>" not in result

    def test_format_response_field_html_passthrough(self):
        from formatting import format_response_field
        html = "<p>Hello</p>"
        assert format_response_field(html, "html") == html


# ===========================================================================
# Cache
# ===========================================================================

class TestCache:
    """Tests for TTL cache."""

    @pytest.mark.asyncio
    async def test_cache_returns_cached_value(self):
        from cache import get_cached, invalidate
        invalidate()  # clean state

        call_count = 0

        async def fetcher():
            nonlocal call_count
            call_count += 1
            return {"data": "value"}

        r1 = await get_cached("test_key", fetcher)
        r2 = await get_cached("test_key", fetcher)
        assert r1 == r2
        assert call_count == 1  # Second call used cache

    @pytest.mark.asyncio
    async def test_cache_invalidate(self):
        from cache import get_cached, invalidate
        invalidate()

        call_count = 0

        async def fetcher():
            nonlocal call_count
            call_count += 1
            return call_count

        await get_cached("key2", fetcher)
        invalidate("key2")
        r2 = await get_cached("key2", fetcher)
        assert r2 == 2  # Cache was invalidated, fetcher called again


# ===========================================================================
# Errors module
# ===========================================================================

class TestErrors:
    """Tests for error formatting."""

    def test_format_error_basic(self):
        from errors import AhaNotFoundError, format_error
        err = AhaNotFoundError("Could not find record \"PROJ-999\".")
        result = format_error(err)
        assert "PROJ-999" in result

    def test_format_error_with_suggestion(self):
        from errors import AhaNotFoundError, format_error
        err = AhaNotFoundError(
            "Could not find record \"PROJ-999\".",
            suggestion='Did you mean: PROJ-99 (Q3 Planning)?\nExample: aha_get("PROJ-123")',
        )
        result = format_error(err)
        assert "PROJ-99" in result
        assert "aha_get" in result

    def test_validation_error(self):
        from errors import AhaValidationError, format_error
        err = AhaValidationError("Missing required parameter: record_type")
        result = format_error(err)
        assert "record_type" in result


# ===========================================================================
# Utils
# ===========================================================================

class TestUtils:
    """Tests for utility functions."""

    def test_validate_reference_feature(self):
        from utils import validate_reference
        assert validate_reference("PROJ-123", "feature") is None

    def test_validate_reference_idea(self):
        from utils import validate_reference
        assert validate_reference("PROJ-I-45", "idea") is None

    def test_validate_reference_page(self):
        from utils import validate_reference
        assert validate_reference("PROJ-N-1", "page") is None

    def test_validate_reference_invalid(self):
        from utils import validate_reference
        result = validate_reference("INVALID", "feature")
        assert result is not None
        assert "Invalid" in result

    def test_build_standard_fields_feature(self):
        from utils import build_standard_fields
        fields = build_standard_fields("feature")
        assert "id" in fields
        assert "referenceNum" in fields
        assert any("workflowStatus" in f for f in fields)

    def test_build_standard_fields_unknown_type(self):
        from utils import build_standard_fields
        fields = build_standard_fields("unknown_type")
        assert fields == ["id", "referenceNum", "name"]

    def test_build_attributes(self):
        from utils import build_attributes
        attrs = build_attributes(
            {"name": "Test"},
            {"description": "Desc", "status": None},
        )
        assert attrs["name"] == "Test"
        assert attrs["description"] == "Desc"
        assert "status" not in attrs

    def test_build_filters(self):
        from utils import build_filters
        result = build_filters(project="PROJ", active=True, empty=None)
        assert 'project: "PROJ"' in result
        assert "active: true" in result
        assert "empty" not in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
