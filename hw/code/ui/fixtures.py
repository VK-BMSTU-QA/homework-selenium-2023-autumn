import os
import allure
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']

    with allure.step('Init browser'):
        browser = get_driver(config)
        browser.get(url)

    yield browser
    browser.quit()


def get_driver(config):
    browser_name = config['browser']

    if browser_name == 'chrome':
        options = Options()
        browser = webdriver.Chrome(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    return os.getenv('EMAIL'), os.getenv('PASSWORD')
