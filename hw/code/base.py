import time
from ui.fixtures import login_page
import pytest

from ui.pages.campaigns_page import CampaignsPage
from ui.pages.create_cabinet_page import CreateCabinetPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.settings_page import SettingsPage


class BaseCase:
    authorize = True
    create_cabinet = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, login_page, credentials):
        print("Starting setup")
        self.driver = driver
        self.config = config

        if self.authorize:
            print("Login...")
            login_page.login(*credentials)
            RegistrationPage(driver=driver).is_opened()
            print("Login completed.")

        if self.create_cabinet:
            print("Creating cabinet...")
            driver.get(CreateCabinetPage.url)
            page = CreateCabinetPage(driver=driver)
            page.fill_email(credentials[0])
            page.submit_form()
            CampaignsPage(driver=self.driver).is_opened()
            print("Cabinet created.")

        print("Setup completed")

    @pytest.fixture(scope='function', autouse=True)
    def teardown(self):
        yield

        print("Starting teardown")
        if self.create_cabinet:
            print("Deleting cabinet...")
            self.driver.get(SettingsPage.url)
            page = SettingsPage(driver=self.driver)
            page.delete_cabinet()
            print("Cabinet deleted.")

        print("Teardown completed")
