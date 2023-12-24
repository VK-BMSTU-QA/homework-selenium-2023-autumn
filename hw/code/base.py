import allure
import pytest

from ui.pages.login.login_page import LoginPage
from ui.pages.base_page import PageNotOpenedExeption

CLICK_RETRY = 3


class BaseCase:
    driver = None
    config = None

    @allure.step("Setup")
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver,  config, credentials):
        self.driver = driver
        self.config = config

        self.authorize(driver, credentials)

    @allure.step("login")
    def authorize(self, driver, credentials):
        login_page = LoginPage(self.driver)

        try:
            login_page.login(*credentials)
        except PageNotOpenedExeption:
            if 'login?&fail=1' in driver.current_url:
                login_page.confirm_login(*credentials)
            else:
                raise
