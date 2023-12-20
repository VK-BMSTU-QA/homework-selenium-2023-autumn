import pytest
import time

from tests.base_case import BaseCase, credentials, AllLinks
from tests.base_case import cookies_and_local_storage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ui.pages.group_adv_page import GroupAdvPage


class TestGroup(BaseCase):
    authorize = True

    # def test_region_select(self, group_adv_page: GroupAdvPage):
    #     # HACK remove get page and remove selected
    #     group_adv_page.get_page()

    #     page = group_adv_page
    #     page.site_region_click()

    #     assert page.get_selected_region() != None

    #     group_adv_page.remove_selected_region()

    # def test_upper_limit(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page()
    #     group_adv_page.wait_load_page()
    #     group_adv_page.select_demograpy()

    #     group_adv_page.select_bottom_age(15)
    #     group_adv_page.select_upper_age(14)

    #     assert group_adv_page.get_upper_age() != 14

    # def test_lower_limit(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page()
    #     group_adv_page.wait_load_page()

    #     group_adv_page.select_demograpy()
    #     group_adv_page.select_upper_age(15)
    #     group_adv_page.select_bottom_age(16)

    #     assert group_adv_page.get_lower_age() != 16

    # def test_empty_region(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page()
    #     group_adv_page.wait_load_page()

    #     group_adv_page.click_continue_button()
    #     assert "ошибка" in group_adv_page.driver.page_source

    # def test_key_phrases_error(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page().wait_load_page()

    #     group_adv_page.click_key_phrases().send_key_phrases(
    #         "строка1" * 71
    #     ).click_continue_button()

    #     assert "validation_failed" in group_adv_page.driver.page_source

    # def test_key_phrases_duplicate(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page().wait_load_page()

    #     group_adv_page.click_key_phrases().send_key_phrases(
    #         "строка1"
    #     ).send_keys_phrases_minus("строка1")

    #     assert "У вас дублируются" in group_adv_page.driver.page_source

    # def test_key_devices(self, group_adv_page: GroupAdvPage):
    #     group_adv_page.get_page().wait_load_page()

    #     group_adv_page.click_device_region().remove_device(0).remove_device(1)

    #     assert group_adv_page.is_disabled_and_cheked_device(1)

    def test_url(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_url_region().select_utm().send_text_url(
            "adsabasb"
        ).click_continue_button()

        assert group_adv_page.is_utm_not_correct()
