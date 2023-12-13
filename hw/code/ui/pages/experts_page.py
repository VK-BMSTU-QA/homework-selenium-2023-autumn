from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class ExpertPage(MainPage):
    url = r'^https:\/\/expert\.vk\.com'

    locators = basic_locators.ExpertPageLocators
