from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpAuthorizationPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/authorization.*$'

    locators = basic_locators.HelpAuthorizationPageLocators
