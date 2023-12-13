from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class EventsPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/events.*$'

    locators = basic_locators.EventsPageLocators
