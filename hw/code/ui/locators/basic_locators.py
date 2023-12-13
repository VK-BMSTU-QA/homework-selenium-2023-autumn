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
    
    ONBOARDING_LOCATOR = (By.XPATH, "//div[contains(@class, 'ModalManagerPage_modalContent')]")
    ONBOARDING_CLOSE_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiModalDismissButton')]")
    HELP_LOCATOR = (By.XPATH, "//div[contains(@class, 'Content_container_')]")
    HELP_CLOSE_LOCATOR = (By.XPATH, "//button[contains(@class, 'CloseButton_wrapper_')]")
    ONBOARDING = (By.XPATH, "//*[@id='_modal_18']/div/div/div[3]")
    TRIGGER_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//*[@id='adPlan']/div/div[2]/div/div[1]/div/div[1]/a")

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
