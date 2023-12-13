from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpDocumentsPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/documents.*$'

    locators = basic_locators.HelpDocumentsPageLocators
