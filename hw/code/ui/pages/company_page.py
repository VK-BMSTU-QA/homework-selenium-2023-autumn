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

    def multiple_find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def create_company(self, timeout=None):
        self.click(self.locators.CREATE_BUTTON, timeout=timeout)

    def download(self, timeout=None):
        element = self.find(self.locators.DOWNLOAD_BUTTON, timeout=timeout)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

        return self

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
        return self

    def select_deleted_filter(self):
        element = self.find(self.locators.DELETED_FILTER)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

        return self

    def select_started_filter(self):
        element = self.find(self.locators.STARTED_FILTER)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

        return self

    def apply_filters(self):
        self.click(self.locators.FILTER_APPLY_BUTTON)
        return self

    def select_company(self, number_of_company=0):
        elements = self.multiple_find(self.locators.COMPANY_OPTIONS)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(elements[number_of_company])
        actions.click(elements[number_of_company])
        actions.perform()

        return self

    def select_action_list(self):
        element = self.find(self.locators.ACTION_SELECTOR)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

        return self

    def select_delete_action(self):
        element = self.find(self.locators.DELETE_ACTION)

        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

        return self

    def is_on_site_text(self, text: str, timeout: int = 5):
        returnVal = False
        try:
            returnVal = self.wait(timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{text}')]")
                )
            )
        except Exception as e:
            returnVal = False

        return returnVal

    def go_to_drafts(self):
        self.click(self.locators.DRAFT_BUTTON)
        return self

    def delete_draft(self):
        self.click(self.locators.DELETE_DRAFT)
        return self
