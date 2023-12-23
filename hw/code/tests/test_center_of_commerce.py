from datetime import datetime, timezone, timedelta
import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.center_of_commerce import CenterOfCommercePage
from tests.base_case import cookies_and_local_storage
from time import gmtime, strftime
import os
from selenium.common.exceptions import TimeoutException

strftime("%Y-%m-%d %H:%M:%S", gmtime())

class TestCenterOfCommerce(BaseCase):
    authorize = True

    # def test_creation_catalog_started(self, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.start_creating_catalog()

    #     assert center_of_commerce_page.find_new_catalog_title() != None

    # @pytest.mark.parametrize("query,result", [("fff", "Товары – fff"), ("19", "Товары – Каталог 2023-12-19")])
    # def test_catalog_search(self, query, result, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.search_catalog(query)
        
    #     assert center_of_commerce_page.find_element_with_text('span', result) != None

    # @pytest.mark.parametrize("title", ["Товары – fff", "Товары – Каталог 2023-12-19"])
    # def test_redirect_to_catalog(self, title, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.go_to_catalog(title)

    #     assert center_of_commerce_page.find_element_with_text('span', 'История загрузок') != None

    # def test_creation_title_name_required_message(self, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.start_creating_catalog()
    #     center_of_commerce_page.clear_catalog_title()
    #     center_of_commerce_page.create_catalog_finish()
        

    #     assert center_of_commerce_page.find_necessary_field_error() != None

    # @pytest.mark.parametrize("tab, element", [("feed", "div"), ("marketplace", "div"), ("manual", "span")])
    # def test_url_field_error_message(self, tab, element, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.start_creating_catalog()
    #     center_of_commerce_page.click_on_tab(tab)
    #     center_of_commerce_page.create_catalog_finish()

    #     assert center_of_commerce_page.find_necessary_field_error(element) != None

    # @pytest.mark.parametrize("tab,url", [("feed", "ddd"), ("marketplace", "dda")])
    # def test_creation_url_field_protocol_message(self, tab, url, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.close_banner()
    #     center_of_commerce_page.start_creating_catalog()
    #     center_of_commerce_page.click_on_tab(tab)
    #     center_of_commerce_page.fill_url_input(url)
    #     center_of_commerce_page.create_catalog_finish()

    #     assert center_of_commerce_page.find_https_error() != None

    # @pytest.mark.parametrize("period, selector_field", [("everyday", "Ежедневно"), ("1 hour", "1 час"), ("4 hours", "4 часа"), ("8 hours", "8 часов")])
    # def test_creation_period_selector(self, period, selector_field, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_feed_catalog()
    #     center_of_commerce_page.set_refresh_period(period)

    #     assert center_of_commerce_page.find_with_text('span', selector_field) != None


    # @pytest.mark.parametrize("url", ["https://vk.com/fa_sales", "https://vk.com/motorprod"])
    # def test_creation_only_with_3andmore_products(self, url, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_feed_catalog()
    #     center_of_commerce_page.fill_url_input(url)

    #     assert center_of_commerce_page.find_not_enough_products_banner() != None 

    # @pytest.mark.parametrize("url", ["https://vk.com/ninoauto"])
    # def test_creation_clear_utm_working(self, url, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_feed_catalog()
    #     center_of_commerce_page.click_on_clear_utm_checkbox()
    #     center_of_commerce_page.fill_url_input(url)
    #     center_of_commerce_page.clear_url_input()

    #     assert center_of_commerce_page.check_clear_utm_checkbox_is_checked() == True

    # def test_hover_on_checkbox_label_working(self, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_feed_catalog()
        
    #     assert 'vkuiTappable--hover-background' in center_of_commerce_page.hover_on_utm_label().get_attribute("class")

    # @pytest.mark.parametrize("url", ["https://vk.com/ninoauto"])
    # def test_creation_marketplace_error_incorrect_url(self, url, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_marketplace_catalog()
    #     center_of_commerce_page.fill_url_input(url)
    #     center_of_commerce_page.create_catalog_finish()
        
    #     assert center_of_commerce_page.find_incorrect_marketplace_url_error() != None

    # @pytest.mark.parametrize("url, href1, href2", [("https://www.wildberries.ru/brands/crocs/all", "https://seller.wildberries.ru/login/", "https://openapi.wildberries.ru"), ("https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208", "https://seller.ozon.ru/app/settings/api-keys", "https://seller-edu.ozon.ru/docs/api-ozon/how-to-api.html"), ("https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X", "https://business.aliexpress.ru/docs/api-token", "https://business.aliexpress.ru/docs/quick-start#heading-shagi-dlya-integratsii-s-lokalnim-api")])
    # def test_creation_marketplace_hrefs_found(self, url, href1, href2, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_marketplace_catalog()
    #     center_of_commerce_page.fill_url_input(url)
        
    #     assert center_of_commerce_page.find_link_with_href(href1) != None and center_of_commerce_page.find_link_with_href(href2) != None
    
    # @pytest.mark.parametrize("url, apikey, placeholder, client_id", [("https://www.wildberries.ru/brands/crocs/all", "eee", "Введите ключ API", ""), ("https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208", "aaa", "Введите ключ API", "aa"), ("https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X", "bbb", "Введите токен для доступа к API", "")])
    # def test_creation_marketplace_hrefs_found(self, url, apikey, placeholder, client_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_marketplace_catalog()
    #     center_of_commerce_page.fill_url_input(url)
    #     center_of_commerce_page.fill_client_id_input(client_id)
    #     center_of_commerce_page.fill_api_key_input(placeholder, apikey)
    #     center_of_commerce_page.create_catalog_finish()
        
    #     assert center_of_commerce_page.find_validation_failed_notification() != None and center_of_commerce_page.find_invalid_apikey_error() != None

    # @pytest.mark.parametrize("url, apikey, placeholder, client_id", [("https://www.wildberries.ru/brands/crocs/all", "ааа", "Введите ключ API", ""), ("https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208", "ььь", "Введите ключ API", "aa"), ("https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X", "ввв", "Введите токен для доступа к API", "")])
    # def test_creation_marketplace_hrefs_found(self, url, apikey, placeholder, client_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_marketplace_catalog()
    #     center_of_commerce_page.fill_url_input(url)
    #     center_of_commerce_page.fill_client_id_input(client_id)
    #     center_of_commerce_page.fill_api_key_input(placeholder, apikey)
    #     center_of_commerce_page.create_catalog_finish()
        
    #     assert center_of_commerce_page.find_validation_failed_notification() != None and center_of_commerce_page.find_invalid_apikey_string_encoding_error() != None

    # @pytest.mark.parametrize("category", ["Авто", "Авиарейсы", "Товары", "Гостиницы", "Недвижимость", "Услуги"])
    # def test_creation_manual_category_selector(self, category, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_manual_catalog()
    #     center_of_commerce_page.set_category(category)

    #     assert center_of_commerce_page.find_category_on_download(category) != None

    # @pytest.mark.parametrize("category, file_path", [("Авто", "tmp/catalog_auto_google.csv"), ("Авиарейсы", "tmp/feed_flight_google.csv"),("Товары", "tmp/catalog_products.csv"), ("Гостиницы", "tmp/hotels_feed_example.csv"), ("Недвижимость", "tmp/catalog_realty.csv"), ("Услуги", "tmp/catalog_services.csv")])
    # def test_creation_manual_category_files_downloading(self, category, file_path, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_manual_catalog()
    #     center_of_commerce_page.set_category(category)

    #     center_of_commerce_page.click_on_category_to_download(category)
    #     timeout = 5

    #     while not os.path.exists(file_path) and timeout > 0:
    #         time.sleep(1)
    #         timeout -= 1

    #     print("Текущая деректория:", os.getcwd())

    #     existence = os.path.exists(file_path)
    #     os.remove(file_path)

    #     assert existence

    # @pytest.mark.parametrize("category, file_path", [("Авто", "mock_files/catalog_auto_google.csv"), ("Авиарейсы", "mock_files/feed_flight_google.csv"),("Товары", "mock_files/catalog_products.csv"), ("Гостиницы", "mock_files/hotels_feed_example.csv"), ("Недвижимость", "mock_files/catalog_realty.csv"), ("Услуги", "mock_files/catalog_services.csv")])
    # def test_manual_creation_files_uploading(self, category, file_path, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
    #     center_of_commerce_page.go_to_create_manual_catalog()
    #     center_of_commerce_page.set_category(category)
    #     center_of_commerce_page.fill_file_input(file_path)

    #     assert center_of_commerce_page.find_downloaded_file() != None


    @pytest.mark.parametrize("tab, second_field", [("feed", "https://vk.com/luxvisage_cosmetics"), ("manual", "mock_files/catalog_products.csv")])
    def test_url_field_error_message(self, tab, second_field, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_create_catalog(tab, second_field)
        center_of_commerce_page.create_catalog_finish()

        assert center_of_commerce_page.find_catalog_tabs() != None