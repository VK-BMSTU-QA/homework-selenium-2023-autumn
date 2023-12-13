from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpFeaturesPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/features.*$'

    locators = basic_locators.HelpFeaturesPageLocators
