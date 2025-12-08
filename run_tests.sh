#!/bin/bash
# Test runner script for analytics service
# Runs all pytest tests with detailed output
# Usage: bash run_tests.sh

set -e

echo "🧪 Running pytest test suite..."
echo "================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Run setup.sh first: bash setup.sh"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run pytest with detailed output
echo "📊 Executing tests..."
pytest tests/ -v --tb=short --color=yes

echo ""
echo "================================"
echo "✅ Test suite completed!"
