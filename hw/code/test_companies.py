from base import BaseCase
from ui.fixtures import main_page, cases_page, companies_page
import pytest


class TestCompanies(BaseCase):

    TARGET_SITE = 'event-radar.ru'
    LOW_MONEY = '10'
    CORRECT_MONEY = '1000'

    FIELD_NECESSARY = 'Обязательное поле'
    MIN_BUDGET = 'Бюджет кампании должен быть не меньше 100₽'
    AD_GROUP = 'ad_group'
    CAMPAIGN = 'Кампания'
    INVALID_NAME = 'Strange Name'

    def test_redirect_create_page(self, companies_page):
        companies_page.click_create_btn()
        assert self.is_url_open(
            'https://ads.vk.com/hq/new_create/ad_plan')

    def test_input_appearance(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        assert companies_page.get_target_input() is not None

    def test_site_neccessary_error(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.click_continue_btn()
        assert self.FIELD_NECESSARY in companies_page.driver.page_source

    def test_money_necessary_error(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.click_continue_btn()
        assert self.FIELD_NECESSARY in companies_page.driver.page_source

    def test_less_money_error(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.input_money_value(self.LOW_MONEY)
        companies_page.click_continue_btn()
        assert self.MIN_BUDGET in companies_page.driver.page_source

    def test_correct_data_redirect(self, companies_page):
        companies_page.create_company(self.TARGET_SITE, self.CORRECT_MONEY)
        assert self.AD_GROUP in self.driver.current_url.split('/')

    def test_mobile_input_appearance(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_mobileapp_target()
        assert companies_page.get_mobile_target_input() is not None

    def test_unfinished_company_appearance(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        assert companies_page.company_id() in companies_page.driver.page_source

    def test_search_in_drafts_presence(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        companies_page.input_search_query(self.CAMPAIGN)
        assert companies_page.company_id() in companies_page.driver.page_source

    def test_search_in_drafts_empty(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        companies_page.input_search_query(self.INVALID_NAME)
        assert companies_page.company_id() not in companies_page.driver.page_source
