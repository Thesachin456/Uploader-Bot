# 📚 Lecture Scraper - Flask Web Application

A beautiful, responsive Flask web application that can scrape lecture content from partner websites and display them in an elegant, pastel-themed interface.

## ✨ Features

- **🔍 Web Scraping**: Automatically extract lecture content from any URL
- **📱 Responsive Design**: Beautiful pastel theme that works on mobile and desktop
- **🎥 Video Support**: Embed YouTube, Vimeo, and other video content
- **📝 Notes Management**: Extract and display text-based lecture notes
- **⚙️ Admin Panel**: Easy-to-use interface for managing lectures
- **✏️ Edit Functionality**: Modify scraped content as needed
- **🗑️ Delete Options**: Remove unwanted lectures
- **💾 File Storage**: Simple JSON-based storage (no database required)

## 🎨 Screenshots

The application features a beautiful pastel gradient theme with:
- Soft color palette (purple, blue, pink, orange)
- Smooth animations and hover effects
- Card-based layout for lectures
- Responsive grid system
- Glass-morphism design elements

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup

Choose your preferred method:

#### Option 1: Quick Start (Recommended)
```bash
# Build and setup everything
./build.sh

# Start the server
./start.sh
```

#### Option 2: Using Make
```bash
# Setup the project
make build

# Start the server
make start
```

#### Option 3: Using npm-style commands
```bash
# Setup the project
npm run build

# Start the server
npm start
```

#### Option 4: Manual Setup
```bash
# Create virtual environment
python3 -m venv lecture_env
source lecture_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python server.py
```

#### Access the Application
```
Homepage: http://localhost:5000
Admin Panel: http://localhost:5000/admin
```

## 📖 How to Use

### Adding Lectures

1. **Go to Admin Panel**
   - Visit `http://localhost:5000/admin`
   - Or click "⚙️ Admin Panel" from the homepage

2. **Enter a Lecture URL**
   - Paste the URL of a webpage containing lecture content
   - Click "🔍 Scrape & Add Lecture"

3. **Wait for Processing**
   - The app will automatically extract:
     - Title
     - Description
     - Video links (YouTube, Vimeo, etc.)
     - Text content and notes

### Managing Lectures

- **View All**: Homepage displays all lectures in a beautiful card layout
- **Edit**: Click "✏️ Edit" to modify title, description, video URL, or notes
- **Delete**: Click "🗑️ Delete" to remove a lecture (with confirmation)
- **View Source**: Click "🔗 Source" to visit the original webpage

### Supported Content Types

The scraper can extract:
- **Titles**: `<h1>`, `.title`, `#title`, `.lecture-title`, etc.
- **Descriptions**: `.description`, `.summary`, meta descriptions
- **Videos**: YouTube embeds, Vimeo links, direct video files
- **Notes**: Paragraphs, bullet points, formatted text content

## 🛠️ Technical Details

### Project Structure
```
lecture-scraper/
├── server.py              # Main Flask application
├── requirements.txt       # Python dependencies
├── lectures.json          # Data storage (auto-created)
├── templates/
│   ├── index.html         # Homepage template
│   ├── admin.html         # Admin panel template
│   └── edit.html          # Edit lecture template
└── static/
    └── styles.css         # Pastel theme CSS
```

### Dependencies

- **Flask**: Web framework
- **BeautifulSoup4**: HTML parsing and scraping
- **Requests**: HTTP requests for web scraping
- **lxml**: XML/HTML parser
- **Werkzeug**: WSGI utilities

### Data Storage

Lectures are stored in `lectures.json` with this structure:
```json
[
  {
    "id": 1,
    "title": "Lecture Title",
    "description": "Lecture description",
    "video_url": "https://youtube.com/watch?v=...",
    "notes": ["Note 1", "Note 2", "..."],
    "source_url": "https://original-url.com"
  }
]
```

## 🎨 Customization

### Changing the Theme

Edit `static/styles.css` to customize:
- Colors: Modify the gradient backgrounds and color variables
- Fonts: Change the font-family declarations
- Layout: Adjust grid settings and spacing
- Animations: Modify transition and animation properties

### Modifying Scraping Logic

Edit `server.py` functions:
- `scrape_lecture_content()`: Main scraping logic
- `extract_youtube_id()`: Video URL processing
- Add new selectors for different website structures

### Adding New Features

The codebase is beginner-friendly and modular:
- Routes are clearly defined in `server.py`
- Templates use Jinja2 for dynamic content
- CSS is organized with clear sections
- JavaScript adds progressive enhancement

## 🛠️ Available Commands

The project provides multiple ways to build and run the application:

### Build Commands
```bash
./build.sh           # Complete project setup
make build           # Using Make
npm run build        # Using npm scripts
```

### Start Commands
```bash
./start.sh           # Start the Flask server
make start           # Using Make
npm start            # Using npm scripts
npm run dev          # Development mode (same as start)
```

### Utility Commands
```bash
make help            # Show available Make commands
make clean           # Clean up build artifacts
make test            # Run basic functionality tests
make install         # Install dependencies only
```

### What the Build Script Does
- ✅ Checks Python version compatibility
- ✅ Installs system dependencies (if needed)
- ✅ Creates Python virtual environment
- ✅ Installs Python packages from requirements.txt
- ✅ Creates necessary directories
- ✅ Sets proper file permissions
- ✅ Verifies installation

### What the Start Script Does
- ✅ Activates virtual environment
- ✅ Installs/updates dependencies
- ✅ Starts Flask development server
- ✅ Shows access URLs and instructions

## 🔧 Troubleshooting

### Common Issues

1. **"Failed to scrape" error**
   - Check if the URL is accessible
   - Some sites block automated requests
   - Verify the site contains scrapeable content

2. **Video not displaying**
   - Ensure the video URL is correctly formatted
   - Check if the video is publicly accessible
   - Try editing the lecture to fix the video URL

3. **Styling issues**
   - Clear browser cache
   - Check if `styles.css` is loading correctly
   - Verify the Flask static file serving

### Development Mode

The app runs in debug mode by default, which:
- Auto-reloads on code changes
- Shows detailed error messages
- Should not be used in production

### Production Deployment

For production use:
1. Set `debug=False` in `server.py`
2. Use a production WSGI server (gunicorn, uWSGI)
3. Set up proper error logging
4. Consider using a real database for larger datasets

## 🤝 Contributing

This is a beginner-friendly project! Areas for improvement:
- Add more video platform support
- Implement search functionality
- Add user authentication
- Create lecture categories/tags
- Add export functionality
- Improve mobile responsiveness

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure you're using a supported Python version
4. Check that the target websites are accessible

---

**Happy Learning!** 📚✨
