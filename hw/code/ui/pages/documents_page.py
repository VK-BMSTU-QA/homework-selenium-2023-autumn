from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class DocumentsPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/documents.*$'

    locators = basic_locators.DocumentsPageLocators
