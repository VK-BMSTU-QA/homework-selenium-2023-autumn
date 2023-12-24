from ui.pages.base_page import BasePage
from ui.locators.campaign import basic_locators


class CampaignPageInterface(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/dashboard\/ad_plans.*$'

    locators = basic_locators.CampaignPageLocators
