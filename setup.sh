#!/bin/bash
# Setup script for analytics service
# Creates virtual environment and installs dependencies
# Usage: bash setup.sh

set -e

echo "🔧 Setting up backend analytics service..."
echo "Python version check:"
python3 --version

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip, setuptools, wheel
echo "📥 Upgrading pip and build tools..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "📚 Installing project dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo "To activate the environment, run: source venv/bin/activate"
echo "To run tests, run: bash run_tests.sh"
