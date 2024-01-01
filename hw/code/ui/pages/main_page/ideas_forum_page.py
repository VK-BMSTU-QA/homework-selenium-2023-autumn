from ui.pages.base_page import BasePage
from ui.locators.main import MainPageLocators


class IdeasForumPage(BasePage):
    url = "https://ads.vk.com/upvote"
    locators = MainPageLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.is_opened()
