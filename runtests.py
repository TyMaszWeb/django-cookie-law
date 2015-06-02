from __future__ import absolute_import

import os.path
import sys

import django
from django.conf import settings
from django.core import management
# from django.utils.unittest import TestLoader

# from cookielaw import tests


def main():
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'django-cookie-law.db',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.staticfiles',
            'cookielaw',
            'cookielaw.test_project.test_app',
        ),
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
        ),
        TEMPLATE_CONTEXT_PROCESSORS=(
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
            'django.contrib.messages.context_processors.messages'
        ),
        ROOT_URLCONF='cookielaw.test_project.urls',
        STATIC_ROOT=os.path.abspath('cookielaw/test_project/static'),
        STATIC_URL='/static/',
    )
    if hasattr(django, 'setup'):
        django.setup()

    management.execute_from_command_line(['', 'test', 'cookielaw',])
    sys.exit()
