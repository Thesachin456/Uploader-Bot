from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
from bs4 import BeautifulSoup
import json
import os
import re
from urllib.parse import urljoin, urlparse

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Data storage file
DATA_FILE = 'lectures.json'

def load_lectures():
    """Load lectures from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_lectures(lectures):
    """Save lectures to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(lectures, f, indent=2, ensure_ascii=False)

def extract_youtube_id(url):
    """Extract YouTube video ID from various URL formats"""
    if not url:
        return None
    
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/v\/([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def scrape_lecture_content(url):
    """Scrape lecture content from a given URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title (try multiple selectors)
        title = None
        title_selectors = ['h1', '.title', '#title', '.lecture-title', '.post-title', 'title']
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element and element.get_text(strip=True):
                title = element.get_text(strip=True)
                break
        
        # Extract description (try multiple selectors)
        description = ""
        desc_selectors = ['.description', '.summary', '.excerpt', '.intro', 'meta[name="description"]']
        for selector in desc_selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == 'meta':
                    description = element.get('content', '')
                else:
                    description = element.get_text(strip=True)
                if description:
                    break
        
        # Extract video links (YouTube, Vimeo, direct video)
        video_url = None
        
        # Look for YouTube embeds
        youtube_iframe = soup.find('iframe', src=re.compile(r'youtube\.com/embed/'))
        if youtube_iframe:
            video_url = youtube_iframe.get('src')
        
        # Look for YouTube links
        if not video_url:
            youtube_links = soup.find_all('a', href=re.compile(r'(youtube\.com|youtu\.be)'))
            if youtube_links:
                video_url = youtube_links[0].get('href')
        
        # Look for video tags
        if not video_url:
            video_tag = soup.find('video')
            if video_tag:
                source = video_tag.find('source')
                if source:
                    video_url = source.get('src')
                else:
                    video_url = video_tag.get('src')
        
        # Extract text content (paragraphs, lists)
        notes = []
        
        # Look for main content areas
        content_selectors = ['.content', '.post-content', '.lecture-content', '.main-content', '.article-body']
        content_area = None
        
        for selector in content_selectors:
            content_area = soup.select_one(selector)
            if content_area:
                break
        
        # If no specific content area found, use body
        if not content_area:
            content_area = soup.find('body')
        
        if content_area:
            # Extract paragraphs
            paragraphs = content_area.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20:  # Filter out very short paragraphs
                    notes.append(text)
            
            # Extract lists
            lists = content_area.find_all(['ul', 'ol'])
            for ul in lists:
                list_items = ul.find_all('li')
                if list_items:
                    for li in list_items:
                        text = li.get_text(strip=True)
                        if text:
                            notes.append(f"• {text}")
        
        # Clean up notes (remove duplicates and very short items)
        notes = list(dict.fromkeys(notes))  # Remove duplicates
        notes = [note for note in notes if len(note) > 10]  # Remove very short notes
        
        return {
            'title': title or 'Untitled Lecture',
            'description': description or 'No description available',
            'video_url': video_url,
            'notes': notes[:10],  # Limit to first 10 notes
            'source_url': url
        }
        
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

@app.route('/')
def index():
    """Homepage displaying all lectures"""
    lectures = load_lectures()
    return render_template('index.html', lectures=lectures)

@app.route('/admin')
def admin():
    """Admin panel for managing lectures"""
    lectures = load_lectures()
    return render_template('admin.html', lectures=lectures)

@app.route('/scrape', methods=['POST'])
def scrape_lecture():
    """Scrape a lecture from the provided URL"""
    url = request.form.get('url', '').strip()
    
    if not url:
        flash('Please provide a valid URL', 'error')
        return redirect(url_for('admin'))
    
    # Add http:// if no protocol specified
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    lecture_data = scrape_lecture_content(url)
    
    if lecture_data:
        lectures = load_lectures()
        
        # Add unique ID
        lecture_data['id'] = len(lectures) + 1
        
        lectures.append(lecture_data)
        save_lectures(lectures)
        
        flash(f'Successfully added lecture: {lecture_data["title"]}', 'success')
    else:
        flash('Failed to scrape lecture content. Please check the URL and try again.', 'error')
    
    return redirect(url_for('admin'))

@app.route('/delete/<int:lecture_id>')
def delete_lecture(lecture_id):
    """Delete a lecture"""
    lectures = load_lectures()
    lectures = [l for l in lectures if l.get('id') != lecture_id]
    save_lectures(lectures)
    flash('Lecture deleted successfully', 'success')
    return redirect(url_for('admin'))

@app.route('/edit/<int:lecture_id>', methods=['GET', 'POST'])
def edit_lecture(lecture_id):
    """Edit a lecture"""
    lectures = load_lectures()
    lecture = next((l for l in lectures if l.get('id') == lecture_id), None)
    
    if not lecture:
        flash('Lecture not found', 'error')
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        # Update lecture data
        lecture['title'] = request.form.get('title', lecture['title'])
        lecture['description'] = request.form.get('description', lecture['description'])
        lecture['video_url'] = request.form.get('video_url', lecture['video_url'])
        
        # Update notes (convert from textarea to list)
        notes_text = request.form.get('notes', '')
        lecture['notes'] = [note.strip() for note in notes_text.split('\n') if note.strip()]
        
        save_lectures(lectures)
        flash('Lecture updated successfully', 'success')
        return redirect(url_for('admin'))
    
    # Convert notes list to text for editing
    lecture['notes_text'] = '\n'.join(lecture.get('notes', []))
    
    return render_template('edit.html', lecture=lecture)

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)