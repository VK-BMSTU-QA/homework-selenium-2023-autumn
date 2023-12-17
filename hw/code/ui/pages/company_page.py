from ui.pages.base_page import BasePage
from ui.locators.company import CompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CompanyPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CompanyPageLocators

    def create_company(self, timeout=None):
        self.click(self.locators.CREATE_BUTTON, timeout=timeout)

    