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


def test_text_is_not_rendered_unless_cookies_are_accepted(selenium, live_server):
    selenium.get(f'{live_server.url}/accepted')
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_id('msg')


def test_context_processors_puts_variable_into_context(selenium, live_server):
    # accept cookies
    selenium.get(live_server.url)
    cookielaw_banner = selenium.find_element_by_id('CookielawBanner')
    cookielaw_banner.find_element_by_class_name('btn').click()

    # go to different page and test if context_processor filled the
    # accepted_cookies variable
    selenium.get(f'{live_server.url}/accepted')
    msg = selenium.find_element_by_id('msg')
    assert msg
    assert msg.text == 'Cookies are good.'


def test_reject_cookies_hides_banner(selenium, live_server):
    # load page with rejectable banner and click reject button
    selenium.get(f'{live_server.url}/rejectable')
    selenium.find_element_by_id('CookielawBanner').find_element_by_class_name('reject').click()

    # reload the page and the banner should not be displayed
    selenium.get(live_server.url)
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_id('CookielawBanner')


def test_cookies_rejected_context_processor(selenium, live_server):
    # load page with rejectable banner and click reject button
    selenium.get(f'{live_server.url}/rejectable')
    selenium.find_element_by_id('CookielawBanner').find_element_by_class_name('reject').click()

    # go to different page and test if context_processor filled the
    # cookielaw_rejected variable
    selenium.get(f'{live_server.url}/rejected')
    msg = selenium.find_element_by_id('msg')
    assert msg
    assert msg.text == 'Cookies are bad.'
