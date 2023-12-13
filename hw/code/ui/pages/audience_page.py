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

    def create_audience(self, src_text, keywords, title=None, keywords_title=None, neg_keywords=None):
        self.click(self.locators.CREATE_AUDIENCE_BTN)
        if title is not None:
            self.fill(self.locators.AUDIENCE_TITLE_INPUT, title)
        self.click(self.locators.ADD_SRC_BTN)
        self.click(self.locators.src_by_text(src_text))

        if keywords_title is not None:
            self.fill(self.locators.KEYWORDS_TITLE_INPUT, keywords_title)
        self.fill(self.locators.KEYWORDS_INPUT, keywords)
        if neg_keywords is not None:
            self.fill(self.locators.NEG_KEYWORDS_INPUT, neg_keywords)
        self.click(self.locators.KEYWORDS_SAVE_BTN)
        modals = self.find_elements(self.locators.MODAL_WINDOW)
        self.is_invisible(modals[-1])

        self.click(self.locators.SAVE_AUDIENCE_BTN)
        self.is_invisible(self.locators.MODAL_WINDOW)

    def delete_audience(self, audience_name):
        detail_btns = self.find_elements(self.locators.audience_details_btn_by_name(audience_name))
        detail_btn = detail_btns[0]
        self.hover_and_click(detail_btn)
        options = self.find_elements(self.locators.AUDIENCE_OPTION)
        self.click_by_elem(options[-1])
        self.click(self.locators.CONFIRM_DELETE_BTN)
        self.is_invisible(detail_btn)
