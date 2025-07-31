# 🚀 Deployment Guide - Lecture Scraper

This guide covers deploying the Lecture Scraper application to various platforms.

## 🌐 Render Deployment (Recommended)

Render is the easiest way to deploy this Flask application with automatic builds and free hosting.

### Prerequisites
- GitHub, GitLab, or Bitbucket account
- Render account (free at render.com)

### Step-by-Step Deployment

1. **Prepare Your Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Visit [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub/GitLab repository
   - Select the lecture-scraper repository

3. **Configure the Service**
   - **Name**: `lecture-scraper` (or your preferred name)
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python start_render.py`
   - **Plan**: Free (or paid for better performance)

4. **Environment Variables** (Optional)
   - `FLASK_ENV`: `production` (automatically set)
   - `WEB_CONCURRENCY`: `2` (for Gunicorn)
   - `GUNICORN_TIMEOUT`: `120`

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Your app will be available at `https://your-app-name.onrender.com`

### Render Configuration Files

The following files are included for Render deployment:

- **`render.yaml`** - Service configuration
- **`start_render.py`** - Production start script
- **`start_render_gunicorn.py`** - Gunicorn-based start (better performance)
- **`requirements.txt`** - Python dependencies
- **`runtime.txt`** - Python version specification

### Performance Options

**Basic (Default):**
```yaml
startCommand: "python start_render.py"
```

**High Performance (Recommended):**
```yaml
startCommand: "python start_render_gunicorn.py"
```

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Start command
CMD ["python", "start_render.py"]
```

### Docker Commands
```bash
# Build image
docker build -t lecture-scraper .

# Run container
docker run -p 5000:5000 -e FLASK_ENV=production lecture-scraper
```

## ☁️ Other Cloud Platforms

### Heroku
1. Install Heroku CLI
2. Create Procfile:
   ```
   web: python start_render.py
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Railway
1. Connect GitHub repository
2. Railway auto-detects Python
3. Set start command: `python start_render.py`

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json`:
   ```json
   {
     "builds": [
       {
         "src": "start_render.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "start_render.py"
       }
     ]
   }
   ```
3. Deploy: `vercel --prod`

## 🔧 Environment Variables

### Required for Production
- `FLASK_ENV=production` - Disables debug mode
- `PORT` - Server port (auto-set by most platforms)

### Optional Performance Tuning
- `WEB_CONCURRENCY=2` - Number of worker processes
- `GUNICORN_TIMEOUT=120` - Request timeout in seconds
- `MAX_REQUESTS=1000` - Requests per worker before restart

## 📊 Performance Optimization

### For High Traffic
1. **Use Gunicorn**: `python start_render_gunicorn.py`
2. **Increase Workers**: Set `WEB_CONCURRENCY=4`
3. **Enable Caching**: Add Redis/Memcached
4. **Use CDN**: For static files

### For Better Scraping
1. **Add User-Agent Rotation**
2. **Implement Rate Limiting**
3. **Add Request Retry Logic**
4. **Use Proxy Rotation** (for production)

## 🔒 Security Considerations

### Production Checklist
- [ ] Set `FLASK_ENV=production`
- [ ] Change secret key in `server.py`
- [ ] Add HTTPS (handled by Render/Heroku)
- [ ] Implement rate limiting for scraping
- [ ] Add input validation for URLs
- [ ] Set up monitoring and logging

### Security Headers (Add to Flask app)
```python
@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

## 📝 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check Python version in `runtime.txt`
   - Verify all dependencies in `requirements.txt`
   - Ensure all files are committed to git

2. **Start Failures**
   - Check PORT environment variable
   - Verify start command syntax
   - Check application logs

3. **Scraping Issues**
   - Some sites block cloud IPs
   - Add delays between requests
   - Rotate User-Agent headers

### Monitoring

**Check Application Health:**
```bash
curl https://your-app.onrender.com/
```

**View Logs (Render):**
- Go to your service dashboard
- Click "Logs" tab for real-time logs

## 🚀 Quick Deployment

**One-Click Render Deploy:**
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

**Manual Deploy:**
```bash
# 1. Push to GitHub
git push origin main

# 2. Visit render.com and connect repository
# 3. Use these settings:
#    Build: pip install -r requirements.txt
#    Start: python start_render.py
```

Your Lecture Scraper will be live and ready to use! 🎉