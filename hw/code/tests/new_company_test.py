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


class TestNewCompany(BaseCase):
    authorize = True

    # def test_min_value_cost(self, new_company_page: NewCompanyPage):
    #     new_company_page.site_region_click()
    #     new_company_page.send_keys_site("ababa.com")

    #     new_company_page.send_cost(22)
    #     new_company_page.continue_click()

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Бюджет кампании должен быть не меньше 100₽")]',
    #             )
    #         )
    #     )
    #     assert (
    #         "Бюджет кампании должен быть не меньше 100₽"
    #         in new_company_page.driver.page_source
    #     )

    # def test_empty_cost(self, new_company_page: NewCompanyPage):
    #     new_company_page.site_region_click()
    #     new_company_page.send_keys_site("ababa.com")

    #     new_company_page.send_cost("")
    #     new_company_page.continue_click()

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Обязательное поле")]',
    #             )
    #         )
    #     )

    #     assert "Обязательное поле" in new_company_page.driver.page_source

    # def test_empty_pred_cost(self, new_company_page: NewCompanyPage):
    #     new_company_page.site_region_click()
    #     new_company_page.send_keys_site("ababa.com")

    #     new_company_page.select_pred_cost()
    #     new_company_page.send_cost(200)
    #     new_company_page.send_max_click_cost("")

    #     new_company_page.continue_click()

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Обязательное поле")]',
    #             )
    #         )
    #     )

    #     assert "Обязательное поле" in new_company_page.driver.page_source

    # def test_empty_catalog(self, new_company_page: NewCompanyPage):
    #     new_company_page.catalog_region_click()
    #     new_company_page.continue_click()

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Обязательное поле")]',
    #             )
    #         )
    #     )
    #     assert "Обязательное поле" in new_company_page.driver.page_source

    # def test_wrong_group(self, new_company_page: NewCompanyPage):
    #     # NOTE maybe const
    #     url_vk = "https://vk.com/sweetmarin"
    #     new_company_page.catalog_region_click()
    #     new_company_page.select_vk_group(url_vk)

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Сообщество не найдено")]',
    #             )
    #         )
    #     )
    #     assert "Сообщество не найдено" in new_company_page.driver.page_source

    def test_select_lead_again(self, new_company_page: NewCompanyPage):
        new_company_page.lead_region_click()
        new_company_page.select_split()

        WebDriverWait(new_company_page.driver, 3).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[contains(text(), "Сообщество не найдено")]',
                )
            )
        )
        assert "Сообщество не найдено" in new_company_page.driver.page_source
