from ui.fixtures import login_page
import pytest

from ui.pages.campaigns_page import CampaignsPage
from ui.pages.create_cabinet_page import CreateCabinetPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.settings_page import SettingsPage


class BaseCase:
    authorize = True
    create_cabinet = False
    general_info_set = False

    _cabinet_deletion_failed = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, login_page, credentials):
        print("Starting setup")
        self.driver = driver
        self.config = config

        if self.authorize:
            print("Login...")
            login_page.login(*credentials)
            try:
                RegistrationPage(driver=driver).is_opened()
            except:
                self._cabinet_deletion_failed = True
                CampaignsPage(driver=driver).is_opened()
            print("Login completed.")

        if self.create_cabinet and not self._cabinet_deletion_failed:
            print("Creating cabinet...")
            driver.get(CreateCabinetPage.url)
            page = CreateCabinetPage(driver=self.driver)
            page.fill_email(credentials[0])
            page.submit_form()
            CampaignsPage(driver=self.driver).is_opened()
            print("Cabinet created.")

            if self.general_info_set:
                driver.get(SettingsPage.url)
                page = SettingsPage(driver=driver)
                page.edit_general(phone='+79000000000', fio='Петр Иванов Иванович', inn='12345678901')
                print("General info filled.")

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
        self.driver.quit()

        print("Teardown completed")
