import time

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage, BasePageAuthorized
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class SitesPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/pixels.*$'

    locators = basic_locators.SitesPageLocators

    def confirm_new_pixel(self):
        self.logger.debug("checking exists confirmation modal for creting pixel")

        if self.has_object(self.locators.PIXEL_CONFIRMATION_LOCATOR):
            self.logger.debug("confirmation exists")

            with allure.step("confirming_new_pixel"):
                self.click(self.locators.CREATE_NEW_PIXEL_LOCATOR)
        else:
            self.logger.debug("confirmation modal not exist")

    @allure.step("Creating pixel")
    def create_pixel(self, data):
        self.click(self.locators.ADD_PIXEL_BUTTON_LOCATOR)
        input = self.click(self.locators.PIXEL_DOMAIN_FIELD_LOCATOR)
        input.send_keys(data['by_domain']['domain'])
        input.send_keys(Keys.ENTER)
        pixel_modal = self.find(self.locators.PIXEL_MODAL_LOCATOR)
        self.click(self.locators.ADD_PIXEL_BUTTON_MAIN_LOCATOR, obj=pixel_modal)
        self.confirm_new_pixel()
        self.click(self.locators.CLOSE_CREATE_PIXEL_LOCATOR)

    @allure.step("Deleting pixel")
    def delete_pixel(self, domain):
        res, pixel = self.find_pixel_by_domain(domain)
        if not res:
            raise "pixel not found for delete"
        self.hover_and_click(self.locators.MORE_PIXEL_BUTTON_LOCATOR, obj=pixel)
        self.click(self.locators.DELETE_PIXEL_LOCATOR)
        self.click(self.locators.CONFIRM_DELETE_PIXEL_LOCATOR)
        self.wait_for_remove(pixel)

    def find_pixel_by_domain(self, domain, timeout=5):
        try:
            campaigns = self.find(self.locators.PIXEL_LIST_LOCATOR, timeout=timeout)
            pixel = self.find((self.locators.PIXEL_FORMAT_LOCATOR[0], self.locators.PIXEL_FORMAT_LOCATOR[1].format(domain)), timeout=timeout)
            return True, pixel
        except TimeoutException:
            return False, None
