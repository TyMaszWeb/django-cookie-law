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

- Django >= 1.2
- django-classy-tags >= 0.3.0

Installation
============

#. ``pip install django-cookie-law``
#. Add ``'cookielaw'`` to ``INSTALLED_APPS``
#. Run ``collectstatic`` (Django 1.3+) or copy the statics to your media directory
#. Add ``cookielaw/js/cookielaw.js`` to the markup directly or via your asset
   manager such as ``django-pipeline`` or ``django-compressor``
#. Add ``cookielaw`` to your ``INSTALLED_APPS``
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

Changelog
=========

* **1.0.12** added German translation thanks to dated_
* **1.0.11** added Catalan translation thanks to joansv_
* **1.0.9** added unofficial support for Django 1.10 thanks to farin_
* **1.0.8** added Spanish translation thanks to jonashagstedt_
* **1.0.7** added Russian translation thanks to paschembri_
* **1.0.6** ``django.core.context_processors.request`` is still required but if not available in template context a
  warning will be raise instead of a ``KeyError``
* **1.0.5** added Dutch translation thanks to douwevandermeij_
* **1.0.4** context_instance is now passed to the banner template
* **1.0.3** added Italian translation thanks to Jiloc_

Some very minor changes have not been listed.


Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/TyMaszWeb/django-cookie-law

:author: Piotr Kilczuk
:date: 2013/04/08

.. _dated: https://github.com/dated
.. _douwevandermeij: https://github.com/douwevandermeij
.. _farin: https://github.com/farin
.. _Jiloc: https://github.com/Jiloc
.. _joansv: https://github.com/joansv
.. _jonashagstedt: https://github.com/jonashagstedt
.. _paschembri: https://github.com/paschembri
