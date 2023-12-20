import time
from typing import Dict
from contextlib import contextmanager
import os

from pytest import FixtureRequest
import pytest
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.lk_page import LKPage
from ui.fixtures import driver, get_driver
from conftest import config
from ui.pages.login_page import LoginPage
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


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

    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        yield
        # teardown
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
        self.driver.switch_to.window(self.driver.window_handles[-1])

        for handle in self.driver.window_handles[:-1]:
            self.driver.switch_to.window(handle)

            # Wait for any potential alert
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())

            # Handle the alert if present
            try:
                alert = self.driver.switch_to.alert
                alert.accept()  # You can also use alert.dismiss() if needed
            except:
                pass

            self.driver.close()

        self.driver.delete_all_cookies()
        time.sleep(5)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest, cookies_and_local_storage):
        print("Setup")
        self.driver = driver
        self.config = config

        # self.login_page: LoginPage = request.getfixturevalue("login_page")
        # self.lk_page: LKPage = request.getfixturevalue("lk_page")

        # main_page = BasePage(self.driver)
        if self.authorize:
            print("Setup authorize")
            cookies = request.getfixturevalue("cookies_and_local_storage")

            # HACK
            self.driver.get("https://ads.vk.com/cases")

            print("Set local")
            for key, value in cookies[1].items():
                self.driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

            print("Set cookies")
            for cookie in cookies[0]:
                self.driver.add_cookie(cookie)

            print("Open cases: https://ads.vk.com/cases")
            self.driver.get("https://ads.vk.com/cases")
            self.driver.refresh()


# TODO может убрать в confest или fixtures?


# HACK
def save_localstorage_cookies_to_env(driver):
    localstorage = driver.execute_script("return window.localStorage")
    with open("localstorage.env", "w") as f:
        json.dump(localstorage, f)

    cookies = driver.get_cookies()
    with open("cookies.env", "w") as f:
        json.dump(cookies, f)


# HACK
def load_localstorage_cookies_from_env():
    with open("cookies.env", "r") as f:
        cookies = json.load(f)
    # driver.delete_all_cookies()
    # for cookie in cookies:
    #     driver.add_cookie(cookie)

    with open("localstorage.env", "r") as f:
        localstorage = json.load(f)
    # for key, value in localstorage.items():
    #     driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")
    return cookies, localstorage


@pytest.fixture(scope="session")
def cookies_and_local_storage(credentials, config, service):
    browser = config["browser"]
    # HACK
    if credentials["password"] == "" and credentials["user"]:
        print("Hack credentials")
        # User doesn't have password => localStorage and cookies stored in env
        [cookies, local] = load_localstorage_cookies_from_env()
        return [cookies, local]

    new_driver = get_driver(browser, service)

    login_page = LoginPage(new_driver)
    login_page.login(credentials["user"], credentials["password"])

    # main_page = BasePage(new_driver)
    new_driver.refresh()
    co = new_driver.get_cookies()
    print(co)

    all_local_storage = new_driver.execute_script(
        "return Object.entries(localStorage);"
    )
    local_storage_dict = dict(all_local_storage)
    # sorted_objects = [obj for obj in co if obj.get("domain") != "id.vk.com"]
    # print(sorted_objects)
    return [co, local_storage_dict]


@pytest.fixture(scope="session")
def credentials() -> Dict[str, str | None]:
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return {"user": os.getenv("USER_CRED"), "password": os.getenv("PASSWORD_CRED")}


# HACK
class AllLinks:
    COMPANY_CREATE = "https://ads.vk.com/hq/new_create/ad_plan"
    GROUP = "https://ads.vk.com/hq/dashboard/ad_groups"
    ADVERTISEMENTS = "https://ads.vk.com/hq/dashboard/ads"
