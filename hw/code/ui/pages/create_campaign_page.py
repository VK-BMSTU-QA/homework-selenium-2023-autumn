from ui.pages.base_page import BasePageAuthorized
from ui.locators import basic_locators

class CreateCampaignPage(BasePageAuthorized):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'

    locators = basic_locators.CampaignPageLocators