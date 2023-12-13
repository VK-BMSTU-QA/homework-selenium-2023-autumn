from ui.fixtures import login_page
import pytest

from ui.pages.campaigns_page import CampaignsPage
from ui.pages.registration_page import RegistrationPage


class BaseCase:
    authorize = True
    create_cabinet = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, login_page, create_cabinet_page, credentials):
        print("Starting setup")
        self.driver = driver
        self.config = config

        if self.authorize:
            print("Login...")
            login_page.login(*credentials)
            # try:
            RegistrationPage(driver=driver).is_opened()
            # except:
            # CampaignsPage(driver=driver).is_opened()
            print("Login completed.")

        if self.create_cabinet:
            print("Creating cabinet...")
            create_cabinet_page.fill_email(credentials[0])
            create_cabinet_page.submit_form()
            CampaignsPage(driver=self.driver).is_opened()
            print("Cabinet created.")

        print("Setup completed")

    @pytest.fixture(scope='function', autouse=True)
    def teardown(self, settings_page):
        yield

        print("Starting teardown")
        if self.create_cabinet:
            print("Deleting cabinet...")
            settings_page.delete_cabinet()
            print("Cabinet deleted.")
        self.driver.quit()

        print("Teardown completed")
