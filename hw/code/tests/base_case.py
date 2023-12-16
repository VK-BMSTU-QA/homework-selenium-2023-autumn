from typing import Dict
from contextlib import contextmanager
import os

from pytest import FixtureRequest
import pytest
from dotenv import load_dotenv
from ui.pages.lk_page import LKPage
from ui.fixtures import driver
from conftest import config
from ui.pages.login_page import LoginPage


class BaseCase:
    driver = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.lk_page: LKPage = (request.getfixturevalue('lk_page'))

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

# TODO может убрать в confest или fixtures?

@pytest.fixture(scope='session')
def cookies(credentials, driver):
    login_page = LoginPage(driver)
    login_page.login(credentials["user"], credentials["password"])
    return driver.get_cookies()


@pytest.fixture(scope='session')
def credentials() -> Dict[str, str]:
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    
    return {'user': os.getenv('USER'), 'password': os.getenv('PASSWORD')}

