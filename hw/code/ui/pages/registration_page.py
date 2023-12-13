import time

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized
from ui.pages.campaign_page import CampaignPage


class RegistrationPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/registration.*$'

    locators = basic_locators.RegistrationPageLocators

    @allure.step("Creating cabinet")
    def create_cabinet(self, data):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        self.fill_field(self.locators.EMAIL_LOCATOR, data['email'])
        self.click(self.locators.SUBMIT_LOCATOR)

        return CampaignPage(self.driver)

    @allure.step("Filling agency type of cabinet")
    def fill_agency_type(self):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        physic = self.find(self.locators.PHYS_AC_TYPE_LOCATOR)
        checkboxes = self.find_list(self.locators.AC_TYPES_CHECKBOX_LOCATOR)
        if len(checkboxes) >= 3:
            checkboxes[1].click()
            self.wait_for_remove(physic)
        else:
            raise "wrong checkboxes format"

    @allure.step("Creating cabinet without email")
    def create_cabinet_empty_email(self):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        self.click(self.locators.SUBMIT_LOCATOR)

    def get_email_error_message(self):
        el = self.find(self.locators.BOTTOM_ERROR_LOCATOR)
        return el.get_attribute("innerText")

    def get_rules_error_message(self):
        el = self.find(self.locators.BOTTOM_ERROR_LOCATOR)
        return el.get_attribute("innerText")

    def get_email_format_error_message(self):
        el = self.find(self.locators.BOTTOM_ERROR_LOCATOR)
        return el.get_attribute("innerText")

    @allure.step("Creating cabinet without accept")
    def create_cabinet_without_accept(self, data):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        self.fill_field(self.locators.EMAIL_LOCATOR, data['email'])
        self.click(self.locators.ACCEPT_RULES_LOCATOR)
        self.click(self.locators.SUBMIT_LOCATOR)

    @allure.step("Creating cabinet wrong email")
    def create_cabinet_with_wrong_email(self, email):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        self.fill_field(self.locators.EMAIL_LOCATOR, email)
        self.click(self.locators.SUBMIT_LOCATOR)

    def get_allowed_ac_types(self):
        types = self.find_list(self.locators.AC_TYPES_LOCATOR)
        res_types = []
        for t in types:
            res_types.append(t.get_attribute("innerText"))

        return res_types[:len(res_types)-1]

    def get_user_data(self):
        element = self.find(self.locators.SWITCH_ACCOUNT_LOCATOR)
        return element.get_attribute('innerText')
