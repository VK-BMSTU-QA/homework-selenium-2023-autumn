import pytest
from hw.code.tests.base_case import BaseCase
from hw.code.ui.pages.login_page import LoginPage

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials, login_page: LoginPage):
        self.login_page.login(credentials['user'], credentials['password'])

        # assert main_page.url == main_page.driver.current_url
        
    @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
    def test_login_neg(self, invalid_creds):
        self.login_page.login(invalid_creds)

        # assert main_page.url != main_page.driver.driver.current_url
    