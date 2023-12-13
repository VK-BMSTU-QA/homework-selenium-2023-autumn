import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MonetizationPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/partner.*$'

    locators = basic_locators.MonetizationPageLocators

    def find_monetization_section(self):
        return self.find_list(self.locators.MONETIZATION_ITEMS_LOCATOR)

    def find_monetization_buttons(self):
        return self.find_list(self.locators.MONETIZATION_TOGGLE_LOCATOR)

    def click_app_button(self):
        buttons = self.find_monetization_buttons()
        self.scroll_to(buttons[1])
        elem = self.wait(timeout=5).until(EC.element_to_be_clickable(buttons[1]))
        elem.send_keys("\n")

    def fill_name(self):
        self.click(self.locators.MONETIZATION_NAME_LOCATOR)
        self.fill_field(self.locators.MONETIZATION_NAME_LOCATOR, "Иван")
        self.click(self.locators.MONETIZATION_NAME_LOCATOR)

    def fill_email(self):
        self.click(self.locators.MONETIZATION_EMAIL_LOCATOR)
        self.fill_field(self.locators.MONETIZATION_EMAIL_LOCATOR, "test@mailbx.ru")
        self.click(self.locators.MONETIZATION_EMAIL_LOCATOR)

    def get_form_button(self):
        return self.find(self.locators.MONETIZATION_FORM_BUTTON_LOCATOR)

    def click_form_button(self):
        self.click(self.locators.MONETIZATION_FORM_BUTTON_LOCATOR)

    def get_success_form(self):
        return self.find(self.locators.MONETIZATION_FORM_SUCCESS_LOCATOR)
