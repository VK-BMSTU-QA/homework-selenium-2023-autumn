import os
from dotenv import load_dotenv
from ui.fixtures import driver
from conftest import config
from ui.pages.login_page import LoginPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            for cookie in cookies:
                driver.add_cookie(cookie)


@pytest.fixture(scope='session')
def cookies(credentials, driver, config):
    login_page = LoginPage(driver)
    login_page.login(credentials["user"], credentials["password"])
    return driver.get_cookies()


@pytest.fixture(scope='session')
def credentials() -> Dict[str, str]:
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    
    return {'telephone_number': os.getenv('TELEPHONE_NUMBER'), 'password': os.getenv('PASSWORD')}

