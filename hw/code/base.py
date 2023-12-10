import time
from ui.fixtures import login_page
import pytest

from ui.pages.registration_page import RegistrationPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, login_page, credentials):
        self.driver = driver
        self.config = config

        if self.authorize:
            login_page.login(*credentials)
            RegistrationPage(driver=driver).is_opened()
