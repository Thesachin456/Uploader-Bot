#!/usr/bin/env python3
"""
Render-optimized start script for the Lecture Scraper application
"""

import os
import sys
from server import app

if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    
    # Get host from environment (Render requires 0.0.0.0)
    host = os.environ.get('HOST', '0.0.0.0')
    
    # Disable debug in production
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"🚀 Starting Lecture Scraper on {host}:{port}")
    print(f"🔧 Debug mode: {debug}")
    
    # Start the Flask application
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )