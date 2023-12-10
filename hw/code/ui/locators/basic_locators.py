from selenium.webdriver.common.by import By


class BasePageLocators:
    GO_TO_CABINET_BTN = By.CLASS_NAME, 'ButtonCabinet_primary__KQnu7'
    OPTIONS = (By.XPATH, f"//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")

    @staticmethod
    def by_css_selector(selector, id):
        return By.CSS_SELECTOR, f"[{selector}='{id}']"

    @staticmethod
    def by_option(text):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']"


class LoginPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BTN = BasePageLocators.by_css_selector('data-test-id', 'oAuthService_mail_ru')
    MAIL_RU_LOGIN_INPUT = (By.NAME, 'username')
    MAIL_RU_ENTER_PASSWORD_BTN = BasePageLocators.by_css_selector('data-test-id', 'next-button')
    MAIL_RU_PASSWORD_INPUT = (By.NAME, 'password')
    MAIL_RU_SUBMIT_BTN = BasePageLocators.by_css_selector('data-test-id', 'submit-button')


class RegistrationPageLocators(BasePageLocators):
    CREATE_CABINET_BTN = BasePageLocators.by_css_selector('data-testid', 'create-new')


class CreateCabinetPageLocators(BasePageLocators):
    AGENCY_RADIO = (By.XPATH, f".//*[text()='Агентство']")
    PHYSICAL_RADIO = BasePageLocators.by_css_selector('data-testid', 'physical')
    COUNTRY_SELECT = BasePageLocators.by_css_selector('data-testid', 'country')
    CURRENCY_SELECT = BasePageLocators.by_css_selector('data-testid', 'currency')
    EMAIL_FIELD = BasePageLocators.by_css_selector('data-testid', 'email')
    TERMS_CHECK = (By.CLASS_NAME, "registration_offerTitle__BqyqW")
    SUBMIT_BTN = BasePageLocators.by_css_selector('data-testid', 'create-button')
    EMAIL_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    TERMS_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    FORM_ERROR = (By.CLASS_NAME, 'vkuiFormStatus--mode-error')


class HqPageLocators(BasePageLocators):
    pass


class AudiencePageLocators(BasePageLocators):
    AUDIENCE_TAB = (By.ID, 'tab_audience')
    USERS_TAB = (By.ID, 'tab_audience.users_list')
