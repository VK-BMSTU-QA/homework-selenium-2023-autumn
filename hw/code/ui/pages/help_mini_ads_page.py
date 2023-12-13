from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpMiniAdsPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/mini_ads.*$'

    locators = basic_locators.HelpMiniAdsPageLocators
