#!/bin/sh

# Waits for the Postgresql services to be available
# before running Django migration.
while ! nc -z db 5432; do sleep 3; done
python manage.py migrate

python manage.py collectstatic --noinput

# Create a superuser.
# Credits go to: http://source.mihelac.org/2009/10/23/django-avoiding-typing-password-for-superuser/
echo "from django.contrib.auth.models import User; User.objects.create_superuser('karolina', 'k.dziorek@gmail.com', 'rootpassword')" | python manage.py shell

/usr/local/bin/gunicorn karolin.wsgi:application -w 2 -b :8000