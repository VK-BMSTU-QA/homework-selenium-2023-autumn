from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class HelpStatisticsPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/help\/categories\/statistics.*$'

    locators = basic_locators.HelpStatisticsPageLocators
