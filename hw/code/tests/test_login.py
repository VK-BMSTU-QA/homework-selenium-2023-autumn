import pytest
import time
from tests.base_case import (
    BaseCase,
    credentials,
    save_localstorage_cookies_to_env,
    cookies_and_local_storage,
)
from ui.pages.login_page import LoginPage

from selenium.common.exceptions import TimeoutException


class TestLogin(BaseCase):
    authorize = False

    # # HACK
    # def test_login(self, login_page):
    #     time.sleep(100)
    #     save_localstorage_cookies_to_env(login_page.driver)

    # TODO remove comments
    # def test_login(self, credentials, login_page: LoginPage):
    # login_page.login(credentials["user"], credentials["password"])

    # try:
    #     self.driver.get_cookie("remixnsid")
    # except Exception as e:
    #     assert False, f"self.driver.get_cookie raised {e}"

    # @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
    # def test_login_neg(self, invalid_creds):
    #     with pytest.raises(TimeoutException):
    #         self.login_page.login(invalid_creds["user"], invalid_creds["password"])
