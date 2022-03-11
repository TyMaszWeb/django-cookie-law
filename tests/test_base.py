import six
import pytest
from django.utils.translation import gettext as _


@pytest.fixture()
def content(client):
    response = client.get('/')
    assert response.status_code == 200
    return response.content


def test_banner_shows(content):
    assert 'CookielawBanner' in content


def test_banner_contains_correct_text(content):
    assert _('COOKIE_INFO_HEADER') in content
    assert _('COOKIE_INFO_PARA') in content
    assert _('COOKIE_INFO_OK') in content
