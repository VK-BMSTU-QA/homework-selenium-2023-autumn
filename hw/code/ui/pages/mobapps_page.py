from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class MobAppsPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/apps.*$'

    locators = basic_locators.MobAppsPageLocators
