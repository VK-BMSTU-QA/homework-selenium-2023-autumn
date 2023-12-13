import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class NewsPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/news.*$'

    locators = basic_locators.NewsPageLocators
