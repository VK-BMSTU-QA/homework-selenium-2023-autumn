from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    LOGIN_OAUTH_MAIL_BUTTON = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")
    LOGIN_ENTER_PASSWORD_BUTTON = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    LOGIN_EMAIL_INPUT = (By.NAME, "username")
    LOGIN_PASSWORD_INPUT = (By.NAME, "password")
