import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.lk_page import LKPage
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage


@pytest.fixture(scope="session")
def driver(config):
    print("Initialize driver")

    browser = config["browser"]
    service  = None

    options = Options()
    if browser == "chrome":
        service  = ServiceChrome(executable_path=ChromeDriverManager().install())
        
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options, service=service)
        
    elif browser == "firefox":
        service  = ServiceFirefox(executable_path=GeckoDriverManager().install())

        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options, service=service)
        
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    
    # Setup
    driver.maximize_window()

    yield driver
    print("Stop driver")

    # Teardown
    driver.quit()
    service.stop()

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def lk_page(driver):
    return LKPage(driver=driver)
