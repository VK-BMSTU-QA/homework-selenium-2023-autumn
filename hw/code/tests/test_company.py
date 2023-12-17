from datetime import datetime, timezone, timedelta
import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.company_page import CompanyPage
from tests.base_case import cookies_and_local_storage

from selenium.common.exceptions import TimeoutException

from time import gmtime, strftime
strftime("%Y-%m-%d %H:%M:%S", gmtime())


class TestCompany(BaseCase):
    authorize = True

    def test_create(self, company_page: CompanyPage, cookies_and_local_storage):
        print(self.driver.get_cookies())

        company_page.close_banner()
        company_page.create_company()

        time.sleep(5)

        datetime_moscow = datetime.now(timezone(timedelta(hours=+3), 'MSC'))

        assert f"Кампания {datetime_moscow.strftime('%Y-%m-%d')}" in self.driver.page_source