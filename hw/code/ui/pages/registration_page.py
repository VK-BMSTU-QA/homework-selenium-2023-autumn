import time

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class RegistrationPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/registration.*$'

    locators = basic_locators.RegistrationPageLocators

    def get_user_data(self):
        element = self.find(self.locators.SWITCH_ACCOUNT_LOCATOR)
        return element.get_attribute('innerText')

