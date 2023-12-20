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
        return self

    def catalog_region_click(self):
        self.click(self.locators.CATALOG_REGION)
        return self

    def lead_region_click(self):
        self.click(self.locators.LEAD_FORM_REGION)
        return self

    def continue_click(self):
        self.click(locator=self.locators.CONTINUE_BUTTON)
        return self

    def actions_click(self, element):
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

    def send_keys_site(self, text):
        el = self.find(self.locators.SITE_INPUT)
        self.driver.implicitly_wait(5)
        el.click()
        el.clear()
        el.send_keys(text, Keys.RETURN)
        return self

    def send_cost(self, cost):
        el = self.find(self.locators.COST_INPUT)
        el.clear()
        el.send_keys(cost, Keys.RETURN)
        return self

    def delete_symbols_from_field(self, field_locator, count_delete):
        el = self.find(field_locator)
        el.send_keys(Keys.END)
        for i in range(count_delete):
            el.send_keys(Keys.BACKSPACE)
        return self

    def select_min_cost(self):
        selector = self.find(self.locators.SELECTOR_STRATEGY, 5)
        self.actions_click(selector)

        elements = self.find(self.locators.MIN_STRATEGY)
        self.actions_click(elements)
        return self

    def select_pred_cost(self):
        selector = self.find(self.locators.SELECTOR_STRATEGY, 5)
        self.actions_click(selector)

        elements = self.find(self.locators.PRED_STRATEGY)
        self.actions_click(elements)
        return self

    def send_max_click_cost(self, cost):
        el = self.find(self.locators.MAX_CLICK_COST)
        el.clear()
        el.send_keys(cost, Keys.RETURN)
        return self

    def select_vk_group(self, group):
        self.click(self.locators.RADIO_BUTTON_VK_GROUP)
        self.click(self.locators.GROUP_SELECTOR)
        self.click(self.locators.VK_ANOTHER_GROUP)

        input_group = self.find(self.locators.VK_INPUT_ANOTHER_GROUP)
        input_group.send_keys(group, Keys.RETURN)

        self.click(self.locators.ADD_BUTTON_GROUP)
        return self

    def select_split(self):
        self.click(self.locators.SPLIT_CHECKBOX)
        return self

    def select_lead_click(self, what_lead: int):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@data-testid="lead-form-select"]')
            )
        )

        self.actions_click(element[what_lead])
        return self

    def select_lead_option(self, what_option: int):
        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators.SELECT_LEAD_OPTION)
        )
        self.actions_click(option[what_option])

    def click_date(self):
        el = self.find(self.locators.DATE_PICKER)
        self.actions_click(el)
        return self

    def select_prev_month(self):
        el = self.find(self.locators.DATE_LAST_MONTH_BUTTON)
        self.actions_click(el)
        return self

    def click_first_day(self):
        el = self.find(self.locators.FIRST_DAY)
        self.actions_click(el)
        return self
