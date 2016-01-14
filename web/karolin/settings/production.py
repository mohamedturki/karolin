"""
Settings specific to the production environment.
"""

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']


# TODO:
# Add django-compressor
# add loggin with Sentry
#
