import pytest
from ui.pages.settings_page import SettingsPage
from ui.fixtures import settings_page
from base import BaseCase


# @pytest.mark.skip('skip')
class TestSettings(BaseCase):
    create_cabinet = True
    general_info_set = True

    @pytest.mark.parametrize(
        'tab_name,tab_url',
        [
            pytest.param(SettingsPage.GENERAL_TAB, 'https://ads.vk.com/hq/settings'),
            pytest.param(SettingsPage.NOTIFICATIONS_TAB, 'https://ads.vk.com/hq/settings/notifications'),
            pytest.param(SettingsPage.ACCESS_TAB, 'https://ads.vk.com/hq/settings/access'),
            pytest.param(SettingsPage.HISTORY_TAB, 'https://ads.vk.com/hq/settings/logs'),
        ]
    )
    def test_tab_navigation(self, settings_page, tab_name, tab_url):
        settings_page.go_to_tab(tab_name)
        settings_page.check_url(tab_url)

    def test_chars_in_phone(self, settings_page):
        settings_page.edit_general(phone='abc')
        settings_page.find_element(settings_page.locators.PHONE_INVALID_ERROR)

    def test_empty_phone(self, settings_page):
        settings_page.edit_general(phone='')
        settings_page.find_element(settings_page.locators.PHONE_INVALID_ERROR)

    def test_empty_fio(self, settings_page):
        settings_page.edit_general(fio='')
        settings_page.find_element(settings_page.locators.FIO_INVALID_ERROR)

    def test_digits_in_fio(self, settings_page):
        settings_page.edit_general(fio='123')
        settings_page.find_element(settings_page.locators.FIO_INVALID_CHARS_ERROR)

    def test_empty_inn(self, settings_page):
        settings_page.edit_general(inn='')
        settings_page.find_element(settings_page.locators.INN_INVALID_ERROR)

    def test_chars_in_inn(self, settings_page):
        settings_page.edit_general(inn='abc')
        settings_page.find_element(settings_page.locators.INN_INVALID_ERROR)

    def test_too_short_inn(self, settings_page):
        settings_page.edit_general(inn='12345678901')
        settings_page.find_element(settings_page.locators.INN_TOO_SHORT_ERROR)
