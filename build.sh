#!/bin/bash

echo "🔨 Building Lecture Scraper Project..."
echo "====================================="

# Check Python version
echo "🐍 Checking Python version..."
python3 --version

# Install system dependencies if needed
echo "📦 Installing system dependencies..."
if command -v apt &> /dev/null; then
    echo "   Installing libxml2-dev libxslt-dev (for potential lxml support)..."
    sudo apt update && sudo apt install -y python3-venv python3-full python3-dev libxml2-dev libxslt1-dev
elif command -v yum &> /dev/null; then
    echo "   Installing development tools for RHEL/CentOS..."
    sudo yum install -y python3-venv python3-devel libxml2-devel libxslt-devel
elif command -v brew &> /dev/null; then
    echo "   Installing dependencies for macOS..."
    brew install python@3.11 libxml2 libxslt
else
    echo "   ⚠️  Unknown package manager. Please ensure python3-venv is installed."
fi

# Create virtual environment
echo "🏗️  Creating virtual environment..."
if [ -d "lecture_env" ]; then
    echo "   Virtual environment already exists. Removing old one..."
    rm -rf lecture_env
fi

python3 -m venv lecture_env

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source lecture_env/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p static templates

# Set permissions
echo "🔐 Setting file permissions..."
chmod +x start.sh

# Verify installation
echo "✅ Verifying installation..."
python -c "import flask, bs4, requests; print('✅ All dependencies installed successfully!')"

echo ""
echo "🎉 Build completed successfully!"
echo "================================="
echo "📋 Next steps:"
echo "   1. Run './start.sh' to start the server"
echo "   2. Visit http://localhost:5000 in your browser"
echo "   3. Go to http://localhost:5000/admin to add lectures"
echo ""