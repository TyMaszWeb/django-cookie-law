from __future__ import absolute_import

import os
import sys

from django.conf import settings
from django.core import management


def main():
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS = (
            'django.contrib.staticfiles',
            'cookielaw',
            'cookielaw.test_project.test_app',
        ),
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
        ),
        TEMPLATE_CONTEXT_PROCESSORS = (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
            'django.contrib.messages.context_processors.messages'
        ),
        ROOT_URLCONF = 'cookielaw.test_project.urls',
        STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'cookielaw', 'static'),
        STATIC_URL = '/static/',
    )
    management.execute_from_command_line(['', 'test', 'cookielaw',])
    sys.exit()
