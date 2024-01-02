from tests.base_case import BaseCase
from ui.pages.login_page import LoginPage


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials, login_page: LoginPage):
        login_page.login(credentials["user"], credentials["password"])

        assert login_page.check_auth_cookie()
