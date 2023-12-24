from datetime import datetime, timezone, timedelta
import pytest
import time
from tests.base_case import BaseCase, credentials, AllLinks
from ui.pages.company_page import CompanyPage
from ui.pages.adv_page import AdvPage
from ui.pages.group_adv_page import GroupAdvPage
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

    @pytest.fixture
    def setup_started_filters(self, preparations):
        preparations.select_filter().select_started_filter().apply_filters()
        yield preparations
        preparations.select_filter().select_started_filter().apply_filters()

    def test_download(self, setup_started_filters):
        setup_started_filters.download(5)
        # NOTE can be taken out
        assert not setup_started_filters.is_on_site_text("Отчет по датам")

    def test_settings(self, setup_started_filters):
        setup_started_filters.settings(5)
        # NOTE can be taken out
        assert not setup_started_filters.is_on_site_text("Настроить столбцы")

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
        page = AdvPage.__new__(AdvPage)
        page.driver = new_company_page.driver
        page.create_company()

        company_page = CompanyPage(new_company_page.driver)
        company_page.select_filter().select_started_filter().apply_filters()
        yield company_page

    def test_company_deletion(self, create_company):
        while True:
            try:
                create_company.select_company().select_action_list().select_delete_action()
            except:
                break
        assert create_company.is_on_site_text(
            "Ничего не нашлось"
        ) or create_company.is_on_site_text("Создайте первую рекламную кампанию")

    @pytest.fixture
    def create_draft(self, company_page):
        page = GroupAdvPage(company_page.driver)
        page.get_to_next()

        company_page.open()

        yield company_page

    def test_draft(self, create_draft):
        create_draft.go_to_drafts()
        while True:
            try:
                create_draft.select_draft_option().delete_draft().click_approve_delete()
            except:
                break

        assert create_draft.is_on_site_text("Создайте первую рекламную кампанию")
