import pytest
from django.utils.translation import gettext as _


@pytest.fixture()
def content(client):
    response = client.get("/")
    assert 200 == response.status_code
    return response.content.decode("utf-8")


def test_banner_shows(content):
    assert "CookielawBanner" in content


def test_banner_contains_correct_text(content):
    assert _("COOKIE_INFO_HEADER") in content
    assert _("COOKIE_INFO_PARA") in content
    assert _("COOKIE_INFO_OK") in content
