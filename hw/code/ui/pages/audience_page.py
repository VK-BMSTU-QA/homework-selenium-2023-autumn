from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class AudiencePage(HqPage):
    AUDIENCE_TAB = 'audience'
    USERS_TAB = 'users'

    url = 'https://ads.vk.com/hq/audience'
    locators = basic_locators.AudiencePageLocators

    tabs = {
        AUDIENCE_TAB: locators.AUDIENCE_TAB,
        USERS_TAB: locators.USERS_TAB,
    }

    def go_to_tab(self, tab_name):
        locator = self.tabs[tab_name]
        self.click(locator)
