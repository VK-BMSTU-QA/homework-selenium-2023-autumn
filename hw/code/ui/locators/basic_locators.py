from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators(BasePageLocators):
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//a[contains(@class, 'ButtonCabinet')]")
    OAUTH_MAIL_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")

    EMAIL_LOCATOR = (By.NAME, "username")
    ENTER_PASSWORD_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    RECAPTCHA_BTN_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'recaptcha-inter-next')]")


class RegistrationPageLocators(BasePageLocators):
    SWITCH_ACCOUNT_LOCATOR = (By.XPATH, "//div[contains(@class, 'AccountSwitch_changeAccountName')]")
   
class BasePageAuthorizedLocators(BasePageLocators):
    pass