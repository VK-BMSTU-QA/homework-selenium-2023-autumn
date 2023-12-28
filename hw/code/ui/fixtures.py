import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.cases_page import CasesPage
from ui.pages.hq_page import HqPage
from ui.pages.lead_page import LeadPage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationMainPage, RegistrationPage
from ui.pages.upvote_page import UpvotePage
from ui.pages.ad_groups_page import AdGroupsPage, AdGroupDraftsPage
from ui.pages.partner_page import PartnerPage
from ui.pages.help_page import HelpPage
from ui.pages.audience_page import AudiencePage
from ui.pages.webinars_page import WebinarsPage
from ui.pages.companies_page import CompaniesPage
from ui.pages.ecomm_page import EcommPage
from ui.pages.sites_page import SitesPage
from dotenv import load_dotenv


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    if selenoid:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        options.default_capabilities = capabilities
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub', options=options)
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
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
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def cases_page(driver):
    driver.get(CasesPage.url)
    return CasesPage(driver=driver)


@pytest.fixture
def partner_page(driver):
    driver.get(PartnerPage.url)
    return PartnerPage(driver=driver)


@pytest.fixture
def help_page(driver):
    driver.get(HelpPage.url)
    return HelpPage(driver=driver)


@pytest.fixture
def registration_main_page(driver):
    driver.get(RegistrationMainPage.url)
    return RegistrationMainPage(driver=driver)


@pytest.fixture(scope='session')
def load_env():
    load_dotenv('.test_env')


@pytest.fixture(scope='session')
def credentials(load_env):
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"), os.getenv("METHOD"))


@pytest.fixture(scope='session')
def no_cabinet_credentials(load_env):
    return (os.getenv("NO_CABINET_LOGIN"), os.getenv("NO_CABINET_PASSWORD"), os.getenv("NO_CABINET_METHOD"))


@pytest.fixture
def registration_page(registration_main_page, no_cabinet_credentials):
    return registration_main_page.go_to_account_creation(*no_cabinet_credentials)


@pytest.fixture(scope='session')
def create_account(config, credentials):
    if not config['create_account']:
        yield  # Хак, иначе pytest ругается, что мы не дошли до следующего yield
        return

    driver = get_driver(config['browser'])

    driver.get(RegistrationMainPage.url)
    page = RegistrationMainPage(driver)

    acc_creation_page = page.go_to_account_creation(*credentials)
    acc_creation_page.fill_in_form('example@mail.org')

    page = HqPage(driver)
    driver.quit()

    yield

    driver = get_driver(config['browser'])

    driver.get(RegistrationMainPage.url)
    RegistrationMainPage(driver).login(*credentials)

    page = HqPage(driver)
    page.delete_account()
    driver.quit()


@pytest.fixture
def hq_page(create_account, registration_main_page, credentials):
    registration_main_page.login(*credentials)
    return HqPage(registration_main_page.driver)


@pytest.fixture
def audience_page(hq_page):
    hq_page.driver.get(AudiencePage.url)
    return AudiencePage(driver=hq_page.driver)


@pytest.fixture
def webinar_page(driver):
    driver.get(WebinarsPage.url)
    return WebinarsPage(driver=driver)


@pytest.fixture
def companies_page(hq_page):
    return CompaniesPage(hq_page.driver)


@pytest.fixture
def ad_groups_page(hq_page):
    hq_page.driver.get(AdGroupsPage.url)
    page = AdGroupsPage(driver=hq_page.driver)
    yield page
    page.clear_drafts()


@pytest.fixture
def ad_group_creation_page(ad_groups_page):
    return ad_groups_page.go_to_creation()


@pytest.fixture
def ecomm_page(hq_page):
    hq_page.driver.get(EcommPage.url)
    return EcommPage(driver=hq_page.driver)


@pytest.fixture
def sites_page(hq_page):
    hq_page.driver.get(SitesPage.url)
    return SitesPage(driver=hq_page.driver)


@pytest.fixture
def ad_group_drafts_page(ad_group_creation_page):
    ad_group_creation_page.driver.get(AdGroupDraftsPage.url)
    return AdGroupDraftsPage(ad_group_creation_page.driver)


@pytest.fixture
def upvote_page(driver):
    driver.get(UpvotePage.url)
    return UpvotePage(driver)


@pytest.fixture
def lead_page(hq_page):
    hq_page.driver.get(LeadPage.url)
    return LeadPage(hq_page.driver)
