from ui.pages.base_page import BasePage
from ui.locators.center_of_commerce import CenterOfCommerceLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import os
import time

FEED = 'feed'
MARKETPLACE = 'marketplace'
MANUAL = 'manual'


class CenterOfCommercePage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CenterOfCommerceLocators

    # find methods

    def find_https_error(self, timeout=None):
        return self.find_with_text('div', 'Необходимо указать протокол http(s)', timeout)

    def find_necessary_field_error(self, element = 'div', timeout=None):
        return self.find_with_text(element, 'Обязательное поле', timeout)
    
    def find_incorrect_marketplace_url_error(self, timeout=None):
        return self.find_with_text('div', 'Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе', timeout)

    def find_new_catalog_title(self, timeout=None):
        return self.find_with_text('h2', 'Новый каталог', timeout)
    
    def find_not_enough_products_banner(self, timeout = None) -> WebElement:
        return self.find(self.locators.CATALOG_ERROR_WITH_MINIMUM_THREE_PRODUCTS, timeout)

    def find_clear_utm_checkbox(self, timeout = None) -> WebElement:
        return self.find(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_OFF, timeout)
    
    def find_api_key_input(self, placeholder, timeout = None) -> WebElement:
        return self.find_with_text('input', placeholder, timeout)
    
    def find_element_with_text(self, element, text, timeout=None):
        return self.find_with_text(element, text, timeout)
    
    def find_invalid_apikey_error(self, timeout=None):
        return self.find_with_text('div', 'Указан неверный ключ', timeout)
    
    def find_invalid_apikey_string_encoding_error(self, timeout=None):
        return self.find_with_text('div', 'String is not compatible with encoding', timeout)
    
    def find_category_on_download(self, category, timeout=None):
        return self.find(self.locators.CATALOG_CATEGORY_ON_DOWNLOAD(category), timeout)
    
    def find_file_downloading_error(self, timeout=None):
        return self.find(self.locators.FILE_DOWNLOADING_ERROR_NOTIFICATION, timeout)
    
    def find_downloaded_file(self, timeout=None):
        return self.find(self.locators.DOWNLOADED_FILE, timeout)
    
    def find_catalog_tabs(self, timeout=None):
        return self.find(self.locators.CATALOG_TABS, timeout)
    
    # fill methods

    def fill_url_input(self, url, timeout=None):
        self.fill(self.locators.CATALOG_URL_UNPUT, url, timeout)
    
    def fill_client_id_input(self, client_id, timeout = None) -> WebElement:
        if client_id:
            return self.fill_input_with_placeholder("Введите Client ID", client_id, timeout)

    def fill_api_key_input(self, placeholder, apikey, timeout = None) -> WebElement:
        return self.fill_input_with_placeholder(placeholder, apikey, timeout)
    
    def fill_file_input(self, file_path, timeout = None):
        current_directory = os.getcwd()
        download_directory = os.path.join(current_directory, file_path)
        return self.fill(self.locators.MANUAL_FILE_INPUT, download_directory, timeout)

    # clear methods

    def clear_url_input(self):
        self.clear(self.locators.CATALOG_URL_UNPUT)

    def clear_catalog_title(self, timeout=None):
        self.create_catalog_finish()
        self.clear_with_validation(self.locators.CATALOG_TITLE_INPUT, timeout=timeout)

    def clear_title_input(self, timeout=None):
        self.clear(self.locators.CATALOG_TITLE_UNPUT, timeout)

    # click methods

    def click_on_tab(self, type: str, timeout=None):
        match type:
            case "feed":
                self.click(self.locators.FEED_TAB, timeout)
            case "marketplace":
                self.click(self.locators.MARKET_TAB, timeout)
            case "manual":
                self.click(self.locators.MANUAL_TAB, timeout)

    def click_on_clear_utm_checkbox(self, timeout = None):
        if self.is_checkbox_checked(self.locators.CATALOG_CLEAR_UTM_CHECKBOX, timeout):
            self.click(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_ON, timeout)
        else:
            self.click(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_OFF, timeout)

    def click_on_category_to_download(self, category, timeout=None):
        return self.click(self.locators.CATALOG_CATEGORY_ON_DOWNLOAD(category), timeout)

    # custom methods
    def start_creating_catalog(self, timeout=None):
        self.click(self.locators.START_CREATING_CATALOG, timeout=timeout)

    def go_to_create_feed_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(FEED, timeout)

    def go_to_create_marketplace_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(MARKETPLACE, timeout)

    def go_to_create_manual_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(MANUAL, timeout)

    def go_to_create_catalog(self, tab, second_field, timeout=None):
        match tab:
            case "feed":
                self.go_to_create_feed_catalog(timeout)
                self.fill_url_input(second_field)
                time.sleep(2)
            case "marketplace":
                self.go_to_create_marketplace_catalog(timeout)
                self.fill_url_input(second_field)
            case "manual":
                self.go_to_create_manual_catalog(timeout)
                self.fill_file_input(second_field)


    def search_catalog(self, query):
        self.search(self.locators.SEARCH_CATALOG_FIELD, query)

    def go_to_catalog(self, title, timeout = None):
        self.click_element_with_text('span', title, timeout)

    def set_refresh_period(self, period: str, timeout = None):
        self.click(self.locators.CATALOG_SELECT_TITLE)
        match period:
            case "everyday":
                self.click(self.locators.CATALOG_PERIOD_EVERYDAY, timeout)
            case "1 hour":
                self.click(self.locators.CATALOG_PERIOD_EVERYHOUR, timeout)
            case "4 hours":
                self.click(self.locators.CATALOG_PERIOD_EVERY4HOURS, timeout)
            case "8 hours":
                self.click(self.locators.CATALOG_PERIOD_EVERY8HOURS, timeout)
    
    def set_category(self, category: str, timeout = None):
        self.click(self.locators.CATALOG_SELECT_TITLE)
        if category != "Товары":
            self.click(self.locators.CATALOG_CATEGORY(category), timeout)

    def create_catalog_finish(self, timeout=None):
        self.click(self.locators.CATALOG_CREATE_BUTTON, timeout=timeout)
    
    def check_clear_utm_checkbox_is_checked(self, timeout = None) -> bool:
        return self.is_checkbox_checked(self.locators.CATALOG_CLEAR_UTM_CHECKBOX, timeout)
    
    def hover_on_utm_label(self, timeout = None) -> WebElement:
        return self.hover_on_element(self.locators.CATALOG_CHECKBOX_UTM_LABEL, timeout)
