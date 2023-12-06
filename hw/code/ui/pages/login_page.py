from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.LoginPageLocators()

    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BTN)
        self.fill(self.locators.MAIL_RU_LOGIN_INPUT, login)
        self.click(self.locators.MAIL_RU_ENTER_PASSWORD_BTN)
        self.fill(self.locators.MAIL_RU_PASSWORD_INPUT, password)
        self.click(self.locators.MAIL_RU_SUBMIT_BTN)
