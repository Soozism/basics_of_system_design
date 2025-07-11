#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple HTTP Server for System Design Tutorial Website
This script starts a local web server to view the HTML website
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

def main():
    """Start the web server"""
    # Change to the html_website directory
    website_dir = Path(__file__).parent
    os.chdir(website_dir)
    
    # Server configuration
    port = 8000
    host = 'localhost'
    
    # Create server
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"🚀 Starting System Design Tutorial Website...")
    print(f"📁 Serving from: {website_dir}")
    print(f"🌐 Server running at: http://{host}:{port}")
    print(f"📖 Open your browser and go to: http://{host}:{port}")
    print(f"📋 For complete page list: http://{host}:{port}/sitemap.html")
    print("\n🔧 Press Ctrl+C to stop the server")
    
    # Try to open browser automatically
    try:
        webbrowser.open(f'http://{host}:{port}')
        print("🌐 Browser opened automatically")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
    
    # Start server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n⏹️  Server stopped by user")
        httpd.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()
