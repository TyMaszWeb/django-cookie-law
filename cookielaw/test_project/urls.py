from __future__ import absolute_import

from django.conf.urls import patterns, include, url


from .test_app.views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
)
