#!/bin/sh

# Waits for the Postgresql services to be available
# before running Django migration.
while ! nc -z db 5432; do sleep 3; done
python manage.py migrate

python manage.py collectstatic --noinput

python manage.py loaddata karolin/fixtures/fixtures.json

/usr/local/bin/gunicorn -b :8000 -w 2 karolin.wsgi:application
