from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.RegistrationPageLocators()

    lang_tabs = {
        'ru': locators.RU_TAB,
        'en': locators.EN_TAB,
    }
    lang_titles = {
        'ru': 'Создать новый кабинет',
        'en': 'Create a new account',
    }

    def create_cabinet(self):
        self.click(self.locators.CREATE_CABINET_BTN)

    def choose_language(self, lang):
        locator = self.lang_tabs[lang]
        self.click(locator)

    def is_language(self, lang):
        self.has_text(self.locators.CREATE_CABINET_BTN, self.lang_titles[lang])

    def logout(self):
        self.click(self.locators.AVATAR_BTN)
        self.click(self.locators.LOGOUT_BTN)
