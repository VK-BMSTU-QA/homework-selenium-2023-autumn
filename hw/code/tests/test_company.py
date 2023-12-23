from datetime import datetime, timezone, timedelta
import pytest
import time
from tests.base_case import BaseCase, credentials, AllLinks
from ui.pages.company_page import CompanyPage
from tests.base_case import cookies_and_local_storage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

from time import gmtime, strftime

strftime("%Y-%m-%d %H:%M:%S", gmtime())


# HACK
def is_matching_link(link, base_url):
    # Parse the link and base_url
    parsed_link = urlparse(link)
    parsed_base_url = urlparse(base_url)

    # Check if the link starts with the base URL
    return (
        parsed_link.scheme == parsed_base_url.scheme
        and parsed_link.netloc == parsed_base_url.netloc
        and parsed_link.path.startswith(parsed_base_url.path)
    )


class TestCompany(BaseCase):
    authorize = True

    @pytest.fixture
    def preparations(self, company_page: CompanyPage):
        company_page.close_banner()
        yield company_page

    def test_create(self, preparations):
        preparations.create_company()
        assert is_matching_link(preparations.get_current_url(), AllLinks.COMPANY_CREATE)

    def test_group(self, preparations):
        preparations.group_view(5)
        assert is_matching_link(preparations.get_current_url(), AllLinks.GROUP)

    def test_advertisment(self, preparations):
        preparations.advertisment_view(5)
        assert is_matching_link(preparations.get_current_url(), AllLinks.ADVERTISEMENTS)

    def test_list(self, preparations):
        preparations.select_action_list()

        selector_classes = preparations.get_selector_attribute()
        # NOTE class can be taken out
        assert "vkuiCustomSelect--pop-down" not in selector_classes

    def test_download(self, preparations):
        preparations.download(5)
        # NOTE can be taken out
        assert not preparations.is_on_site_text("Отчет по датам")

    def test_settings(self, preparations):
        preparations.settings(5)
        # NOTE can be taken out
        assert not preparations.is_on_site_text("Настроить столбцы")

    @pytest.fixture
    def setup_filter(self, preparations):
        preparations.select_filter().select_deleted_filter().apply_filters()
        yield preparations
        preparations.select_filter().select_deleted_filter().apply_filters()

    def test_select_company_settings(self, setup_filter: CompanyPage):
        setup_filter.select_company().settings()
        assert setup_filter.is_on_site_text("Настроить столбцы")

    def test_select_company_downloads(self, setup_filter):
        setup_filter.select_company().download()
        assert setup_filter.is_on_site_text("Отчет по датам")

    @pytest.fixture
    def create_company(self, new_company_page):
        # TODO make creation of company
        company_page = CompanyPage(new_company_page.driver)
        company_page.select_filter().select_started_filter().apply_filters()
        yield company_page

    def test_company_deletion(self, create_company):
        create_company.select_company().select_action_list().select_delete_action()
        assert create_company.is_on_site_text("Ничего не нашлось")

    @pytest.fixture
    def create_draft(self, company_page):
        # TODO make creation of draft
        yield company_page
        company_page.select_company().delete_draft()

    def test_draft(self, create_draft):
        create_draft.go_to_drafts().delete_draft()
        assert create_draft.is_on_site_text("Создайте первую рекламную кампанию")
