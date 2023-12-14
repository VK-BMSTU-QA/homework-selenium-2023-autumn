from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.login_locators import LKPageLocators, LoginPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LKPage(BasePage):
    url = 'https://ads.vk.com/hq/'
    locators = LKPageLocators

    pass