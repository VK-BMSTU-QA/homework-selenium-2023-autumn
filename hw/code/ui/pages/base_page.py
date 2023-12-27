import time

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    basic_locators = basic.BasePageLocators()
    url = "https://ads.vk.com/"

    # Open url
    def open(self):
        self.driver.get(self.url)

    def url_cmp(self):
        driver_url = self.driver.current_url
        for i, v in enumerate(self.url):
            if self.url[i] == '*':
                return True
            if self.url[i] != driver_url[i]:
                return False

    # Check url of opened page and page set in url
    def is_opened(self, timeout=15):
        time.sleep(5)
        '''started = time.time()
        while time.time() - started < timeout:

            # TODO
            if self.url_cmp():
            # if self.url == self.driver.current_url:    
                return True
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )'''

    def close_cookie_banner(self):
        try:
            self.click(self.basic_locators.COOKIE_BANNER_BUTTON)
        except Exception as e:
            print(e)
            pass

    def close_banner(self):
        try:
            self.click(self.basic_locators.BANNER_BUTTON)
        except Exception as e:
            print(e)
            pass

    # Open url that set in url of page and check if opened
    def __init__(self, driver):
        self.driver = driver
        self.open()
        # self.is_opened()

    # wait for timeout. Default timeout 5
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    # Wait timeout to find element by locator
    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def find_with_text(self, element, text, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.ELEMENT_WITH_TEXT(element, text)))
    
    def click_element_with_text(self, element, text, timeout=None) -> WebElement:
        element = self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.ELEMENT_WITH_TEXT(element, text)))
        element.click()

    def find_with_text_and_class(self, element, text, class_name, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(element, text, class_name)))
    
    def click_element_with_text_and_class(self, element, text, class_name, timeout=None) -> WebElement:
        element = self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(element, text, class_name)))
        element.click()
    
    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem.clear()
        elem.send_keys(text)
        return elem
    
    def fill_input_with_placeholder(self, placeholder, text, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.INPUT_WITH_PLACEHOLDER(placeholder)))
        elem.clear()
        elem.send_keys(text)
        return elem
    
    def clear(self, locator, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        print(elem)
        elem.clear()
        return elem
    
    def clear_with_validation(self, locator, timeout=None):
        elem = self.find(locator, timeout=timeout)
        self.click(locator, timeout=timeout)
        elem.send_keys(Keys.END + Keys.SHIFT + Keys.HOME)
        time.sleep(3)
        elem.send_keys(Keys.BACKSPACE)
    
    def search(self, search_locator, query, timeout = None):
        elem = self.find(search_locator, timeout)
        elem.send_keys(query)

    # Search for element by locator and click on it
    def click(self, locator, timeout=None) -> None:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def is_checkbox_checked(self, locator, timeout=None) -> bool:
        checkbox = self.find(locator, timeout)
        return self.driver.execute_script("return arguments[0].checked", checkbox)
    
    def hover_on_element(self, locator, timeout=None) -> WebElement:
        element_to_hover = self.find(locator, timeout)
        hover = ActionChains(self.driver).move_to_element(element_to_hover)
        hover.perform()
        return element_to_hover
    
    def find_link_with_href(self, href, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.LINK_WITH_HREF(href)))
    
    def find_validation_failed_notification(self, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(self.basic_locators.VALIDATION_FAILED_NOTIFICATION))
    
