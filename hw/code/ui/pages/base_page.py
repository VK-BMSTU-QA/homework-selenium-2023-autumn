import time

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = "https://ads.vk.com/"

    # Open url
    def open(self):
        self.driver.get(self.url)

    def url_cmp(self):
        for i, v in enumerate(self.url):
            if self.url[i] == '*':
                return True
            if self.url[i] != self.driver.current_url[i]:
                return False

    # Check url of opened page and page set in url
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            #if self.url_cmp():
            if self.url == self.driver.current_url:    
                return True
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    # Open url that set in url of page and check if opened
    def __init__(self, driver):
        self.driver = driver
        self.open()
        self.is_opened()

    # wait for timeout. Default timeout 5
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    # Wait timeout to find element by locator
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        print(elem)
        elem.clear()
        elem.send_keys(text)
        return elem

    # Search for element by locator and click on it
    def click(self, locator, timeout=None) -> None:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
