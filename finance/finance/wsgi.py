"""
WSGI config for finance project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance.settings")

# application = get_wsgi_application()

# # modified for heroku
# # from whitenoise.django import DjangoWhiteNoise
# # application = DjangoWhiteNoise(application)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
