import allure

from ui.pages.campaign.campaign_page_interface import CampaignPageInterface
from ui.locators.campaign.create.advertisements_locators import CreateCampaignAdvertisementsPageLocators


class CreateCampaignAdvertisementPage(CampaignPageInterface):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+\/ad\/\d+.*$'

    locators = CreateCampaignAdvertisementsPageLocators

    @allure.step("Creating advertisement via site")
    def create_advertisement_via_site(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, data['short_description'])
        self.fill_image_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_INPUT, data['image_path'])
        self.find(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_PREVIEW_LABEL, timeout=20)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CampaignPageInterface(self.driver)

    @allure.step("Creating advertisement via site empty title")
    def create_advertisement_via_site_empty_title(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, '')
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site long title")
    def create_advertisement_via_site_long_title(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site empty short description")
    def create_advertisement_via_site_empty_short_description(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, '')
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site long short description")
    def create_advertisement_via_site_long_short_description(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, data['short_description'])
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site long long description")
    def create_advertisement_via_site_long_long_description(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, data['short_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SITE_LONG_DESCRIPTION_INPUT, data['long_description'])
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site long button text")
    def create_advertisement_via_site_long_button_text(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, data['short_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SITE_LONG_DESCRIPTION_INPUT, data['long_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_BUTTON_TEXT_INPUT, data['button_text'])
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via site long advertiser")
    def create_advertisement_via_site_long_advertiser(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT, data['short_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_SITE_LONG_DESCRIPTION_INPUT,
                        data['long_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_BUTTON_TEXT_INPUT, data['button_text'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_ADVERTISER_INPUT, data['advertiser'])
        buttons = self.find_list(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON)
        buttons[0].click()

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via community")
    def create_advertisement_via_community(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_INPUT, data['description'])
        self.fill_image_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_INPUT, data['image_path'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_ADVERTISER_INPUT, data['advertiser'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.find(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_PREVIEW_LABEL, timeout=20)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CampaignPageInterface(self.driver)

    @allure.step("Creating advertisement via classmates")
    def create_advertisement_via_classmates(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_INPUT, data['description'])
        self.fill_image_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_INPUT, data['image_path'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_ADVERTISER_INPUT, data['advertiser'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.find(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_PREVIEW_LABEL, timeout=20)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CampaignPageInterface(self.driver)

    @allure.step("Creating advertisement via catalog")
    def create_advertisement_via_catalog(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, data['carousel_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_DESCRIPTION_INPUT, data['long_description'])
        self.fill_image_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_INPUT, data['video_path'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_ADVERTISER_INPUT, data['advertiser'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT, data['banner_description'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CAROUSEL_CARD_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_CAROUSEL_CARD_INPUT, data['carousel_card'])
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CampaignPageInterface(self.driver)

    @allure.step("Creating advertisement via catalog empty title")
    def create_advertisement_via_catalog_empty_title(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, '')
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog long title")
    def create_advertisement_via_catalog_long_title(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog empty carousel description")
    def create_advertisement_via_catalog_empty_carousel_description(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, '')
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog long carousel description")
    def create_advertisement_via_catalog_long_carousel_description(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, data['carousel_description'])
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog empty banner description")
    def create_advertisement_via_catalog_empty_banner_description(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, data['carousel_description'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT, '')
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog long banner description")
    def create_advertisement_via_catalog_long_banner_description(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, data['carousel_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT, data['banner_description'])
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via catalog long long description")
    def create_advertisement_via_catalog_long_long_description(self, data):
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT, data['title'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT, data['carousel_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT, data['banner_description'])
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_DESCRIPTION_INPUT, data['long_description'])
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CreateCampaignAdvertisementPage(self.driver)

    @allure.step("Creating advertisement via vk apps")
    def create_advertisement_via_vk_apps(self, data):
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_INPUT, data['description'])
        self.fill_image_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_INPUT, data['image_path'])
        self.clear_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT)
        self.fill_field(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT, data['title'])
        self.find(self.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_PREVIEW_LABEL, timeout=20)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_BUTTON)

        return CampaignPageInterface(self.driver)
