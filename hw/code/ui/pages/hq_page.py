from ui.pages.base_page import BasePage
from ui.locators.basic_locators import HqPageLocators


class HqPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = HqPageLocators
