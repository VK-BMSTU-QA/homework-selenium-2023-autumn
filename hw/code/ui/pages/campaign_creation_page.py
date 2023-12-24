import time

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

    def go_to_ad_groups(self, domain, budget, name=None):
        if name is not None:
            self.click(self.locators.CAMPAIGN_SECTION_TITLE)
            time.sleep(5)
            self.fill(self.locators.CAMPAIGN_SECTION_TITLE_INPUT, name)

        self.click(self.locators.SITE_OPTION)
        self.fill_site_domain(domain)
        self.fill_budget(budget)
        time.sleep(5)
        self.click(self.locators.CONTINUE_BTN)
        time.sleep(5)

    def go_to_ads(self, domain, budget, region, name=None):
        self.go_to_ad_groups(domain, budget, name)
        self.click(self.locators.region_item(region))
        self.click(self.locators.CONTINUE_BTN)

    def get_selected_regions_count(self):
        return int(self.find_element(self.locators.REGIONS_COUNTER).text.split()[0])

    def fill_ad_title_input(self, title):
        self.fill(self.locators.TITLE_INPUT, title)

    def fill_ad_short_description(self, description):
        self.fill(self.locators.SHORT_DESCRIPTION_INPUT, description)


    def fill_site_link(self, link):
        self.fill(self.locators.SITE_LINK_INPUT, link)

    def fill_ad_info(self, title, link, description):
        self.fill_ad_title_input(title)
        self.fill_site_link(link)
        self.fill_ad_short_description(description)

    def set_logo(self):
        self.click(self.locators.SET_LOGO_BTN)
        self.click(self.locators.LOGO_IMG)

    def set_mediafile(self):
        self.click(self.locators.CHOOSE_MEDIAFILES_BTN)
        self.click(self.locators.LOGO_IMG)
        self.click(self.locators.ADD_MEDIFILES_BTN)

