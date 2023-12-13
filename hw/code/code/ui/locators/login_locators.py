from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.ID, "popup-login-form-submit")
    USER_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')