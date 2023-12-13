from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpGeneralPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/general.*$'

    locators = basic_locators.HelpAuthorizationPageLocators
