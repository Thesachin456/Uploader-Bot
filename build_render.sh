#!/bin/bash

echo "🔨 Building Lecture Scraper for Render..."
echo "========================================"

# Render automatically provides Python, so we just need to install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p static templates

# Set executable permissions
echo "🔐 Setting permissions..."
chmod +x start_render.py

echo "✅ Render build completed successfully!"
echo "🚀 Ready to start with: python start_render.py"