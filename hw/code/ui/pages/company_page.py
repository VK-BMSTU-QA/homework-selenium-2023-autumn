from ui.pages.base_page import BasePage
from ui.locators.company import CompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CompanyPage(BasePage):
    url = "https://ads.vk.com/hq/dashboard/ad_plans?mode=ads&attribution=impression&sort=-created"
    locators = CompanyPageLocators

    def create_company(self, timeout=None):
        self.click(self.locators.CREATE_BUTTON, timeout=timeout)

    def download(self, timeout=None):
        element = self.find(self.locators.DOWNLOAD_BUTTON, timeout=timeout)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def settings(self, timeout=None):
        element = self.find(self.locators.SETTINGS_BUTTON, timeout=timeout)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def action(self, timeout=None):
        self.click(self.locators.ACTION_SELECTOR, timeout=timeout)

    def group_view(self, timeout=None):
        self.click(self.locators.GROUP_BUTTON, timeout=timeout)

    def advertisment_view(self, timeout=None):
        self.click(self.locators.ADVERTISEMENTS_BUTTON, timeout=timeout)

    def select_filter(self, timoeut=None):
        self.click(self.locators.FILTER_BUTTON, 5)
