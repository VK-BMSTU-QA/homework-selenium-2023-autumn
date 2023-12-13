from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from locators.login_locators import LoginPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    url = 'https://ads.vk.com/hq/'

    def setTextInLocatorElement(self, locator, text):
        element: WebElement = self.find(locator)

        element.clear()
        element.send_keys(text)


    def login(self, user, password):
        submit: WebElement = self.find(LoginPageLocators.LOGIN)
        self.setTextInLocatorElement(LoginPageLocators.USER_FIELD, user)
        self.setTextInLocatorElement(LoginPageLocators.PASSWORD_FIELD, password)

        submit.click()
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Блоги")))

        return BasePage(self.driver)