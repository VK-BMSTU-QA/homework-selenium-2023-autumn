import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import allure

from ui.pages.campaign.campaign_page_interface import CampaignPageInterface
from ui.locators.campaign.create.groups_locators import CreateCampaignGroupsPageLocators
from ui.pages.campaign.create.advertisements_page import CreateCampaignAdvertisementPage


class CreateCampaignGroupsPage(CampaignPageInterface):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+.*$'

    locators = CreateCampaignGroupsPageLocators

    @allure.step("Creating group")
    def create_group(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_GROUPS_SEARCH_INPUT, data['search'])
        checkbox_locator = (
            self.locators.CREATE_CAMPAIGN_GROUPS_SEARCH_CHECKBOX[0],
            self.locators.CREATE_CAMPAIGN_GROUPS_SEARCH_CHECKBOX[1].format(data['region']),
        )
        self.click(checkbox_locator)
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating via incorrect region")
    def create_group_via_incorrect_region(self):
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_GROUPS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignGroupsPage(self.driver)