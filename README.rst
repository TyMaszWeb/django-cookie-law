==================
django-cookie-law
==================

.. image:: https://travis-ci.org/TyMaszWeb/django-cookie-law.svg?branch=master
   :target: https://travis-ci.org/TyMaszWeb/django-cookie-law

django-cookie-law helps your Django project comply with the
`EU cookie regulations <http://www.aboutcookies.org/default.aspx?page=3>`_.
by displaying a cookie information banner until it is dismissed by the user.

.. warning:: The app can be incompatible with your local cookie
             law regulations. Consult your lawyer when in doubt.

Contributions and comments are welcome using Github at:
http://github.com/TyMaszWeb/django-cookie-law

Please note that django-cookie-law requires:

- Django >= 1.8
- django-classy-tags >= 0.3.0

Installation
============

#. ``pip install django-cookie-law``
#. Add ``'cookielaw'`` to ``INSTALLED_APPS``
#. Run ``collectstatic`` (Django 1.3+) or copy the statics to your media directory
#. Add ``cookielaw/js/cookielaw.js`` to the markup directly or via your asset
   manager such as ``django-pipeline`` or ``django-compressor``
#. Enable ``'django.core.context_processors.request'`` in your
   ``TEMPLATE_CONTEXT_PROCESSORS`` setting, eg.:

    ::

        TEMPLATE_CONTEXT_PROCESSORS = (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
            'django.contrib.messages.context_processors.messages'
        )

   .. note:: If you don't have this setting defined, just add it to your
             settings module.

#. ``{% load cookielaw_tags %}`` and add ``{% cookielaw_banner %}`` template
   tag where you want to display the cookielaw banner. Best place for this is
   your 'base' template, so you will have the cookie banner on every page of
   your website.

Configuration
=============

If you want to use our default template, add ``cookielaw/css/cookielaw.css`` to
the markup and you should see the cookie law banner at the top of the page until
you dismiss it with the button in the top-right. This CSS is Twitter Bootstrap
compatible, but chances are, you'll like to adjust it anyway.

To change the markup, just add a template named ``cookielaw/banner.html`` and
make sure it is loaded before the default template (for example put the
``django.template.loaders.filesystem.Loader`` before
``django.template.loaders.app_directories.Loader`` and add your new template
to any of the ``TEMPLATE_DIRS``).

To change the CSS, just write your own rules and don't include the default
stylesheet.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/TyMaszWeb/django-cookie-law

:author: Piotr Kilczuk
:date: 2013/04/08

