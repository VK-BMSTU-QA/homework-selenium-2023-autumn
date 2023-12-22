from selenium.webdriver.common.by import By

from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class CampaignPage(HqPage):
    CAMPAIGN_TAB = 'campaign'
    ADS_TAB = 'ads'
    GROUPS_TAB = 'groups'
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = basic_locators.CampaignPageLocators

    tabs = {
        CAMPAIGN_TAB: locators.CAMPAIGN_TAB,
        ADS_TAB: locators.ADS_TAB,
        GROUPS_TAB: locators.GROUPS_TAB,
    }
    def close_edu_modal(self):
        try:
            self.click(self.locators.CLOSE_EDU_MODAL_BTN, 15)
        except:
            pass
        try:
            self.click(self.locators.CLOSE_EDU_HINT_BTN, 15)
        except:
            pass
1
    def go_to_tab(self, tab_name):
        locator = self.tabs[tab_name]
        self.click(locator)



