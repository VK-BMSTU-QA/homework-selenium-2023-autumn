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


class TestCenterOfCommerceCatalog(BaseCase):
    authorize = True

    @pytest.mark.parametrize("tab, second_field", [("feed", "https://vk.com/luxvisage_cosmetics"), ("manual", "mock_files/catalog_products.csv")])
    def test_catalog_creation_works(self, tab, second_field, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_create_catalog(tab, second_field)
        center_of_commerce_page.create_catalog_finish()

        assert center_of_commerce_page.find_catalog_tabs() is not None

    @pytest.mark.parametrize("from_what, to", [("Товары – fff", "Товары – dddsdsd"), ("Тачки", "Товары – fff")])
    def test_catalog_category_switch_works(self, from_what, to, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(from_what)
        center_of_commerce_page.switch_catalog(to)

        assert center_of_commerce_page.find_catalog_title(to) is not None

    @pytest.mark.parametrize("catalog, tab, tab_id", [("Тачки", "Товары", "tab_catalogs.catalogMain"), ("Тачки", "Группы", "tab_catalogs.catalogMain.catalogGroups"), ("Тачки", "Диагностика", "tab_catalogs.catalogMain.catalogDiagnostics"), ("Тачки", "События", "tab_catalogs.catalogMain.catalogEvents"), ("Тачки", "История загрузок", "tab_catalogs.catalogMain.catalogHistory"), ("Товары – fff", "История загрузок", "tab_catalogs.catalogMain.catalogHistory"), ("Товары – fff", "Диагностика", "tab_catalogs.catalogMain.catalogDiagnostics"), ("Товары – fff", "События", "tab_catalogs.catalogMain.catalogEvents")])
    def test_catalog_category_tabs_redirecting(self, catalog, tab, tab_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.switch_catalog_tab(tab_id)

        assert center_of_commerce_page.check_catalog_tab_switched(tab) is not None

    @pytest.mark.parametrize("catalog, tab_id", [("Тачки", "tab_catalogs.catalogMain"), ("Товары – fff", "tab_catalogs.catalogMain")])
    def test_catalog_products_promote_works(self, catalog, tab_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.switch_catalog_tab(tab_id)
        center_of_commerce_page.click_on_promote_button()

        assert center_of_commerce_page.find_promote_title() is not None

    @pytest.mark.parametrize("catalog, id, title", [("Товары – fff", "8005304", "Тени для век Glam Look матовые, палетка"), ("Товары – fff", "8008361", "Лак для ногтей GEL SHINE перламутровый")])
    def test_catalog_products_search(self, catalog, id, title, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.search_product(id)

        assert center_of_commerce_page.find_product_by_title(title) is not None

    @pytest.mark.parametrize("catalog", ["Товары – fff", "Тачки"])
    def test_catalog_products_table_settings_widget(self, catalog, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.click_product_table_settings()

        assert center_of_commerce_page.find_table_settings_title() is not None

    @pytest.mark.parametrize("catalog, product, product_id", [("Товары – fff", "Подарочный набор декоративной косметики Beauty Box №6", "8699561"), ("Товары – fff", "Жидкость для снятия лака без ацетона с витамином F", "8013293")])
    def test_catalog_product_widget(self, catalog, product, product_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.go_to_catalog_product(product_id, product)

        assert center_of_commerce_page.find_h2_with_text(product) is not None

    @pytest.mark.parametrize("catalog, product, product_id", [("Товары – fff", "Подарочный набор декоративной косметики Beauty Box №6", "8699561"), ("Товары – fff", "Жидкость для снятия лака без ацетона с витамином F", "8013293")])
    def test_catalog_product_vklink(self, catalog, product, product_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.go_to_catalog_product(product_id, product)

        assert center_of_commerce_page.check_vk_product_found(product)

    @pytest.mark.parametrize("catalog, product_id", [("Товары – fff", "8002726")])
    def test_catalog_product_sort(self, catalog, product_id, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.click_on_sort_products()

        assert center_of_commerce_page.find_product_by_id(product_id) is not None

    @pytest.mark.parametrize("catalog, redirected_tab", [("Товары – fff", "Диагностика")])
    def test_catalog_warning_button(self, catalog, redirected_tab, center_of_commerce_page: CenterOfCommercePage, cookies_and_local_storage):
        center_of_commerce_page.go_to_catalog(catalog)
        center_of_commerce_page.click_on_warning_button()

        assert center_of_commerce_page.check_catalog_tab_switched(redirected_tab)
