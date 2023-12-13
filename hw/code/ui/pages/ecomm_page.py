from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class ECommPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/ecomm\/catalogs.*$'

    locators = basic_locators.ECommPageLocators
