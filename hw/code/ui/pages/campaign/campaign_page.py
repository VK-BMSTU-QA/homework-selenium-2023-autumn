import time

import allure
from selenium.common.exceptions import TimeoutException

from ui.pages.campaign.campaign_page_interface import CampaignPageInterface
from ui.pages.campaign.create.settings_page import CreateCampaignSettingsPage


class CampaignNotFound(Exception):
    pass


class CampaignPage(CampaignPageInterface):
    @allure.step("Creating campaign via site")
    def create_campaign_via_site(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site(data['advertisement'])

    @allure.step("Creating campaign via community")
    def create_campaign_via_community(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_community(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_community(data['advertisement'])

    @allure.step("Creating campaign via classmates")
    def create_campaign_via_classmates(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_classmates(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_classmates(data['advertisement'])

    @allure.step("Creating campaign via catalog")
    def create_campaign_via_catalog(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog(data['advertisement'])

    @allure.step("Creating campaign via vk apps")
    def create_campaign_via_vk_apps(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_vk_apps(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_vk_apps(data['advertisement'])

    @allure.step("Deleting campaign")
    def delete_campaign(self, name):
        ind, campaigns = self.find_ind_campaign_by_name(name)

        if ind != -1:
            checkboxes = self.find_list(self.locators.CAMPAIGN_LIST_CHECKBOX)
            checkboxes[ind].click()
        else:
            raise CampaignNotFound

        self.click(self.locators.CAMPAIGN_LIST_OPTIONS_POPUP)
        self.select(self.locators.CAMPAIGN_LIST_OPTIONS_SELECT_POPUP, 'archive')
        self.wait_for_remove(campaigns[ind])

    @allure.step("Creating draft via site")
    def create_draft_via_site(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_site(data['settings'])

    @allure.step("Deleting draft")
    def delete_draft(self, name):
        self.click(self.locators.MOVE_TO_MAIN_PAGE_BUTTON)
        self.click(self.locators.CAMPAIGN_DRAFTS_BUTTON)
        ind, campaigns = self.find_ind_campaign_by_name(name)

        if ind != -1:
            checkboxes = self.find_list(self.locators.CAMPAIGN_LIST_CHECKBOX)
            checkboxes[ind].click()
        else:
            raise CampaignNotFound

        self.click(self.locators.CAMPAIGN_DELETE_DRAFT_BUTTON)
        buttons = self.find_list(self.locators.CAMPAIGN_CONFIRM_DELETE_DRAFT_BUTTON)
        buttons[len(buttons) - 1].click()
        self.wait_for_remove(campaigns[ind])

    @allure.step("Creating campaign via site empty url")
    def create_campaign_via_site_empty_url(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_site_empty_url(data)

        return campaign_settings_page

    @allure.step("Creating campaign via site incorrect url")
    def create_campaign_via_site_incorrect_url(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_site_incorrect_url(data['settings'])

        return campaign_settings_page

    @allure.step("Creating campaign via site incorrect budget")
    def create_campaign_via_site_incorrect_budget(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_site_incorrect_budget(data['settings'])

        return campaign_settings_page

    @allure.step("Creating campaign via site incorrect region")
    def create_campaign_via_site_incorrect_region(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        group_page.create_group_via_incorrect_region()

        return group_page

    @allure.step("Creating campaign via site empty title")
    def create_campaign_via_site_empty_title(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_empty_title(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site long title")
    def create_campaign_via_site_long_title(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_long_title(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site empty short description")
    def create_campaign_via_site_empty_short_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_empty_short_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site long short description")
    def create_campaign_via_site_long_short_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_long_short_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site long long description")
    def create_campaign_via_site_long_long_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_long_long_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site long button text")
    def create_campaign_via_site_long_button_text(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_long_button_text(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via site long advertiser")
    def create_campaign_via_site_long_advertiser(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_site(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_site_long_advertiser(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog empty url")
    def create_campaign_via_catalog_empty_url(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_catalog_empty_url(data)

        return campaign_settings_page

    @allure.step("Creating campaign via catalog incorrect url")
    def create_campaign_via_catalog_incorrect_url(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_catalog_incorrect_url(data['settings'])

        return campaign_settings_page

    @allure.step("Creating campaign via catalog empty catalog")
    def create_campaign_via_catalog_empty_catalog(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        campaign_settings_page.create_campaign_settings_via_catalog_empty_catalog(data['settings'])

        return campaign_settings_page

    @allure.step("Creating campaign via catalog empty title")
    def create_campaign_via_catalog_empty_title(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_empty_title(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog long title")
    def create_campaign_via_catalog_long_title(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_long_title(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog empty carousel description")
    def create_campaign_via_catalog_empty_carousel_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_empty_carousel_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog long carousel description")
    def create_campaign_via_catalog_long_carousel_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_long_carousel_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog empty banner description")
    def create_campaign_via_catalog_empty_banner_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_empty_banner_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog long banner description")
    def create_campaign_via_catalog_long_banner_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_long_banner_description(data['advertisement'])

        return advertisement_page

    @allure.step("Creating campaign via catalog long long description")
    def create_campaign_via_catalog_long_long_description(self, data):
        self.click(self.locators.CAMPAIGN_CREATING_BUTTON)
        campaign_settings_page = CreateCampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.create_campaign_settings_via_catalog(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement_via_catalog_long_long_description(data['advertisement'])

        return advertisement_page

    @allure.step("Find campaign index by name")
    def find_ind_campaign_by_name(self, name):
        try:
            campaigns = self.find_list(self.locators.CAMPAIGN_LIST)
        except TimeoutException:
            return -1, []

        for i in range(len(campaigns)):
            if campaigns[i].get_attribute("innerHTML") == name:
                return i, campaigns

        return -1, []
