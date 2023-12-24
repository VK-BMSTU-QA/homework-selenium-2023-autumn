from selenium.webdriver.common.by import By
from ui.locators import basic_locators
from ui.pages.hq_page import HqPage

class CampaignCreationPage(HqPage):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'
    locators = basic_locators.CampaignCreationPageLocators

    def get_budget_value(self):
        return self.find_element(self.locators.BUDGET_INPUT).get_attribute('value')

    def fill_site_domain(self, domain):
        self.fill(self.locators.SITE_DOMAIN_INPUT, domain)

    def fill_budget(self, value):
        self.fill(self.locators.BUDGET_INPUT, value)

    def go_to_ad_groups(self, campaign_info):
        self.click(self.locators.SITE_OPTION)
        self.fill_site_domain(campaign_info['domain'])
        self.click(self.locators.CONTINUE_BTN)
        self.fill_budget(campaign_info['budget'])
        attempt = 0
        while not self.url_contains('ad_group') and attempt < 5:
            self.click(self.locators.CONTINUE_BTN)
            attempt += 1

        self.find_element(self.locators.PLACEMENT_SECTION, 10)
        self.find_element(self.locators.CHANGES_SAVING_MSG, 10)

    def click_region(self, region):
        self.click(self.locators.region_item(region))

    def go_to_ads(self, campaign_info):
        self.go_to_ad_groups(campaign_info)
        self.click(self.locators.region_item(campaign_info['region']))
        self.click(self.locators.CONTINUE_BTN)

    def get_selected_regions_count(self):
        return int(self.find_element(self.locators.REGIONS_COUNTER).text.split()[0])

    def fill_ad_title_input(self, title):
        self.fill(self.locators.TITLE_INPUT, title)

    def fill_ad_short_description(self, description):
        self.fill(self.locators.SHORT_DESCRIPTION_INPUT, description)

    def fill_site_link(self, link):
        self.fill(self.locators.SITE_LINK_INPUT, link)

    def fill_ad_info(self, ad_info):
        self.fill_ad_title_input(ad_info['title'])
        self.fill_site_link(ad_info['link'])
        self.fill_ad_short_description(ad_info['description'])

    def set_logo(self):
        self.click(self.locators.SET_LOGO_BTN)
        self.click(self.locators.LOGO_IMG)
        self.find_element(self.locators.LOGO_MEDIA_PREVIEW, 20)

    def set_mediafile(self):
        self.click(self.locators.CHOOSE_MEDIA_FILES_BTN)
        self.click(self.locators.PREVIEW_IMG)
        self.click(self.locators.ADD_MEDIA_FILES_BTN)

    def fill_ad_section(self, ad_info):
        self.click(self.locators.NATIVE_BLOCK_BTN)
        self.fill_ad_info(ad_info)
        self.set_mediafile()
        self.find_element(self.locators.PREVIEW_ITEM, 20)
        self.click(self.locators.PUBLISH_BTN)
        self.click(self.locators.SEND_BTN)

    def delete_campaign(self, name):
        self.click(self.locators.campaign_checkbox(name))
        self.click(self.locators.ACTION_SELECT)
        self.click(self.locators.by_option('Удалить'))

