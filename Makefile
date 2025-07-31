.PHONY: build start dev clean install help test

# Default target
help:
	@echo "🔨 Lecture Scraper - Available Commands"
	@echo "======================================="
	@echo "  make build    - Set up the project environment"
	@echo "  make start    - Start the Flask server"
	@echo "  make dev      - Start in development mode (alias for start)"
	@echo "  make install  - Install dependencies only"
	@echo "  make clean    - Clean up build artifacts"
	@echo "  make test     - Run basic functionality tests"
	@echo "  make help     - Show this help message"
	@echo ""

# Build the project
build:
	@echo "🔨 Building Lecture Scraper..."
	./build.sh

# Start the server
start:
	@echo "🚀 Starting server..."
	./start.sh

# Development mode (same as start)
dev: start

# Install dependencies only
install:
	@echo "📦 Installing dependencies..."
	@if [ ! -d "lecture_env" ]; then python3 -m venv lecture_env; fi
	@source lecture_env/bin/activate && pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	rm -rf lecture_env/
	rm -f lectures.json
	rm -rf __pycache__/
	rm -rf *.pyc
	@echo "✅ Cleanup complete!"

# Basic functionality test
test:
	@echo "🧪 Running basic tests..."
	@source lecture_env/bin/activate && python3 -c "import server; print('✅ Server imports successfully')"
	@echo "✅ Basic tests passed!"

# Quick setup (build + start)
run: build start