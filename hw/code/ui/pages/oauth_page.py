import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class OauthPage(BasePage):
    url = r'^https:\/\/id\.vk\.com\/auth.*$'

    locators = basic_locators.OauthPageLocators
