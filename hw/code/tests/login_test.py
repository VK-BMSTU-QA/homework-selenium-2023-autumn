import pytest
from tests.base_case import BaseCase, credentials
from ui.pages.login_page import LoginPage

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials, driver, login_page: LoginPage):
        self.login_page.login(credentials['user'], credentials['password'])
        print(self.driver.get_cookie('aa'))
        self.driver.get_cookies()
        # assert main_page.url == main_page.driver.current_url
        
    '''@pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
    def test_login_neg(self, invalid_creds):
        self.login_page.login(invalid_creds['user'], invalid_creds['password'])

        # assert main_page.url != main_page.driver.driver.current_url'''
    