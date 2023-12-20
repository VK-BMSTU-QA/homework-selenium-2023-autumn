import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.company_page import CompanyPage
from ui.pages.lk_page import LKPage
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.pages.new_company_page import NewCompanyPage
from ui.pages.group_adv_page import GroupAdvPage


@pytest.fixture(scope="session")
def service(config):
    browser = config["browser"]
    if browser == "chrome":
        service = ServiceChrome(executable_path=ChromeDriverManager().install())

    elif browser == "firefox":
        service = ServiceFirefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    return service


@pytest.fixture(scope="session")
def driver(config, service):
    print("Initialize driver")

    browser = config["browser"]

    driver = get_driver(browser, service)
    yield driver

    print("Stop driver")

    # Teardown
    driver.quit()
    service.stop()


def get_driver(browser, service):
    options = Options()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options, service=service)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    # Setup
    driver.maximize_window()
    return driver


@pytest.fixture
def base_page(driver):
    print("INIT FIXTURE BASE PAGE")
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    print("INIT FIXTURE LOGIN PAGE")
    return LoginPage(driver=driver)


@pytest.fixture
def lk_page(driver):
    print("INIT FIXTURE LKPAGE PAGE")
    return LKPage(driver=driver)


@pytest.fixture
def company_page(driver):
    print("INIT FIXTURE COMPANY PAGE")
    return CompanyPage(driver=driver)


@pytest.fixture
def new_company_page(driver):
    print("INIT FIXTURE NEW COMPANY PAGE")
    return NewCompanyPage(driver=driver)


@pytest.fixture
def group_adv_page(driver):
    print("INIT FIXTURE GROUP PAGE")
    return GroupAdvPage(driver=driver)
