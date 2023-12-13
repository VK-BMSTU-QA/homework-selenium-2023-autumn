from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class BudgetPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/budget\/transactions.*$'

    locators = basic_locators.BudgetPageLocators
