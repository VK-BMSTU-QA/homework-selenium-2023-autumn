import allure

from ui.pages.main_page import MainPage
from ui.pages.campaign.campaign_page import CampaignPage
from ui.locators.login.basic_locators import LoginPageLocators


class LoginPage(MainPage):
    locators = LoginPageLocators

    @allure.step("Login")
    def login(self, email, password):
        self.click(self.locators.MAIN_MOVE_TO_CABINET_BUTTON, timeout=30)
        self.click(self.locators.LOGIN_OAUTH_MAIL_BUTTON, timeout=30)
        self.fill_field(self.locators.LOGIN_EMAIL_INPUT, email)
        self.click(self.locators.LOGIN_ENTER_PASSWORD_BUTTON)
        self.fill_field(self.locators.LOGIN_PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_SUBMIT_BUTTON)

        return CampaignPage(self.driver)
