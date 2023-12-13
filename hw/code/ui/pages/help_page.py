import time

from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class HelpPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/help.*$'

    locators = basic_locators.HelpPageLocators

    def open_help_section(self, ind):
        sections = self.find_list(self.locators.HELP_ITEMS_LOCATOR)
        self.scroll_to(sections[ind])
        elem = self.wait(timeout=5).until(EC.element_to_be_clickable(sections[ind]))
        elem.send_keys("\n")
