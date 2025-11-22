#!/bin/bash
set -e

echo "🚀 Starting Django application..."

echo "📊 Running database migrations..."
python manage.py migrate --verbosity=2

echo "📁 Collecting static files..."  
python manage.py collectstatic --noinput --verbosity=2

echo "🌟 Starting Gunicorn server on port ${PORT:-8000}..."
echo "DEBUG: PORT variable is: ${PORT}"
echo "DEBUG: Will bind to: 0.0.0.0:${PORT:-8000}"
exec gunicorn --bind 0.0.0.0:${PORT:-8000} --workers=2 --timeout=60 --access-logfile=- --error-logfile=- config.wsgi:application