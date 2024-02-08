#!/bin/bash

echo "Apply database migrations..."
poetry run python manage.py makemigrations
poetry run python manage.py migrate

echo "Starting server..."
poetry run python manage.py runserver 0.0.0.0:8000 
