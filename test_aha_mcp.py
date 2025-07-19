#!/usr/bin/env python3
"""
Test suite for Aha! MCP Server
Tests all GraphQL endpoints using FastMCP's in-memory testing pattern
"""
import pytest
import pytest_asyncio
import asyncio
from unittest.mock import patch, AsyncMock, MagicMock
from fastmcp import Client
import os
import json

# Import the server instance - need to handle hyphen in filename
import sys
import importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import module with hyphen in name
spec = importlib.util.spec_from_file_location("aha_mcp", "aha-mcp.py")
aha_mcp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aha_mcp)

# Get the instances we need
mcp = aha_mcp.mcp
graphql = aha_mcp.graphql


# Test data - using DEMO project references
TEST_FEATURE_ID = "DEMO-35"
TEST_IDEA_ID = "DEMO-I-1"
TEST_PAGE_ID = "DEMO-N-1"
TEST_RELEASE_ID = "DEMO-R-2"
TEST_PROJECT_ID = "DEMO"

# Mock GraphQL responses
MOCK_FEATURE_RESPONSE = {
    "feature": {
        "id": "7528852850265353159",
        "referenceNum": "DEMO-35",
        "name": "Send data to my doctors",
        "description": {
            "htmlBody": "<p>Test description</p>"
        }
    }
}

MOCK_IDEA_RESPONSE = {
    "idea": {
        "id": "7528817420261227006",
        "referenceNum": "DEMO-I-1",
        "name": "Example Idea 1",
        "description": {
            "htmlBody": "Test idea description"
        },
        "visibility": "VISIBILITY_PUBLIC",
        "score": 0.0,
        "assignedToUser": {
            "id": None,
            "name": "Default (Unassigned)"
        },
        "promotable": None,
        "workflowStatus": {
            "id": "6001166979456424024",
            "name": "Future consideration"
        }
    }
}

MOCK_PAGE_RESPONSE = {
    "page": {
        "id": "123456",
        "referenceNum": "DEMO-N-1",
        "name": "Test Page",
        "description": {
            "htmlBody": "<p>Test page content</p>"
        },
        "parent": None
    }
}

MOCK_LIST_FEATURES_RESPONSE = {
    "features": {
        "nodes": [
            {
                "id": "7528852850265353159",
                "referenceNum": "DEMO-35",
                "name": "Send data to my doctors",
                "description": {"htmlBody": "<p>Test</p>"},
                "workflowStatus": {"id": "123", "name": "In Progress"},
                "release": {"id": "456", "referenceNum": "DEMO-R-2", "name": "Release 2"},
                "assignedToUser": {"id": None, "name": "Default (Unassigned)"}
            }
        ],
        "currentPage": 1,
        "totalCount": 1,
        "totalPages": 1
    }
}

MOCK_CREATE_FEATURE_RESPONSE = {
    "createFeature": {
        "feature": {
            "id": "new-feature-id",
            "referenceNum": "DEMO-100",
            "name": "New Test Feature"
        },
        "errors": None
    }
}

MOCK_UPDATE_FEATURE_RESPONSE = {
    "updateFeature": {
        "feature": {
            "id": "7528852850265353159",
            "referenceNum": "DEMO-35",
            "name": "Updated Feature Name"
        },
        "errors": None
    }
}

MOCK_DELETE_FEATURE_RESPONSE = {
    "deleteFeature": {
        "errors": None
    }
}

MOCK_SEARCH_RESPONSE = {
    "searchDocuments": {
        "nodes": [
            {
                "name": "Test Document",
                "url": "https://demo.aha.io/test",
                "searchableId": "123",
                "searchableType": "Page"
            }
        ],
        "currentPage": 1,
        "totalCount": 1,
        "totalPages": 1
    }
}

MOCK_LIST_IDEAS_RESPONSE = {
    "ideas": {
        "nodes": [
            {
                "id": "7528817420261227006",
                "referenceNum": "DEMO-I-1",
                "name": "Example Idea 1",
                "description": {"htmlBody": "Test"},
                "visibility": "VISIBILITY_PUBLIC",
                "score": 0.0,
                "assignedToUser": {"id": None, "name": "Default (Unassigned)"}
            }
        ],
        "currentPage": 1,
        "totalCount": 1,
        "totalPages": 1
    }
}

MOCK_CREATE_IDEA_RESPONSE = {
    "createIdea": {
        "idea": {
            "id": "new-idea-id",
            "referenceNum": "DEMO-I-100",
            "name": "New Test Idea"
        },
        "errors": None
    }
}

MOCK_UPDATE_IDEA_RESPONSE = {
    "updateIdea": {
        "idea": {
            "id": "7528817420261227006",
            "referenceNum": "DEMO-I-1",
            "name": "Updated Idea Name"
        },
        "errors": None
    }
}

MOCK_INTROSPECTION_RESPONSE = {
    "__schema": {
        "types": [
            {"name": "Feature", "kind": "OBJECT", "description": "A feature"},
            {"name": "Idea", "kind": "OBJECT", "description": "An idea"}
        ],
        "queryType": {
            "fields": [
                {"name": "feature", "description": "Find a feature"},
                {"name": "idea", "description": "Find an idea"}
            ]
        },
        "mutationType": {
            "fields": [
                {"name": "createFeature", "description": "Create a feature"},
                {"name": "updateFeature", "description": "Update a feature"}
            ]
        }
    }
}

@pytest.fixture
def mock_env(monkeypatch):
    """Set up test environment variables"""
    monkeypatch.setenv("AHA_API_TOKEN", "test-token")
    monkeypatch.setenv("AHA_DOMAIN", "test-domain")

@pytest_asyncio.fixture
async def test_client(mock_env):
    """Create a test client with mocked GraphQL"""
    # Note: We need to patch the graphql function on the imported module
    with patch.object(aha_mcp, 'graphql', new_callable=AsyncMock) as mock_graphql:
        async with Client(mcp) as client:
            # Set the mock on the client for tests to configure
            client.mock_graphql = mock_graphql
            yield client

# Test get_record functionality
@pytest.mark.asyncio
async def test_get_record_feature(test_client):
    """Test getting a feature by reference"""
    test_client.mock_graphql.return_value = MOCK_FEATURE_RESPONSE
    
    result = await test_client.call_tool("get_record", {"reference": TEST_FEATURE_ID})
    
    assert json.loads(result.data) == MOCK_FEATURE_RESPONSE["feature"]
    test_client.mock_graphql.assert_called_once()

@pytest.mark.asyncio
async def test_get_record_idea(test_client):
    """Test getting an idea by reference"""
    test_client.mock_graphql.return_value = MOCK_IDEA_RESPONSE
    
    result = await test_client.call_tool("get_record", {"reference": TEST_IDEA_ID})
    
    assert json.loads(result.data) == MOCK_IDEA_RESPONSE["idea"]

@pytest.mark.asyncio
async def test_get_record_invalid_reference(test_client):
    """Test getting record with invalid reference format"""
    result = await test_client.call_tool("get_record", {"reference": "INVALID"})
    
    data = json.loads(result.data)
    assert "error" in data
    assert "Invalid reference format" in data["error"]

# Test search functionality
@pytest.mark.asyncio
async def test_search_documents(test_client):
    """Test searching documents"""
    test_client.mock_graphql.return_value = MOCK_SEARCH_RESPONSE
    
    result = await test_client.call_tool("search_documents", {
        "query": "test",
        "searchable_type": "Page"
    })
    
    assert json.loads(result.data) == MOCK_SEARCH_RESPONSE["searchDocuments"]

# Test list features
@pytest.mark.asyncio
async def test_list_features(test_client):
    """Test listing features with project filter"""
    test_client.mock_graphql.return_value = MOCK_LIST_FEATURES_RESPONSE
    
    result = await test_client.call_tool("list_features", {
        "project_id": TEST_PROJECT_ID
    })
    
    assert json.loads(result.data) == MOCK_LIST_FEATURES_RESPONSE["features"]

@pytest.mark.asyncio
async def test_list_features_no_filters(test_client):
    """Test list features without required filters"""
    result = await test_client.call_tool("list_features", {})
    
    data = json.loads(result.data)
    assert "error" in data
    assert "At least one filter required" in data["error"]

# Test create feature
@pytest.mark.asyncio
async def test_create_feature(test_client):
    """Test creating a new feature"""
    test_client.mock_graphql.return_value = MOCK_CREATE_FEATURE_RESPONSE
    
    result = await test_client.call_tool("create_feature", {
        "release_id": TEST_RELEASE_ID,
        "name": "New Test Feature",
        "description": "Test description"
    })
    
    assert json.loads(result.data) == MOCK_CREATE_FEATURE_RESPONSE["createFeature"]["feature"]

@pytest.mark.asyncio
async def test_create_feature_with_error(test_client):
    """Test creating feature with GraphQL errors"""
    test_client.mock_graphql.return_value = {
        "createFeature": {
            "feature": None,
            "errors": {
                "attributes": [
                    {"name": "name", "fullMessages": ["Name is required"]}
                ]
            }
        }
    }
    
    result = await test_client.call_tool("create_feature", {
        "release_id": TEST_RELEASE_ID,
        "name": ""
    })
    
    data = json.loads(result.data)
    assert "error" in data
    assert "Failed to create" in data["error"]

# Test update feature
@pytest.mark.asyncio
async def test_update_feature(test_client):
    """Test updating an existing feature"""
    test_client.mock_graphql.return_value = MOCK_UPDATE_FEATURE_RESPONSE
    
    result = await test_client.call_tool("update_feature", {
        "id": TEST_FEATURE_ID,
        "name": "Updated Feature Name"
    })
    
    assert json.loads(result.data) == MOCK_UPDATE_FEATURE_RESPONSE["updateFeature"]["feature"]

# Test delete feature
@pytest.mark.asyncio
async def test_delete_feature(test_client):
    """Test deleting a feature"""
    test_client.mock_graphql.return_value = MOCK_DELETE_FEATURE_RESPONSE
    
    result = await test_client.call_tool("delete_feature", {
        "id": TEST_FEATURE_ID
    })
    
    data = json.loads(result.data)
    assert data["success"] == True
    assert data["id"] == TEST_FEATURE_ID

# Test get feature details
@pytest.mark.asyncio
async def test_get_feature_details(test_client):
    """Test getting detailed feature information"""
    detailed_response = {
        "feature": {
            **MOCK_FEATURE_RESPONSE["feature"],
            "tags": [],
            "createdAt": "2025-01-01T00:00:00Z",
            "updatedAt": "2025-01-01T00:00:00Z",
            "epic": None,
            "team": None
        }
    }
    test_client.mock_graphql.return_value = detailed_response
    
    result = await test_client.call_tool("get_feature_details", {
        "id": TEST_FEATURE_ID
    })
    
    assert json.loads(result.data) == detailed_response["feature"]

# Test page operations
@pytest.mark.asyncio
async def test_get_page(test_client):
    """Test getting a page by reference"""
    test_client.mock_graphql.return_value = MOCK_PAGE_RESPONSE
    
    result = await test_client.call_tool("get_page", {
        "reference": TEST_PAGE_ID,
        "include_parent": False
    })
    
    assert json.loads(result.data) == MOCK_PAGE_RESPONSE["page"]

@pytest.mark.asyncio
async def test_get_page_invalid_format(test_client):
    """Test getting page with invalid reference format"""
    result = await test_client.call_tool("get_page", {
        "reference": "DEMO-123"  # Should be DEMO-N-123
    })
    
    data = json.loads(result.data)
    assert "error" in data
    assert "Invalid page reference format" in data["error"]

# Test idea operations
@pytest.mark.asyncio
async def test_get_idea(test_client):
    """Test getting an idea by ID"""
    test_client.mock_graphql.return_value = MOCK_IDEA_RESPONSE
    
    result = await test_client.call_tool("get_idea", {
        "id": TEST_IDEA_ID
    })
    
    assert json.loads(result.data) == MOCK_IDEA_RESPONSE["idea"]

@pytest.mark.asyncio
async def test_list_ideas(test_client):
    """Test listing ideas for a project"""
    test_client.mock_graphql.return_value = MOCK_LIST_IDEAS_RESPONSE
    
    result = await test_client.call_tool("list_ideas", {
        "project_id": TEST_PROJECT_ID
    })
    
    assert json.loads(result.data) == MOCK_LIST_IDEAS_RESPONSE["ideas"]

@pytest.mark.asyncio
async def test_create_idea(test_client):
    """Test creating a new idea"""
    test_client.mock_graphql.return_value = MOCK_CREATE_IDEA_RESPONSE
    
    result = await test_client.call_tool("create_idea", {
        "project_id": TEST_PROJECT_ID,
        "name": "New Test Idea"
    })
    
    assert json.loads(result.data) == MOCK_CREATE_IDEA_RESPONSE["createIdea"]["idea"]

@pytest.mark.asyncio
async def test_update_idea(test_client):
    """Test updating an idea"""
    test_client.mock_graphql.return_value = MOCK_UPDATE_IDEA_RESPONSE
    
    result = await test_client.call_tool("update_idea", {
        "id": TEST_IDEA_ID,
        "name": "Updated Idea Name"
    })
    
    assert json.loads(result.data) == MOCK_UPDATE_IDEA_RESPONSE["updateIdea"]["idea"]

@pytest.mark.asyncio
async def test_delete_idea(test_client):
    """Test deleting an idea via REST API"""
    # This one uses httpx directly, so we need to mock differently
    with patch('httpx.AsyncClient.delete', new_callable=AsyncMock) as mock_delete:
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response
        
        result = await test_client.call_tool("delete_idea", {
            "id": TEST_IDEA_ID
        })
        
        data = json.loads(result.data)
        assert data["success"] == True
        assert data["id"] == TEST_IDEA_ID

# Test introspection
@pytest.mark.asyncio
async def test_introspection_list_types(test_client):
    """Test GraphQL introspection listing types"""
    test_client.mock_graphql.return_value = MOCK_INTROSPECTION_RESPONSE
    
    result = await test_client.call_tool("introspection", {
        "query_type": "list-types"
    })
    
    assert json.loads(result.data) == MOCK_INTROSPECTION_RESPONSE["__schema"]

@pytest.mark.asyncio
async def test_introspection_search(test_client):
    """Test GraphQL introspection with search"""
    test_client.mock_graphql.return_value = MOCK_INTROSPECTION_RESPONSE
    
    result = await test_client.call_tool("introspection", {
        "query_type": "list-types",
        "search_term": "feature"
    })
    
    data = json.loads(result.data)
    # Should filter results to only include items with "feature" in the name
    assert any("feature" in str(item).lower() for item in data.get("types", []))

# Test error handling
@pytest.mark.asyncio
async def test_graphql_error_handling(test_client):
    """Test handling of GraphQL errors"""
    test_client.mock_graphql.side_effect = RuntimeError("GraphQL errors: [{'message': 'Test error'}]")
    
    with pytest.raises(Exception):  # The error will propagate through the tool call
        await test_client.call_tool("get_record", {"reference": TEST_FEATURE_ID})

# Test pagination
@pytest.mark.asyncio
async def test_list_features_pagination(test_client):
    """Test pagination parameters for list endpoints"""
    test_client.mock_graphql.return_value = MOCK_LIST_FEATURES_RESPONSE
    
    result = await test_client.call_tool("list_features", {
        "project_id": TEST_PROJECT_ID,
        "page": 2,
        "per_page": 50
    })
    
    # Verify the GraphQL was called with correct pagination params
    call_args = test_client.mock_graphql.call_args
    # The call_args is (positional_args, keyword_args)
    # GraphQL is called as: graphql(ctx, query, variables)
    assert call_args[0][2]["page"] == 2  # Third positional argument is variables
    assert call_args[0][2]["per"] == 50

if __name__ == "__main__":
    pytest.main([__file__, "-v"])