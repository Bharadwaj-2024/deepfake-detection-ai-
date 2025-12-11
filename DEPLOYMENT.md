# Deepfake Detection AI - Deployment Guide

## Quick Deploy Options

### Option 1: Deploy to Render (Recommended - Free Tier Available)

1. Fork/Push this repository to your GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Render will auto-detect the `render.yaml` configuration
6. Click "Create Web Service"
7. Wait 5-10 minutes for deployment to complete

### Option 2: Deploy to Railway (Free Trial Available)

1. Go to [Railway](https://railway.app/)
2. Click "Start a New Project"
3. Choose "Deploy from GitHub repo"
4. Select this repository
5. Railway will auto-detect the `railway.json` configuration
6. Click "Deploy"
7. Your app will be live in a few minutes

### Option 3: Docker Deployment (Any Platform)

```bash
# Build the Docker image
docker build -t deepfake-detection .

# Run the container
docker run -p 8000:8000 deepfake-detection
```

## Environment Variables (Optional)

Set these in your deployment platform:

- `SECRET_KEY` - Django secret key (auto-generated if not set)
- `DEBUG` - Set to `False` for production (default: `True`)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts (default: `*`)

## Features

✅ AI-powered deepfake detection
✅ Live statistics dashboard
✅ Report generation and export
✅ User feedback system
✅ Modern responsive UI
✅ Video frame analysis
✅ Confidence scoring

## Tech Stack

- Django 5.0.6
- Python 3.13
- OpenCV for video analysis
- NumPy for statistical calculations
- Bootstrap 4 for responsive UI

## Local Development

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
cd "Django Application"
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

Visit http://localhost:8000 to access the application.

## Notes

- The free tiers of Render/Railway may have cold starts (first request takes longer)
- Video uploads are limited to 100MB by default
- Database uses SQLite (suitable for demo/small-scale deployments)
- For production at scale, consider using PostgreSQL and object storage for videos
