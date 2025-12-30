#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Navigate to backend directory
cd backend

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate