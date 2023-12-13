import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized
from ui.pages.login_page import LoginPage


class SettingsPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/settings.*$'

    locators = basic_locators.SettingsLocators
    sections = {
        'common': locators.COMMON_SECTION_LOCATOR,
        'notifications': locators.NOTIFICATIONS_SECTION_LOCATOR,
        'access': locators.ACCESS_SECTION_LOCATOR,
        'logs': locators.LOGS_SECTION_LOCATOR,
    }

    @allure.step("Deleting account")
    def delete_account(self):
        self.click(self.locators.DELETE_ACCOUNT_LOCATOR)
        modal_window = self.find(self.locators.MODAL_ACTIONS_DELETE_ACCOUNT)
        self.click(self.locators.CONFIRM_DELETE_ACCOUNT, obj=modal_window)

        return LoginPage(self.driver)
    
    @allure.step("Editing account")
    def edit_account_info(self, data):
        self.fill_field(self.locators.PHONE_LOCATOR, data['phone'])
        self.fill_field(self.locators.FIO_LOCATOR, data['fio'])
        self.fill_field(self.locators.INN_LOCATOR, data['inn'])
        self.click(self.locators.SAVE_BUTTON_LOCATOR)

    @allure.step("Getting account")
    def get_account_info(self):
        return {
            'phone': self.find(self.locators.PHONE_LOCATOR).get_attribute('value'),
            'fio': self.find(self.locators.FIO_LOCATOR).get_attribute('value'),
            'inn': self.find(self.locators.INN_LOCATOR).get_attribute('value'),
        }
    
    @allure.step("Opening section {section_name}")
    def open_section(self, section_name):
        super().move_to(section_name, sections=self.sections)

    def get_inner_html_of_form(self):
        form = self.find(self.locators.FORM_LOCATOR)
        return form.get_attribute("innerHTML")


class SettingsNotificationsPage(SettingsPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/settings\/notifications.*$'

    locators = basic_locators.SettingsNotificationsLocators


class SettingsAccessPage(SettingsPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/settings\/access.*$'

    locators = basic_locators.SettingsAccessLocators


class SettingsLogsPage(SettingsPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/settings\/logs.*$'

    locators = basic_locators.SettingsLogsLocators
