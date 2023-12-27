import allure

from selenium.webdriver.common.keys import Keys
from ui.pages.campaign.create.groups_page import CreateCampaignGroupsPage
from ui.pages.campaign.campaign_page_interface import CampaignPageInterface
from ui.locators.campaign.create.settings_locators import CreateCampaignSettingsPageLocators


class CreateCampaignSettingsPage(CampaignPageInterface):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan.*$'

    locators = CreateCampaignSettingsPageLocators

    @allure.step("Create campaign settings via site")
    def create_campaign_settings_via_site(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_BUTTON)
        input = self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_INPUT, data['site'])
        input.send_keys(Keys.ENTER)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.urls_are_equals(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignGroupsPage(self.driver)

    @allure.step("Create campaign settings via site empty url")
    def create_campaign_settings_via_site_empty_url(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via site incorrect url")
    def create_campaign_settings_via_site_incorrect_url(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_BUTTON)
        input = self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_INPUT, data['site'])
        input.send_keys(Keys.ENTER)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via site incorrect budget")
    def create_campaign_settings_via_site_incorrect_budget(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_BUTTON)
        input = self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_SITE_INPUT, data['site'])
        input.send_keys(Keys.ENTER)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via catalog empty url")
    def create_campaign_settings_via_catalog_empty_url(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via catalog incorrect url")
    def create_campaign_settings_via_catalog_incorrect_url(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_BUTTON)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_SITE_INPUT, data['ecomm'])
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via catalog empty catalog")
    def create_campaign_settings_via_catalog_empty_catalog(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_BUTTON)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_SITE_INPUT, data['ecomm'])
        self.click(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignSettingsPage(self.driver)

    @allure.step("Create campaign settings via community")
    def create_campaign_settings_via_community(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_COMMUNITY_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_COMMUNITY_OBJECT_POPUP)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_COMMUNITY_OBJECT_SELECT_POPUP)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.urls_are_equals(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignGroupsPage(self.driver)

    @allure.step("Create campaign settings via classmates")
    def create_campaign_settings_via_classmates(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CLASSMATES_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CLASSMATES_OBJECT_POPUP)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CLASSMATES_OBJECT_SELECT_POPUP)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_CLASSMATES_INPUT, data['odkl'])
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CLASSMATES_ADD_BUTTON)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.urls_are_equals(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignGroupsPage(self.driver)

    @allure.step("Create campaign settings via catalog")
    def create_campaign_settings_via_catalog(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_CIRCLE)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_OBJECT_POPUP)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_OBJECT_SELECT_POPUP)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_INPUT, data['ecomm'])
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_CATALOG_ADD_BUTTON)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.urls_are_equals(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignGroupsPage(self.driver)

    @allure.step("Create campaign settings via vk apps")
    def create_campaign_settings_via_vk_apps(self, data):
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_VK_APPS_BUTTON)
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_VK_APPS_OBJECT_POPUP)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_VK_APPS_INPUT, data['miniapps'])
        self.click(self.locators.CREATE_CAMPAIGN_SETTINGS_VK_APPS_OBJECT_SELECT_POPUP)
        self.fill_field(self.locators.CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT, data['budget'])
        self.urls_are_equals(self.locators.CREATE_CAMPAIGN_CONTINUE_BUTTON)

        return CreateCampaignGroupsPage(self.driver)
