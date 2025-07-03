#!/bin/sh

echo "Waiting for the database to be ready..."
sleep 5


echo "Running migrations..."
python manage.py migrate

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000