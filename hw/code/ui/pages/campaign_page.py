import allure_commons
import allure
from ui.pages.base_page import BasePageAuthorized
from ui.locators import basic_locators
from selenium.webdriver import Keys

RETRY_COUNT = 10

class CampaignPage(BasePageAuthorized):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'

    locators = basic_locators.CampaignPageLocators

    def create_campaign(self, settings):
        self.logger.debug("Starting authorization")
        self.click(self.locators.TRIGGER_CREATE_CAMPAIGN_LOCATOR)
        create_campaign_page = NewAdPlanPage(self.driver)
        create_group_page = create_campaign_page.configure_company_settings(settings)
        create_ad_page = create_group_page.configure_group_settings(settings['region'])
        create_ad_page.configure_company_ads(settings)
        return self.find(self.locators.CAMPAIGN_NAME)
        
    
    def close_onboarding(self):
        self.click(self.locators.ONBOARDING)

    def open_settings(self):
        self.click(self.locators.SETTINGS_PAGE_LOCATOR)

class NewAdPlanPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan.*$'

    locators = basic_locators.NewAdPlanPageLocators

    def configure_company_settings(self, settings):
        self.click(self.locators.SITE_LOCATOR)

        input = self.fill_field(self.locators.URL_INPUT_LOCATOR, settings['url'])
        input.send_keys(Keys.ENTER)

        input = self.fill_field(self.locators.BUDGET_INPUT_LOCATOR, settings['budget'])

        cnt = RETRY_COUNT
        while self.is_opened() and cnt > 0:
            self.click(self.locators.NEXT_PAGE)
            cnt -= 1
        
        return NewAdGroupPage(self.driver)

class NewAdPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+\/ad\/\d+.*$'

    locators = basic_locators.NewAdPageLocators

    def configure_company_ads(self, data):
        self.fill_image_field(self.locators.AD_IMAGE_LOCATOR, data['image_path'])
        self.click(self.locators.LOGO_BUTTON_LOCATOR)
        self.click(self.locators.CHOOSE_IMAGE_LOCATOR)
        self.fill_field(self.locators.TITLE_LOCATOR, data['title'])
        self.fill_field(self.locators.SUMMARY_LOCATOR, data['summary']) 

        cnt = RETRY_COUNT
        while self.is_opened() and cnt > 0:
            self.click(self.locators.NEXT_PAGE)
            cnt -= 1

        return CampaignPage(self.driver)
    
class NewAdGroupPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+.*$'

    locators = basic_locators.NewAdGroupPageLocators

    def configure_group_settings(self, region):
        if region == 'Москва':
            self.click(self.locators.REGION_MOSCOW_LOCATOR)
        elif region == 'Санкт-Петербург':
            self.click(self.locators.REGION_PETERSBURG_LOCATOR)
        elif region == 'Россия':
            self.click(self.locators.REGION_RUSSIA_LOCATOR)
        else:
            self.fill_field(self.locators.REGION_INPUT_LOCATOR, region)
            self.click(self.locators.CHECKBOX_LOCATOR)


        self.click(self.locators.NEXT_PAGE)            
        return NewAdPage(self.driver)

