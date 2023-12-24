import pytest

from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.fixtures import settings_notifications_page
from base import BaseCase


class TestSettingsNotifications(BaseCase):
    @staticmethod
    def check_change(option, state, settings_notifications_page):
        settings_notifications_page.switch_option(option)
        settings_notifications_page.click(settings_notifications_page.locators.SAVE_BTN)
        settings_notifications_page.is_invisible(settings_notifications_page.locators.SAVE_PANEL)
        settings_notifications_page.is_selected(settings_notifications_page.locators.checkbox_by_name(option), state)

    def test_disable_notifications(self, settings_notifications_page):
        settings_notifications_page.switch_notification_enabled()
        settings_notifications_page.find_element(settings_notifications_page.locators.WARNING_HINT)
        settings_notifications_page.is_options_disabled()

    def test_change_option(self, settings_notifications_page):
        for option in SettingsNotificationsPage.OPTIONS:
            self.check_change(option, False, settings_notifications_page)
            self.check_change(option, True, settings_notifications_page)
