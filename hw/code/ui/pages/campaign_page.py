import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage, BasePageAuthorized
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class CampaignNotFound(Exception):
    pass


class CampaignPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/dashboard\/ad_plans.*$'

    locators = basic_locators.CampaignPageLocators
    sections = {
        'campaigns': locators.CAMPAIGNS_SECTION_LOCATOR,
        'groups': locators.GROUPS_SECTION_LOCATOR,
        'ads': locators.ADS_SECTION_LOCATOR,
    }

    def close_onboarding(self):
        self.logger.debug("checking exists onboarding screen")

        if self.has_object(self.locators.ONBOARDING_LOCATOR):
            self.logger.debug("onboarding screen is exists")

            with allure.step("closing onboarding screen"):
                self.click(self.locators.ONBOARDING_CLOSE_LOCATOR)
        else:
            self.logger.debug("help screen don't exists")

        if self.has_object(self.locators.HELP_LOCATOR):
            self.logger.debug("help screen is exists")

            with allure.step("closing help screen"):
                self.click(self.locators.HELP_CLOSE_LOCATOR)
        else:
            self.logger.debug("onboarding screen don't exists")

    @allure.step("Creating campaign")
    def create_campaign(self, data):
        self.click(self.locators.START_CREATING_CAMPAIGN)
        campaign_settings_page = CampaignSettingsPage(self.driver)
        group_page = campaign_settings_page.set_campaign_settings(data['settings'])
        advertisement_page = group_page.create_group(data['group'])
        advertisement_page.create_advertisement(data['advertisement'])

    def find_ind_campaign_by_name(self, name):
        try:
            campaigns = self.find_list(self.locators.CAMPAIGN_LOCATOR)
        except TimeoutException:
            return -1, []

        for i in range(len(campaigns)):
            if campaigns[i].get_attribute("innerHTML") == name:
                return i, campaigns
        
        return -1, []
    
    @allure.step("Deleting campaign")
    def delete_campaign(self, name):
        ind, campaigns = self.find_ind_campaign_by_name(name)

        if ind != -1:
            checkboxes = self.find_list(self.locators.CHECHBOX_CAMPAIGN_LOCATOR)
            checkboxes[ind].click()
        else:
            raise CampaignNotFound
        
        self.click(self.locators.OPTIONS_LOCATOR)
        self.select(self.locators.SELECT_OPTIONS_LOCATOR, 'archive')
        self.wait_for_remove(campaigns[ind])

    @allure.step("Opening section {section_name}")
    def open_section(self, section_name):
        super().move_to(section_name, sections=self.sections)


class CampaignSettingsPage(CampaignPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan.*$'

    locators = basic_locators.CampaignSettingsPageLocators

    @allure.step("Setting campaign settings")
    def set_campaign_settings(self, data):
        self.click(self.locators.SITE_LOCATOR)

        site_modal = self.find(self.locators.SITE_MODAL_LOCATOR)
        input = self.click(self.locators.SITE_FIELD_LOCATOR, obj=site_modal)
        input.send_keys(data['site'])
        input.send_keys(Keys.ENTER)

        input = self.fill_field(self.locators.BUDGET_FIELD_LOCATOR, data['budget'])

        attempt = 1
        while self.urls_are_equal():
            self.click(self.locators.CONTINUE_LOCATOR)

            if attempt == 5:
                break
            
            attempt += 1

        return AddGroupPage(self.driver)
    

class GroupPage(CampaignPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/dashboard\/ad_groups.*$'

    locators = basic_locators.GroupPageLocators


class AddGroupPage(GroupPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+.*$'

    locators = basic_locators.AddGroupPageLocators

    @allure.step("Creating group")
    def create_group(self, data):
        self.fill_field(self.locators.SEARCH_LOCATOR, data['search'])
        checkbox_locator = (self.locators.CHECKBOX_LOCATOR[0], self.locators.CHECKBOX_LOCATOR[1].format(data['region']))
        self.click(checkbox_locator)
        self.click(self.locators.CONTINUE_LOCATOR)
    
        return AddAdvertisementPage(self.driver)


class AdvertisementPage(CampaignPage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/dashboard\/ads.*$'

    locators = basic_locators.AdvertisementPageLocators


class AddAdvertisementPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+\/ad\/\d+.*$'

    locators = basic_locators.AddAdvertisementPageLocators

    @allure.step("Creating advertisement")
    def create_advertisement(self, data):
        self.fill_field(self.locators.TITLE_LOCATOR, data['title'])
        self.fill_field(self.locators.SHORT_DESCRIPTION_LOCATOR, data['short_description'])
        self.fill_image_field(self.locators.IMAGE_INPUT_LOCATOR, data['image_path'])
        self.find(self.locators.PREVIEW_LOCATOR, timeout=20)
        self.click(self.locators.SUBMIT_LOCATOR)

        return CampaignPage(self.driver)
