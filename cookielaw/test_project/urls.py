from __future__ import absolute_import

from django.conf import settings
from django.urls import re_path
from django.views import static

from .test_app.views import HomeView, AcceptedView, RejectableView, RejectedView

urlpatterns = [
    re_path(r'^$', HomeView.as_view()),
    re_path('^accepted$', AcceptedView.as_view()),
    re_path('^rejectable$', RejectableView.as_view()),
    re_path('^rejected$', RejectedView.as_view()),

    re_path(r'^static', static.serve, {'document_root': settings.STATIC_ROOT}),
]
