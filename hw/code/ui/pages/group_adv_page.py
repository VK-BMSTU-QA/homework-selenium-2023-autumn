import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.group_adv import GroupAdvLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class GroupAdvPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan/"
    locators = GroupAdvLocators

    def multiple_find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def site_region_click(self):
        self.click(self.locators.SEARCH_INPUT)
        el = self.find(self.locators.SEARCH_INPUT)
        el.send_keys("Россия", Keys.RETURN)

        self.click(self.locators.REGION_VARIANTS)
        return self

    def remove_selected_region(self):
        self.click(self.locators.SELECTED_RUSSIA)
        return self

    def get_selected_region(self):
        try:
            return self.find(self.locators.SELECTED_RUSSIA)
        except:
            return None

    def get_page(self):
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
        return self

    def action_click(self, element):
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

    def select_demograpy(self):
        self.action_click(self.find(self.locators.DEMOGRAPHY_REGION))
        return self

    def select_bottom_age(self, age: int):
        el = self.multiple_find(self.locators.AGE_FIELD)[0]

        self.action_click(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def select_upper_age(self, age: int):
        el = self.multiple_find(locator=self.locators.AGE_FIELD)[1]
        self.action_click(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def get_upper_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[1]
        return el.get_attribute("value")

    def get_lower_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[0]
        return el.get_attribute("value")

    def click_continue_button(self):
        el = self.multiple_find(self.locators.FOOTER_BUTTONS)[1]
        self.action_click(el)
        return self

    def wait_load_page(self):
        self.multiple_find(self.locators.SAVE_TEXT)[0]

        return self

    def click_key_phrases(self):
        self.action_click(self.find(self.locators.INTEREST_REGION))
        self.action_click(self.find(self.locators.KEY_PHRASES))

        return self

    def send_key_phrases(self, text: str):
        el = self.multiple_find(self.locators.KEY_PHRASE_INPUTS)[0]

        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def send_keys_phrases_minus(self, text):
        el = self.multiple_find(self.locators.KEY_PHRASE_INPUTS)[1]

        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def click_device_region(self):
        self.action_click(self.find(self.locators.DEVICES))
        return self

    def remove_device(self, what_device: int):
        self.action_click(
            self.multiple_find(self.locators.DEVICES_OPTIONS)[what_device]
        )
        return self

    def is_disabled_and_cheked_device(self, what_device: int):
        el = self.multiple_find(self.locators.DEVICES_OPTIONS)[what_device]
        disalbed_att = el.get_attribute("disabled")
        checked_att = el.get_attribute("checked")

        return disalbed_att and checked_att

    def click_url_region(self):
        self.action_click(self.find(self.locators.URL_PARAMETER_REGION))
        return self

    def select_utm(self):
        self.action_click(self.multiple_find(self.locators.URL_OPTIONS)[1])
        return self

    def send_text_url(self, text: str):
        el = self.find(self.locators.URL_INPUT)

        el.clear()
        el.send_keys(text, Keys.RETURN)
        return self

    def is_utm_not_correct(self):
        return "Неверный формат utm-метки" in self.driver.page_source
