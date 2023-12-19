from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.new_company import NewCompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NewCompanyPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan"
    locators = NewCompanyPageLocators

    def create(self):
        self.click(self.locators.CREATE_BUTTON)

    def download(self):
        self.click(self.locators.CREATE_BUTTON)

    def settings(self):
        self.click(self.locators.SETTINGS_BUTTON)

    def action(self):
        self.click(self.locators.ACTION_SELECTOR)
