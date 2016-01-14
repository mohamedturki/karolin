#!/bin/sh

# Waits for the Postgresql services to be available
# before running Django migration.
while ! nc -z db 5432; do sleep 3; done
python manage.py migrate

# Create a superuser.
# Credits go to: http://source.mihelac.org/2009/10/23/django-avoiding-typing-password-for-superuser/
echo "from django.contrib.auth.models import User; try: User.objects.get(username='karolina') except: User.objects.create_superuser('karolina', 'k.dziorek@gmail.com', 'rootpassword')" | python manage.py shell

python manage.py runserver 0000:8000 --settings=karolin.settings.base
