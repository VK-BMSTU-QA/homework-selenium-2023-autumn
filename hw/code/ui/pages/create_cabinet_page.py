from ui.locators import basic_locators
from ui.pages.hq_page import HqPage
from selenium.webdriver.support import expected_conditions as EC


class CreateCabinetPage(HqPage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = basic_locators.CreateCabinetPageLocators

    def select_country(self, country_name):
        self.click(self.locators.COUNTRY_SELECT)
        self.click(self.locators.by_option(country_name))

    def available_currencies(self, first_currency):
        self.wait().until(EC.text_to_be_present_in_element(self.locators.CURRENCY_SELECT, first_currency))
        self.click(self.locators.CURRENCY_SELECT)
        currencies = self.find_elements(self.locators.OPTIONS)
        titles = tuple(currency.get_attribute("title") for currency in currencies)
        return titles

    def fill_email(self, email):
        self.fill(self.locators.EMAIL_FIELD, email)

    def switch_terms(self):
        self.click(self.locators.TERMS_CHECK)

    def submit_form(self):
        self.click(self.locators.SUBMIT_BTN)

    def has_email_error(self):
        elem = self.find_element(self.locators.EMAIL_ERROR)
        return elem.text == "Обязательное поле"

    def has_form_error(self):
        elem = self.find_element(self.locators.FORM_ERROR)
        return elem.text == 'Ошибка\nValidation failed'

    def has_terms_error(self):
        elem = self.find_element(self.locators.TERMS_ERROR)
        return elem.text == "Обязательное поле"
