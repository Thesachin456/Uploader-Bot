#!/bin/bash

echo "🚀 Starting Lecture Scraper Server..."
echo "=================================="

# Check if virtual environment exists
if [ ! -d "lecture_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv lecture_env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source lecture_env/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Start the server
echo "🌐 Starting Flask server..."
echo "🎯 Visit http://localhost:5000 to view your lecture collection"
echo "⚙️  Visit http://localhost:5000/admin to add new lectures"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=================================="

python server.py