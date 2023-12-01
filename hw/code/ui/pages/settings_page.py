import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized
from ui.pages.login_page import LoginPage


class SettingsPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/settings.*$'

    locators = basic_locators.SettingsLocators

    @allure.step("Deleting account")
    def delete_account(self):
        self.click(self.locators.DELETE_ACCOUNT_LOCATOR)
        modal_window = self.find(self.locators.MODAL_ACTIONS_DELETE_ACCOUNT)
        self.click(self.locators.CONFIRM_DELETE_ACCOUNT, obj=modal_window)

        return LoginPage(self.driver)

    # def get_bio(self):
    #     result = self.find(self.locators.BIO_LOCATOR)
    #     return result.get_attribute('value')

    # def edit_bio(self, new_bio):
    #     self.fill_field(self.locators.BIO_LOCATOR, new_bio)
    #     self.click(self.locators.SETTING_SUBMIT_LOCATOR)
