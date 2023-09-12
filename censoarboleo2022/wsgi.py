"""
WSGI config for censoarboleo2022 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.handlers.modwsgi import check_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'censoarboleo2022.settings')

application = get_wsgi_application()
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


