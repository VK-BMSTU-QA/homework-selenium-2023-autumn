import logging
import time

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from ui.locators import basic_locators

CLICK_RETRY = 3


class PageNotOpenedExeption(Exception):
    pass


class NoNavbarSection:
    pass


class BasePage(object):
    url = r'^https:\/\/ads\.vk\.com\/$'
    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.urls_are_equal():
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None, obj=None):
        if obj is None:
            obj = self.driver

        if timeout is None:
            timeout = 5
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

    def select(self, locator, value):
        select_element = self.find(locator)
        self.driver.execute_script("arguments[0].style.display = 'block';", select_element)
        select_element = self.find(locator)
        select = Select(select_element)
        select.select_by_value(value)

    def urls_are_equal(self):
        return re.match(self.url, self.driver.current_url)

    @classmethod
    def convert_regexp_url(cls):
        return cls.url[1:-3].replace('\\', '')

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=5, obj=None):
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
        self.wait_for_scroll(item, timeout=5)

    @allure.step('Hovering and clicking on {locator}')
    def hover_and_click(self, locator, timeout=5, obj=None):
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


class NoNavbarSection(Exception):
    pass


class FooterSection:
    pass


class BasePageAuthorized(BasePage):
    url = None
    locators = basic_locators.BasePageAuthorizedLocators
    navbar = {
        'campaigns': locators.CAMPAIGN_LOCATOR,
        'audience': locators.AUDIENCE_LOCATOR,
        'budget': locators.BUDGET_LOCATOR,
        'ecomm': locators.ECOMM_LOCATOR,
        'sites': locators.SITE_LOCATOR,
        'mobapps': locators.MOBAPP_LOCATOR,
        'leadads': locators.LEADAD_LOCATOR,
        'settings': locators.SETTINGS_LOCATOR
    }

    def move_to(self, section_name, sections=navbar):
        locator = sections.get(section_name, None)

        if locator is not None:
            self.click(locator)
        else:
            raise NoNavbarSection
