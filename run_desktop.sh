#!/bin/bash
# Quick start script for desktop mode

set -e

echo "🚀 Claude Config Editor - Desktop Mode"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate venv
source venv/bin/activate

# Install requirements if needed
if ! python -c "import webview" 2>/dev/null; then
    echo "📥 Installing PyWebView..."
    pip install -q -r requirements.txt
    echo ""
fi

# Run in desktop mode
python3 server.py --desktop "$@"
