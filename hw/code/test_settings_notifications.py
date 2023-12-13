import pytest

from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.fixtures import settings_notifications_page
from base import BaseCase


# @pytest.mark.skip('skip')
class TestSettingsNotifications(BaseCase):
    create_cabinet = True

    def test_disable_notifications(self, settings_notifications_page):
        settings_notifications_page.switch_notification_enabled()
        settings_notifications_page.find_element(settings_notifications_page.locators.WARNING_HINT)
        settings_notifications_page.is_options_disabled()

    @pytest.mark.parametrize(
        'option',
        SettingsNotificationsPage.OPTIONS,
    )
    def test_change_option(self, settings_notifications_page, option):
        settings_notifications_page.switch_option(option)
        settings_notifications_page.click(settings_notifications_page.locators.SAVE_BTN)
        settings_notifications_page.is_selected(settings_notifications_page.locators.checkbox_by_name(option),
                                                False)
        self.driver.refresh()
        settings_notifications_page.switch_option(option)
        settings_notifications_page.click(settings_notifications_page.locators.SAVE_BTN)
        settings_notifications_page.is_selected(settings_notifications_page.locators.checkbox_by_name(option),
                                                True)
