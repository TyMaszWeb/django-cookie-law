from selenium.common.exceptions import NoSuchElementException
import pytest
import time


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test_banner_shows_and_hides(selenium, live_server):
    selenium.get(live_server.url)
    cookielaw_banner = selenium.find_element_by_id('CookielawBanner')

    # on click of the button, cookie set and banner hidden
    cookielaw_banner.find_element_by_class_name('btn').click()
    assert not cookielaw_banner.is_displayed()
    assert '1' == selenium.get_cookie('cookielaw_accepted')['value']

    # on come back, assert banner gone
    selenium.get(live_server.url)

    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_id('CookielawBanner')


def test_banner_shows_and_hides_with_jquery(selenium, live_server):
    # now, with jQuery
    selenium.get('{}/?jquery=1'.format(live_server.url))
    cookielaw_banner = selenium.find_element_by_id('CookielawBanner')

    # on click of the button, cookie set and banner hidden
    cookielaw_banner.find_element_by_class_name('btn').click()
    time.sleep(1)
    assert not cookielaw_banner.is_displayed()
    assert '1' == selenium.get_cookie('cookielaw_accepted')['value']
