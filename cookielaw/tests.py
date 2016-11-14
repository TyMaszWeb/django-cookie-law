import logging
import time

from django.test import LiveServerTestCase
from django.utils.translation import ugettext as _
from selenium import webdriver
from selenium.common.exceptions import *


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        logging.debug('setUp')

        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(6)

    def tearDown(self):
        logging.debug('tearDown')

        self.browser.quit()

    def test_banner_shows_and_hides_jquery(self):
        logging.debug('test_banner_shows_and_hides_jquery')

        self.browser.get('http://localhost:8081/?jquery=1')
        cookielaw_banner = self.browser.find_element_by_id('CookielawBanner')

        # contains header, paragraph and agree button
        self.assertIn(_('COOKIE_INFO_HEADER'), cookielaw_banner.text)
        self.assertIn(_('COOKIE_INFO_PARA'), cookielaw_banner.text)
        self.assertIn(_('COOKIE_INFO_OK'), cookielaw_banner.text)

        # on click of the button, cookie set and banner hidden
        cookielaw_banner.find_element_by_class_name('btn').click()
        time.sleep(1)
        self.assertFalse(cookielaw_banner.is_displayed())
        self.assertEqual(self.browser.get_cookie('cookielaw_accepted')['value'], '1')

        # on come back, assert banner gone
        self.browser.get('http://localhost:8081/?jquery=1')
        self.assertRaises(NoSuchElementException,
            lambda: self.browser.find_element_by_id('CookielawBanner'))

    def test_banner_shows_and_hides_no_jquery(self):
        logging.debug('test_banner_shows_and_hides_no_jquery')

        self.browser.get('http://localhost:8081/')
        cookielaw_banner = self.browser.find_element_by_id('CookielawBanner')

        # contains header, paragraph and agree button
        self.assertIn(_('COOKIE_INFO_HEADER'), cookielaw_banner.text)
        self.assertIn(_('COOKIE_INFO_PARA'), cookielaw_banner.text)
        self.assertIn(_('COOKIE_INFO_OK'), cookielaw_banner.text)

        # on click of the button, cookie set and banner hidden
        cookielaw_banner.find_element_by_class_name('btn').click()
        self.assertFalse(cookielaw_banner.is_displayed())
        self.assertEqual(self.browser.get_cookie('cookielaw_accepted')['value'], '1')

        # on come back, assert banner gone
        self.browser.get('http://localhost:8081/')
        self.assertRaises(NoSuchElementException,
            lambda: self.browser.find_element_by_id('CookielawBanner'))
