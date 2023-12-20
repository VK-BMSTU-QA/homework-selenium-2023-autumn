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
    #     # TODO alert when try to leave to new page, remove it and generate new tab
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
    #     # assert "Сообщество не найдено" in new_company_page.driver.page_source

    #     # HACK
    #     new_company_page.driver.get("https://ads.vk.com/cases")
    #     WebDriverWait(new_company_page.driver, 5).until(EC.alert_is_present())

    #     alert = new_company_page.driver.switch_to.alert
    #     alert.accept()

    #     assert new_company_page.driver.current_url == "https://ads.vk.com/cases"

    # def test_select_lead_again(self, new_company_page: NewCompanyPage):
    #     # NOTE maybe create lead in setup and then click on it in first selector and check in second
    #     new_company_page.lead_region_click()
    #     new_company_page.select_split()

    #     new_company_page.select_lead_click(0)
    #     new_company_page.select_lead_option(0)

    #     new_company_page.select_lead_click(1)

    #     WebDriverWait(new_company_page.driver, 3).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[contains(text(), "Уже выбрана в другом селекте")]',
    #             )
    #         )
    #     )
    #     assert "Уже выбрана в другом селекте" in new_company_page.driver.page_source

    # def test_date_last_not_sooner(self, new_company_page: NewCompanyPage):
    #     new_company_page.site_region_click().send_keys_site("ababa.com")
    #     new_company_page.click_date().select_prev_month().click_first_day()

    #     current_date: datetime = datetime.now()

    #     month_ago_date = current_date - timedelta(days=current_date.day)
    #     assert (
    #         f"01.${month_ago_date.month}.${month_ago_date.year}"
    #         not in new_company_page.driver.page_source
    #     )
