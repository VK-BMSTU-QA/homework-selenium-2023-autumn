from selenium.webdriver.common.by import By

class LoginPageLocators():
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//a[contains(@class, 'ButtonCabinet')]")
    OAUTH_MAIL_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")

    EMAIL_LOCATOR = (By.NAME, "username")
    ENTER_PASSWORD_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    RECAPTCHA_BTN_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'recaptcha-inter-next')]")

class CampaignPageLocators():
    SETTINGS_PAGE_LOCATOR = (By.XPATH, "//a[@data-entityid='settings']")
    ONBOARDING = (By.XPATH, "//button[.//span[.='Попробовать позже']]")
    TRIGGER_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//button[@class='vkuiButton__in']")
    CAMPAIGN_NAME = (By.XPATH, "//button[contains(@class, 'nameCellContent_link__')]")

class NewAdPlanPageLocators():
    SITE_LOCATOR = (By.XPATH, "//div[@id='site_conversions']")
    URL_INPUT_LOCATOR = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    BUDGET_INPUT_LOCATOR = (By.XPATH, '//input[@data-testid="targeting-not-set"]')
    NEXT_PAGE = (By.XPATH, '//button[@class="vkuiButton__in"]')

class NewAdPageLocators():
    TITLE_LOCATOR = (By.XPATH, '//input[contains(@name, "заголовок")]')
    SUMMARY_LOCATOR = (By.XPATH, '//textarea[@data-testid="text-field"]')
    AD_IMAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "LocalFileSelector_container__")]')
    NEXT_PAGE = (By.XPATH, '//button[.//span[.="Опубликовать"]]')
    CHOOSE_IMAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "ImageItems_active__")]')
    LOGO_BUTTON_LOCATOR= (By.XPATH, '//button[@data-testid="set-global-image"]')

class NewAdGroupPageLocators():
    REGION_INPUT_LOCATOR = (By.XPATH, '//input[@data-testid="search"]')
    REGION_RUSSIA_LOCATOR = (By.XPATH, '//button[.//span[.="Россия"]]')
    REGION_MOSCOW_LOCATOR = (By.XPATH, '//button[.//span[.="Москва"]]')
    REGION_PETERSBURG_LOCATOR = (By.XPATH, '//button[.//span[.="Санкт-Петербург"]]')
    CHECKBOX_LOCATOR = (By.XPATH, '//label[@class="vkuiCheckbox')
    NEXT_PAGE = (By.XPATH, '//button[.//span[.="Продолжить"]]')

class RegistrationPageLocators():
    SWITCH_ACCOUNT_LOCATOR = (By.XPATH, "//div[contains(@class, 'AccountSwitch_changeAccountName')]")
    CREATE_CABINET_LOCATOR = (By.ID, "click-createNewButton")
    EMAIL_LOCATOR = (By.NAME, "email")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'create-button')]")
   
class BasePageAuthorizedLocators():
    pass

class SettingsLocators():
    DELETE_ACCOUNT_LOCATOR = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    MODAL_ACTIONS_DELETE_ACCOUNT = (By.XPATH, "//div[contains(@class, 'DeleteAccountConfirmModal_actions')]")
    CONFIRM_DELETE_ACCOUNT = (By.XPATH,
                              "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--appearance-negative')]")
