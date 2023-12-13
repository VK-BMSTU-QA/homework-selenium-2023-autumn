import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CasesPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/cases.*$'

    locators = basic_locators.CasesPageLocators
