from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.new_company import NewCompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class NewCompanyPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan"
    locators = NewCompanyPageLocators

    def site_region_click(self):
        self.click(self.locators.SITE_REGION)

    def catalog_region_click(self):
        self.click(self.locators.CATALOG_REGION)

    def lead_region_click(self):
        self.click(self.locators.LEAD_FORM_REGION)

    def continue_click(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def actions_click(self, element):
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def send_keys_site(self, text):
        el = self.find(self.locators.SITE_INPUT)
        self.driver.implicitly_wait(5)
        el.click()
        el.clear()
        el.send_keys(text, Keys.RETURN)

    def send_cost(self, cost):
        el = self.find(self.locators.COST_INPUT)
        el.clear()
        el.send_keys(cost, Keys.RETURN)

    def delete_symbols_from_field(self, field_locator, count_delete):
        el = self.find(field_locator)
        el.send_keys(Keys.END)
        for i in range(count_delete):
            el.send_keys(Keys.BACKSPACE)

    def select_min_cost(self):
        selector = self.find(self.locators.SELECTOR_STRATEGY, 5)
        self.actions_click(selector)

        elements = self.find(self.locators.MIN_STRATEGY)
        self.actions_click(elements)
       

    def select_pred_cost(self):
        selector = self.find(self.locators.SELECTOR_STRATEGY, 5)
        self.actions_click(selector)

        actions = ActionChains(self.driver, 500)
        elements = self.find(self.locators.PRED_STRATEGY)

        actions.move_to_element(elements)
        actions.click(elements)
        actions.perform()

    def send_max_click_cost(self, cost):
        el = self.find(self.locators.MAX_CLICK_COST)
        el.clear()
        el.send_keys(cost, Keys.RETURN)

    def select_vk_group(self, group):
        self.click(self.locators.RADIO_BUTTON_VK_GROUP)
        self.click(self.locators.GROUP_SELECTOR)
        self.click(self.locators.VK_ANOTHER_GROUP)

        print("input group")
        input_group = self.find(self.locators.VK_INPUT_ANOTHER_GROUP)
        input_group.send_keys(group, Keys.RETURN)

        self.click(self.locators.ADD_BUTTON_GROUP)

    def select_split(self):
        self.click(self.locators.SPLIT_CHECKBOX)

    def select_lead_click(self):
        