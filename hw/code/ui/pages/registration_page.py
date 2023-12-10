from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.RegistrationPageLocators()

    def create_cabinet(self):
        self.click(self.locators.CREATE_CABINET_BTN)
