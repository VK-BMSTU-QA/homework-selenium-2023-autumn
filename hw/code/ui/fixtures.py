import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from ui.pages.audience_page import AudiencePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.base_page import BasePage
from ui.pages.create_cabinet_page import CreateCabinetPage
from ui.pages.hq_page import HqPage
from ui.pages.login_page import LoginPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.budget_page import BudgetPage
from ui.pages.sites_page import SitesPage
from ui.pages.campaign_creation_page import CampaignCreationPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    headless = config['headless']
    options = Options()

    if headless:
        options.add_argument('--headless=new')

    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        service = Service(executable_path='/snap/bin/firefox.geckodriver')
        browser = webdriver.Firefox(service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def credentials(load_env):
    return os.getenv("LOGIN"), os.getenv("PASSWORD")


@pytest.fixture(scope='session')
def no_cabinet_credentials(load_env):
    return os.getenv("NO_CABINET_LOGIN"), os.getenv("NO_CABINET_PASSWORD")


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    driver.get(LoginPage.url)
    return LoginPage(driver=driver)


@pytest.fixture
def registration_page(driver):
    driver.get(RegistrationPage.url)
    return RegistrationPage(driver=driver)


@pytest.fixture
def create_cabinet_page(driver):
    driver.get(CreateCabinetPage.url)
    return CreateCabinetPage(driver=driver)


@pytest.fixture
def hq_page(driver):
    driver.get(HqPage.url)
    return HqPage(driver=driver)


@pytest.fixture
def audience_page(driver):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)


@pytest.fixture
def settings_page(driver):
    driver.get(SettingsPage.url)
    return SettingsPage(driver=driver)


@pytest.fixture
def settings_notifications_page(driver):
    driver.get(SettingsNotificationsPage.url)
    return SettingsNotificationsPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    driver.get(CampaignPage.url)
    return CampaignPage(driver=driver)


@pytest.fixture
def budget_page(driver):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)


@pytest.fixture
def sites_page(driver):
    driver.get(SitesPage.url)
    return SitesPage(driver=driver)

@pytest.fixture
def campaign_creation_page(driver):
    driver.get(CampaignCreationPage.url)
    return CampaignCreationPage(driver=driver)
