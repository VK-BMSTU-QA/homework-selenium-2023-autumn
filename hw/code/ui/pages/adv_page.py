import time
import re

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.adv import AdvLocators
from ui.pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class AdvPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan/"
    locators = AdvLocators

    def multiple_find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def action_click(self, element):
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

    def site_region_click(self):
        self.click(self.locators.SEARCH_INPUT)
        el = self.find(self.locators.SEARCH_INPUT)
        el.send_keys("Россия", Keys.RETURN)

        self.click(self.locators.REGION_VARIANTS)
        return self

    # HACK
    def wait_load_page(self):
        self.multiple_find(self.locators.SAVE_TEXT)[0]

        return self

    def get_page(self):
        # First page of creating company
        self.click(self.locators.SITE_REGION, 10)
        el = self.find(self.locators.SITE_INPUT)
        self.driver.implicitly_wait(5)
        el.click()
        el.clear()
        el.send_keys("ababa.com", Keys.RETURN)

        el = self.find(self.locators.COST_INPUT)
        el.clear()
        el.send_keys(106, Keys.RETURN)

        self.action_click(self.find(self.locators.CONTINUE_BUTTON, 5))

        # TODO make good load page
        # self.wait_load_page()

        self.site_region_click().click_continue_button()

        return self

    def click_continue_button(self):
        el = self.multiple_find(self.locators.FOOTER_BUTTONS)[1]
        self.action_click(el)
        return self

    def send_text_to_title(self, text: str):
        el = self.multiple_find(self.locators.INPUT_TITLE)[0]
        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def get_title_max(self) -> int:
        el = self.multiple_find(self.locators.COUNTS_CHARS)[0]
        text = el.text

        # XXX
        matches = re.search(r"\d+ / (\d+)", text)
        count_chars_value = 0
        if matches:
            count_chars_value = int(matches.group(1))

        return count_chars_value

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

    def send_url(self, url: str):
        el = self.find(self.locators.URL_INPUT)
        el.clear()
        el.send_keys(url, Keys.RETURN)
        return self

    def select_logo(self, number_of_logo: int):
        self.action_click(self.find(self.locators.LOGO_INPUT))
        el = self.multiple_find(self.locators.LOG_VARIANTS)[number_of_logo]

        self.action_click(el)
        return self

    def write_to_inputs(self, text: str):
        inputs = self.multiple_find(self.locators.TEXT_INPUTS)

        for i in inputs:
            i.clear()
            i.send_keys(text, Keys.RETURN)

        return self

    def write_to_textarea(self, text: str):
        areas = self.multiple_find(self.locators.AREA_INPUTS)
        for i in areas:
            i.clear()
            i.send_keys(text, Keys.RETURN)

        return self

    def get_company_name(self):
        return self.find(self.locators.COMPANY_NAME).text
