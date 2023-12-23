from datetime import datetime, timezone, timedelta
import pytest
import time
from tests.base_case import BaseCase, credentials, AllLinks
from ui.pages.new_company_page import NewCompanyPage
from tests.base_case import cookies_and_local_storage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime, timedelta


class TestNewCompany(BaseCase):
    authorize = True

    def test_min_value_cost(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click().send_keys_site("ababa.com")
        new_company_page.send_cost(22).continue_click()

        assert new_company_page.is_less_than_hundred()

    def test_empty_cost(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click()
        new_company_page.send_keys_site("ababa.com")

        new_company_page.send_cost("")
        new_company_page.continue_click()

        assert new_company_page.is_must_field()

    def test_empty_pred_cost(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click()
        new_company_page.send_keys_site("ababa.com")

        new_company_page.click_selector_strategy().select_pred_cost()
        new_company_page.send_cost(200)
        new_company_page.send_max_click_cost("")

        new_company_page.continue_click()

        assert new_company_page.is_must_field()

    def test_empty_catalog(self, new_company_page: NewCompanyPage):
        new_company_page.catalog_region_click()
        new_company_page.continue_click()

        assert new_company_page.is_must_field()

    def test_wrong_group(self, new_company_page: NewCompanyPage):
        # TODO alert when try to leave to new page, remove it and generate new tab
        # NOTE maybe const
        url_vk = "https://vk.com/sweetmarin"
        new_company_page.catalog_region_click()
        new_company_page.select_vk_group(url_vk)

        assert new_company_page.is_not_found_community()

    # TODO make fixture to create lead
    # Ask team
    def test_select_lead_again(self, new_company_page: NewCompanyPage):
        # NOTE maybe create lead in setup and then click on it in first selector and check in second
        new_company_page.lead_region_click()
        new_company_page.select_split()

        new_company_page.select_lead_click(0).select_lead_option(0)

        new_company_page.select_lead_click(1)

        assert new_company_page.is_already_selected()

    def test_date_last_not_sooner(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click().send_keys_site("ababa.com")
        new_company_page.click_date().select_prev_month().click_first_day()

        current_date: datetime = datetime.now()

        month_ago_date = current_date - timedelta(days=current_date.day)
        assert new_company_page.is_on_site_text(
            f"01.${month_ago_date.month}.${month_ago_date.year}"
        )
