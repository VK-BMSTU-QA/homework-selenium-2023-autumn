from ui.pages.main_page import MainPage
from ui.locators import basic_locators

class InsightsPage(MainPage):
    url = r'https:\/\/ads\.vk\.com\/insights'

    locators = basic_locators.InsightsPageLocators
