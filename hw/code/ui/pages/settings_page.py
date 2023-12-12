from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.hq_page import HqPage


class SettingsPage(HqPage):
    url = 'https://ads.vk.com/hq/settings'
    locators = basic_locators.SettingsPageLocators

    def delete_cabinet(self):
        self.click(self.locators.DELETE_CABINET_BTN)
        self.click(self.locators.CONFIRM_DELETE_CABINET_BTN)
        BasePage(driver=self.driver).is_opened()
