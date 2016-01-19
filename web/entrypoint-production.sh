#!/bin/sh

export DB_NAME="postgres"
export DB_USER="postgres"
export DEBUG=False
export SECRET_KEY=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c30)
export DJANGO_SETTINGS_MODULE="karolin.settings.production"


# Waits for the Postgresql services to be available
# before running Django migration.
while ! nc -z db 5432; do sleep 3; done
python manage.py migrate

python manage.py collectstatic --noinput

/usr/local/bin/gunicorn -b :8000 -w 2 karolin.wsgi:application
