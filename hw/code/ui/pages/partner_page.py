from ui.locators.basic_locators import PartnerPageLocators
from ui.pages.base_page import BasePage

class PartnerPage(BasePage):
    url = 'https://ads.vk.com/partner'
    locators = PartnerPageLocators()

    def click_account(self):
        self.click(self.locators.GO_TO_ACCOUNT)

    def click_help(self):
        self.click(self.locators.HELP)

    def click_site_tab(self):
        self.scroll_click(self.locators.SITE_TAB)

    def click_mobile_tab(self):
        self.scroll_click(self.locators.MOBILE_TAB)

    def get_format(self, format_text):
        return self.find(self.locators.DIV_IN_ACTIVE_TAB_BY_TEXT(format_text))

    def get_submit_btn(self):
        return self.find(self.locators.FORM_SUBMIT_BTN)

    def fill_form(self):
        self.fill_in(self.locators.FORM_NAME_INPUT, 'test name')
        self.fill_in(self.locators.FORM_EMAIL_INPUT, 'test@test.com')

    def submit_form(self):
        self.scroll_click(self.locators.FORM_SUBMIT_BTN)

    def get_submit_msg(self):
        return self.find(self.locators.FORM_SUBMIT_MSG)
