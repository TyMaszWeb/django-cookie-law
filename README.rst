==================
django-cookie-law
==================

.. image:: https://github.com/TyMaszWeb/django-cookie-law/workflows/build/badge.svg
   :target: https://github.com/TyMaszWeb/django-cookie-law/actions

`django-cookie-law` will display a dismissable banner, making your users aware of cookies being used.

.. warning:: This app is known to be **not** complaint with the United Kingdom PECR/GDPR.
             It is your responsibility to find out whether `django-cookie-law` meets the specific local legal requirements.

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
#. If you're using Django > 1.8, enable ``'django.core.context_processors.request'`` in your ``TEMPLATES['OPTIONS']`` setting, eg.:

    ::

         TEMPLATES = [
             {
                 'BACKEND': 'django.template.backends.django.DjangoTemplates',
                 'DIRS': [],
                 'APP_DIRS': True,
                 'OPTIONS': {
                     'context_processors': [
                         'django.template.context_processors.debug',
                         'django.core.context_processors.i18n',
                         'django.core.context_processors.media',
                         'django.template.context_processors.request',
                         'django.contrib.auth.context_processors.auth',
                         'django.core.context_processors.static',
                         'django.core.context_processors.tz',
                         'django.contrib.messages.context_processors.messages',
                     ],
                 },
             },
         ]

If you're using an older version of Django (< 1.8) then you'll want to change the 
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



    .. note:: N.b. versions below 1.8 are not officially supported.

    .. note:: If you don't have this setting defined, just add it to your settings module.

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

If you want your visitors to be able to reject the cookies, you should setup
`cookielaw` context processor by adding it to `TEMPLATE_CONTEXT_PROCESSORS`
like this:

    ::

        TEMPLATE_CONTEXT_PROCESSORS = (
            ...
            'cookielaw.context_processors.cookielaw'
        )

That will add ``cookielaw`` context variable to the template context. That
variable is a dict with 3 keys: ``notset``, ``accepted`` and ``rejected``, each
with ``true`` or ``false`` value.

Instead of default ``banner.html`` template, use ``rejectable.html`` one which
shows an example of how to reject the cookies (of course, you may change the
template to suit your own needs, just take care that you have
``<div id="CookielawBanner">`` container.

In your templates, you can choose to display the banner only for new visitors
(case when cookie is not set):

    ::

        {% load cookielaw_tags %}
        {% if cookielaw.notset %}{% rejectable_cookielaw_banner %}{% endif %}

Of course, you may use ``{% cookielaw_banner %}`` as well.

Once the visitors accepts or rejects the cookies, you may choose to load or not
load the analytics trackers:

    ::

        {% if cookielaw.accepted %}
            ... the code to load tracker ...
        {% endif %}

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/TyMaszWeb/django-cookie-law

:author: Piotr Kilczuk
:date: 2013/04/08

