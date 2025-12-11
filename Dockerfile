# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=project_settings.settings \
    PORT=8000

# Set work directory
WORKDIR /app

# Install minimal system dependencies (skip heavy dependencies)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy entire project
COPY . .

# Install Python dependencies with increased timeout
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r "Django Application/requirements.txt" && \
    pip install --no-cache-dir gunicorn whitenoise

# Set working directory to Django app
WORKDIR /app/Django\ Application

# Create necessary directories
RUN mkdir -p uploaded_videos uploaded_images logs static staticfiles

# Collect static files (ignore errors if migrations not needed)
RUN python manage.py collectstatic --noinput 2>/dev/null || true

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--worker-class", "sync", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "project_settings.wsgi:application"]
