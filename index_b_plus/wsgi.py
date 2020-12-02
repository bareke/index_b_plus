"""
WSGI config for index_b_plus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core.utils import load_tree
from core.utils import random_products

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'index_b_plus.settings')

application = get_wsgi_application()

random_products()
load_tree()