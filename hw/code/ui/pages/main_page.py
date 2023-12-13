import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage, NoNavbarSection
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import FooterSection


class MainPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/$'

    locators = basic_locators.MainPageLocators
    navbar = {
        'logo': locators.LOGO_LOCATOR,
        'news': locators.NEWS_LOCATOR,
        'cases': locators.CASES_LOCATOR,
        'ideas_forum': locators.FORUM_LOCATOR,
        'monetization': locators.MONETIZATION_LOCATOR,
        'help': locators.HELP_LOCATOR,
        'cabinet': locators.CABINET_LOCATOR,
    }

    footer = {
        'cabinet': locators.FOOTER_BUTTON_CABINET,
        'business': locators.FOOTER_LOGO_VK_BUSINESS,
        'about': locators.FOOTER_ABOUT,
        'sections': locators.FOOTER_ITEMS,
    }

    def accept_cookie(self):
        self.click(self.locators.ACCEPT_COOKIE_LOCATOR)

    def find_items(self, section_name):
        return self.find_list(self.footer.get(section_name, None))

    def move_to_footer(self, section_name):
        locator = self.footer.get(section_name, None)

        if locator is not None:
            self.click(locator)
            handlen_len = len(self.driver.windows_handles)
            if handlen_len > 1:
                self.driver.switch_to.window(self.driver.windew_handlew[-1])
        else:
            raise FooterSection

    def move_to(self, section_name):
        locator = self.navbar.get(section_name, None)

        if locator is not None:
            self.click(locator)
            handles_len = len(self.driver.window_handles)
            if handles_len > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
        else:
            raise NoNavbarSection

    def open_footer_section(self, ind):
        self.scroll_down()
        sections = self.find_list(self.locators.FOOTER_ITEM_LOCATOR)
        self.wait(timeout=5).until(EC.element_to_be_clickable(sections[ind]))
        sections[ind].click()
        handles_len = len(self.driver.window_handles)
        if handles_len > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
