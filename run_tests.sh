#!/bin/bash
# Script to run Aha! MCP Server tests

echo "Running Aha! MCP Server Tests..."
echo "================================"

# Set test environment variables
export AHA_API_TOKEN="test-token"
export AHA_DOMAIN="test-domain"

# Install test dependencies if needed
pip install -q pytest pytest-asyncio pytest-mock

# Run tests with verbose output
pytest test_aha_mcp.py -v

# Optional: Run with coverage
if [ "$1" == "--coverage" ]; then
    echo ""
    echo "Running tests with coverage..."
    echo "=============================="
    pip install -q pytest-cov
    pytest test_aha_mcp.py --cov=aha_mcp --cov-report=term-missing
fi