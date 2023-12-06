from selenium.webdriver.common.by import By


class BasePageLocators:
    @staticmethod
    def by_test_id(id):
        return By.CSS_SELECTOR, f"[data-test-id='{id}']"


class LoginPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BTN = BasePageLocators.by_test_id('oAuthService_mail_ru')
    MAIL_RU_LOGIN_INPUT = (By.NAME, 'username')
    MAIL_RU_ENTER_PASSWORD_BTN = BasePageLocators.by_test_id('next-button')
    MAIL_RU_PASSWORD_INPUT = (By.NAME, 'password')
    MAIL_RU_SUBMIT_BTN = BasePageLocators.by_test_id('submit-button')


class HqPageLocators(BasePageLocators):
    pass


class AudiencePageLocators(BasePageLocators):
    AUDIENCE_TAB = (By.ID, 'tab_audience')
    USERS_TAB = (By.ID, 'tab_audience.users_list')
