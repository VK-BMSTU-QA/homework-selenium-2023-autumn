import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage


@pytest.fixture()
def driver(config):
    browser = config["browser"]
    options = Options()
    service = Service(executable_path=GeckoDriverManager().install())
    if browser == "chrome":
        driver = webdriver.Chrome(options=options, service=service)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        browser = webdriver.Firefox(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    options = Options()
    service = Service(executable_path=GeckoDriverManager().install())
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        options = webdriver.FirefoxOptions()

        # browser = webdriver.Chrome(service=service, options=options)
        browser = webdriver.Firefox(options=options, service=service)

    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')

    browser.maximize_window()
    return browser


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def all_drivers(config, request):
    url = config["url"]
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)
