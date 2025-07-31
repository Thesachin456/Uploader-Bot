#!/usr/bin/env python3
"""
Demo script to test the lecture scraper functionality
"""

import requests
import json
from server import scrape_lecture_content, extract_youtube_id

def test_scraping():
    """Test the scraping functionality with various URLs"""
    
    # Test URLs (you can replace these with actual URLs)
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # YouTube video
        "https://example.com",  # Basic webpage
    ]
    
    print("🔍 Testing Lecture Scraper Functionality")
    print("=" * 50)
    
    for i, url in enumerate(test_urls, 1):
        print(f"\n{i}. Testing URL: {url}")
        print("-" * 30)
        
        try:
            result = scrape_lecture_content(url)
            if result:
                print(f"✅ Successfully scraped!")
                print(f"   Title: {result['title']}")
                print(f"   Description: {result['description'][:100]}..." if len(result['description']) > 100 else f"   Description: {result['description']}")
                print(f"   Video URL: {result['video_url']}")
                print(f"   Notes count: {len(result['notes'])}")
            else:
                print("❌ Failed to scrape content")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🎯 Testing YouTube ID extraction")
    print("=" * 50)
    
    # Test YouTube ID extraction
    youtube_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
    ]
    
    for url in youtube_urls:
        video_id = extract_youtube_id(url)
        print(f"URL: {url}")
        print(f"Extracted ID: {video_id}")
        print()

def check_server_status():
    """Check if the Flask server is running"""
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code == 200:
            print("✅ Flask server is running at http://localhost:5000")
            return True
        else:
            print(f"❌ Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ Flask server is not running")
        return False

if __name__ == "__main__":
    print("📚 Lecture Scraper Demo")
    print("=" * 50)
    
    # Check server status
    server_running = check_server_status()
    
    if server_running:
        print("\n🌐 You can access the application at:")
        print("   Homepage: http://localhost:5000")
        print("   Admin Panel: http://localhost:5000/admin")
    
    print("\n" + "=" * 50)
    
    # Test scraping functionality
    test_scraping()
    
    print("\n🎉 Demo completed!")
    print("📝 To add real lectures, visit the admin panel and enter URLs of lecture pages.")