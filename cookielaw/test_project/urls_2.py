from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import url
from django.views import static


from .test_app.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^static', static.serve, {'document_root': settings.STATIC_ROOT}),
]
