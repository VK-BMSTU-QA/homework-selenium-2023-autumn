import time

from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.hq_page import HqPage


class SettingsPage(HqPage):
    GENERAL_TAB = 'general'
    NOTIFICATIONS_TAB = 'notifications'
    ACCESS_TAB = 'access'
    HISTORY_TAB = 'history'

    url = 'https://ads.vk.com/hq/settings'
    locators = basic_locators.SettingsPageLocators

    tabs = {
        GENERAL_TAB: locators.GENERAL_TAB,
        NOTIFICATIONS_TAB: locators.NOTIFICATIONS_TAB,
        ACCESS_TAB: locators.ACCESS_TAB,
        HISTORY_TAB: locators.HISTORY_TAB,
    }

    def go_to_tab(self, tab_name):
        locator = self.tabs[tab_name]
        self.click(locator)

    def delete_cabinet(self):
        self.click(self.locators.DELETE_CABINET_BTN)
        self.click(self.locators.CONFIRM_DELETE_CABINET_BTN)
        BasePage(driver=self.driver).is_opened()
        self.is_visible(self.locators.GO_TO_CABINET_BTN)

    def edit_general(self, phone=None, fio=None, inn=None):
        if phone is not None:
            self.fill(self.locators.PHONE_INPUT, ' ')
            self.fill(self.locators.PHONE_INPUT, phone)
        if fio is not None:
            self.fill(self.locators.FIO_INPUT, ' ')
            self.fill(self.locators.FIO_INPUT, fio)
        if inn is not None:
            self.fill(self.locators.INN_INPUT, ' ')
            self.fill(self.locators.INN_INPUT, inn)
        time.sleep(5)
        self.click(self.locators.SAVE_BTN)
