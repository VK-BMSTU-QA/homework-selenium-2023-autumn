from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class SitesPage(HqPage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = basic_locators.SitesPageLocators

    def open_add_pixel_modal(self):
        self.click(self.locators.OPEN_PIXEL_MODAL_BTN)

    def click_site_domain_option(self):
        self.click(self.locators.SITE_DOMAIN_OPTION)

    def click_pixel_id_option(self):
        self.click(self.locators.PIXEL_ID_OPTION)

    def fill_site_domain(self, domain):
        self.fill(self.locators.SITE_DOMAIN_INPUT, domain)

    def fill_pixel_id(self, id):
        self.fill(self.locators.PIXEL_ID_INPUT, id)

    def fill_owner_email(self, email):
        self.fill(self.locators.OWNER_EMAIL_INPUT, email)

    def open_more_ctx_menu(self, domain):
        self.hover_and_click(self.find_element(self.locators.pixel_more_btn(domain)))

    def fill_pixel_name(self, name):
        self.fill(self.locators.RENAME_MODAL_NAME_INPUT, name)