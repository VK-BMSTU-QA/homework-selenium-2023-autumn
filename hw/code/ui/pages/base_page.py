import re
import time
import allure

from ui.locators import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

CLICK_RETRY = 3


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    url = r'^https:\/\/ads\.vk\.com\/$'
    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=30):
        started = time.time()
        while time.time() - started < timeout:
            if self.urls_are_equal():
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None, obj=None):
        if obj is None:
            obj = self.driver

        if timeout is None:
            timeout = 10
        return WebDriverWait(obj, timeout=timeout)

    def wait_for_openning(self, url, timeout=30):
        return self.wait(timeout).until(EC.url_to_be(url))

    def has_object(self, locator):
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False

    def fill_field(self, locator, string):
        field = self.click(locator)
        field.clear()
        field.send_keys(string)
        return field

    def fill_image_field(self, locator, path):
        field = self.find(locator)
        field.send_keys(path)

    def wait_for_remove(self, obj, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element(obj))

    def find_list(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def find(self, locator, timeout=None, obj=None):
        return self.wait(timeout=timeout, obj=obj).until(EC.presence_of_element_located(locator))

    def clear_field(self, locator, timeout=30, obj=None):
        input = self.find(locator)
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.BACKSPACE)

    def select(self, locator, value):
        select_element = self.find(locator)
        self.driver.execute_script("arguments[0].style.display = 'block';", select_element)
        select_element = self.find(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def urls_are_equal(self):
        return re.match(self.url, self.driver.current_url)

    def urls_are_equals(self, locator):
        attempt = 1
        while self.urls_are_equal():
            self.click(locator)

            if attempt == 5:
                break

            attempt += 1

    @classmethod
    def convert_regexp_url(cls):
        return cls.url[1:-3].replace('\\', '')

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=30, obj=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout, obj=obj)
                elem = self.wait(timeout=timeout, obj=obj).until(EC.element_to_be_clickable(locator))
                elem.click()
                return elem
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def wait_for_scroll(self, elem, timeout=None):
        return self.wait(timeout, obj=elem).until(EC.visibility_of(elem))

    def scroll_to(self, item):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
        self.wait_for_scroll(item, timeout=30)

    @allure.step('Hovering and clicking on {locator}')
    def hover_and_click(self, locator, timeout=30, obj=None):
        a = ActionChains(self.driver)
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout, obj=obj)
                a.move_to_element(elem).click().perform()
                return elem
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def scroll_down(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        a = ActionChains(self.driver)
        a.scroll_by_amount(0, page_height).perform()

    def focus(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def find_elements_by_xpath(self, locator, timeout=5):
        return self.driver.find_elements_by_xpath(locator)

    @allure.step("Find element by locator")
    def find_elem_by_locator(self, locator):
        try:
            self.find(locator)
        except TimeoutException:
            return False

        return True

    @allure.step("Find long field label")
    def find_long_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL)

    @allure.step("Find empty url field label")
    def find_empty_url_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_SETTINGS_EMPTY_URL_LABEL)

    @allure.step("Find incorrect url field label")
    def find_incorrect_url_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_URL_LABEL)

    @allure.step("Find incorrect budget field label")
    def find_incorrect_budget_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_BUDGET_LABEL)

    @allure.step("Find incorrect region field label")
    def find_incorrect_region_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_REGION_LABEL)

    @allure.step("Find required field label")
    def find_required_field_label(self):
        return self.find_elem_by_locator(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL)
