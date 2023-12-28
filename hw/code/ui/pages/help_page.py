from ui.locators.basic_locators import HelpPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class HelpPage(BasePage):
    url = 'https://ads.vk.com/help'
    locators = HelpPageLocators()

    def click_authorize_link(self):
        self.scroll_click(self.locators.AUTHORIZE_LINK)

    def click_how_to_tune_link(self):
        self.scroll_click(self.locators.HOW_TO_TUNE_LINK)

    def click_tools_link(self):
        self.scroll_click(self.locators.TOOLS_LINK)

    def click_statistics_and_finance_link(self):
        self.scroll_click(self.locators.STATISTICS_AND_FINANCE_LINK)

    def click_documents_link(self):
        self.scroll_click(self.locators.DOCUMENTS_LINK)

    def click_simplified_link(self):
        self.scroll_click(self.locators.SIMPLIFIED_LINK)

    def click_faq_link(self):
        self.scroll_click(self.locators.FAQ_LINK)

    def click_partner_cabinet_link(self):
        self.scroll_click(self.locators.PARTNER_CABINET_LINK)

    def fill_search(self, text):
        self.fill_in(self.locators.SEARCH, text)

    def unfocus_search(self):
        search = self.find(self.locators.SEARCH)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(search, -30, -30).click()
        action.perform()

    def get_search_suggestions(self, timeout=5):
        return self.get_element(self.locators.SEARCH_SUGGESTIONS, timeout=timeout)
    
    def wait_until_search_suggestion_disappear(self):
        self.wait_until_element_not_visible(self.locators.SEARCH_SUGGESTIONS)
