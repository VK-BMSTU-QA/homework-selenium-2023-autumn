import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class ForumPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/upvote.*$'

    locators = basic_locators.ForumPageLocators
