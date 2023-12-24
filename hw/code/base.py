from ui.fixtures import login_page
import pytest

from ui.pages.campaign_page import CampaignPage
from ui.pages.registration_page import RegistrationPage


class BaseCase:
    authorize = True
    cabinet_created = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, login_page, credentials, no_cabinet_credentials):
        self.driver = driver
        self.config = config

        if self.authorize:
            print("Login...")
            if self.cabinet_created:
                login_page.login(*credentials)
                CampaignPage(driver=driver).is_opened()
            else:
                login_page.login(*no_cabinet_credentials)
                RegistrationPage(driver=driver).is_opened()
            print("Login completed.")
