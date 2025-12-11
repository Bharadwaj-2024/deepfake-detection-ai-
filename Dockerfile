# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=project_settings.settings \
    PORT=8000

# Set work directory
WORKDIR /app

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Copy entire project
COPY . .

# Install Python dependencies with increased timeout
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r "Django Application/requirements.txt" && \
    pip install --no-cache-dir gunicorn whitenoise

# Set working directory to Django app (path contains a space)
WORKDIR "/app/Django Application"

# Create necessary directories
RUN mkdir -p uploaded_videos uploaded_images logs static staticfiles

# Collect static files (ignore errors if migrations not needed)
RUN python manage.py collectstatic --noinput 2>/dev/null || true

# Expose port
EXPOSE 8000

# Run gunicorn binding to platform-provided $PORT
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 2 --worker-class sync --timeout 120 --access-logfile - --error-logfile - project_settings.wsgi:application"]
