from ui.pages.base_page import BasePage
from ui.locators.basic_locators import HqPageLocators


class HqPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = HqPageLocators

    def close_edu_modal(self):
        try:
            self.click(self.locators.CLOSE_EDU_MODAL_BTN)
            self.click(self.locators.CLOSE_EDU_HINT_BTN)
        except:
            pass

