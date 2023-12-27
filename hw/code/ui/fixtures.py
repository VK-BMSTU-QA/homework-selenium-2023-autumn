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
from ui.pages.center_of_commerce import CenterOfCommercePage
import os

@pytest.fixture(scope="session")
def service(config):
    browser = config["browser"]
    if browser == "chrome":
        service  = ServiceChrome(executable_path=ChromeDriverManager().install())
        # service  = ServiceChrome(executable_path='/usr/local/bin/geckodriver')

        
    elif browser == "firefox":
        service  = ServiceFirefox(executable_path=GeckoDriverManager().install())

    elif browser == "yandex":
        service  = ServiceChrome(executable_path='/Users/mochalovskiy/Technopark/QA/homework-selenium-2023-autumn/chromedriver-mac-x64/chromedriver')

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

    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"

        current_directory = os.getcwd()
        download_directory = os.path.join(current_directory, "tmp")
        prefs = {"download.default_directory": download_directory}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    
    # Setup
    driver.maximize_window()
    return driver

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def lk_page(driver):
    return LKPage(driver=driver)

@pytest.fixture
def company_page(driver):
    return CompanyPage(driver=driver)

@pytest.fixture
def center_of_commerce_page(driver):
    return CenterOfCommercePage(driver=driver)

