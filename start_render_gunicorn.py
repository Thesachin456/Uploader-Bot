#!/usr/bin/env python3
"""
Gunicorn-based start script for Render deployment (better for production)
"""

import os
import subprocess
import sys

if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = os.environ.get('PORT', '5000')
    
    # Gunicorn configuration
    workers = os.environ.get('WEB_CONCURRENCY', '2')  # Number of worker processes
    timeout = os.environ.get('GUNICORN_TIMEOUT', '120')  # Timeout for requests
    
    print(f"🚀 Starting Lecture Scraper with Gunicorn")
    print(f"🔧 Port: {port}")
    print(f"👥 Workers: {workers}")
    print(f"⏱️  Timeout: {timeout}s")
    
    # Build gunicorn command
    cmd = [
        'gunicorn',
        '--bind', f'0.0.0.0:{port}',
        '--workers', workers,
        '--timeout', timeout,
        '--worker-class', 'sync',
        '--worker-connections', '1000',
        '--max-requests', '1000',
        '--max-requests-jitter', '100',
        '--preload',
        '--access-logfile', '-',
        '--error-logfile', '-',
        'server:app'
    ]
    
    # Start Gunicorn
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n👋 Shutting down gracefully...")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)