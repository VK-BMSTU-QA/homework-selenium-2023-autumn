from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class LeadAdsPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/leadads\/leadforms.*$'

    locators = basic_locators.LeadAdsPageLocators
