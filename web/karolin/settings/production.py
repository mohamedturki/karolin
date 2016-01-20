import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += (
    'compressor',
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
