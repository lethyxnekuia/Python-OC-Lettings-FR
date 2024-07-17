#!/bin/sh

# Start Nginx
nginx

# Start Gunicorn
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000 --workers 3