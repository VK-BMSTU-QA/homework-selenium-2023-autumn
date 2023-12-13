from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class SitesPage(HqPage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = basic_locators.SitesPageLocators

    def open_add_pixel_modal(self):
        self.click(self.locators.ADD_PIXEL_BTN)