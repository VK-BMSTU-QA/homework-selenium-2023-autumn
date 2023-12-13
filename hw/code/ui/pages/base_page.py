import time
from typing import List

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY = 3


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        if not self.check_url(self.url, timeout):
            raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find_element(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=None) -> List[WebElement]:
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        for i in range(CLICK_RETRY):
            try:
                self.find_element(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return elem
            except:
                if i == CLICK_RETRY - 1:
                    raise

    def click_by_elem(self, elem, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(elem))
        elem.click()
        return elem

    def hover_and_click(self, elem) -> WebElement:
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).click().perform()
        return elem

    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.click(locator, timeout=timeout)
        elem.clear()
        elem.send_keys(text)
        return elem

    def is_visible(self, locator, timeout=None):
        self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def is_invisible(self, locator, timeout=None):
        self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def is_disabled(self, locator, timeout=None):
        self.wait(timeout).until(EC.element_attribute_to_include(locator, 'disabled'))

    def is_selected(self, locator, state=True, timeout=None):
        self.wait(timeout).until(EC.element_located_selection_state_to_be(locator, state))

    def check_url(self, url_for_match, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            idx = self.driver.current_url.find('?')
            url = self.driver.current_url[:idx if idx != -1 else len(self.driver.current_url)]
            if url == url_for_match:
                return True
        return False


    def go_to_cabinet(self):
        self.click(self.locators.GO_TO_CABINET_BTN)
