import allure
import pytest
from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.base_page import PageNotOpenedExeption


CLICK_RETRY = 3
EMAIL = 'test@mail.ru'

class BaseCase:
    driver = None
    authorize = True
    cabinet_created = True
    accept_cookie = False

    @allure.step("Setup")
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, credentials):
        self.driver = driver
        self.config = config
        self.logger = logger

        if self.accept_cookie:
            main_page = MainPage(self.driver)
            main_page.accept_cookie()

        if self.authorize:
            with allure.step("login"):
                login_page = LoginPage(self.driver)

                try:
                    login_page.login(*credentials)
                except PageNotOpenedExeption:
                    if 'login?&fail=1' in driver.current_url:
                        login_page.confirm_login(*credentials)
                    else:
                        raise

        if self.cabinet_created:
            self.campaign_page = self.create_cabinet()
            self.campaign_page.close_onboarding()

        self.logger.debug('Initial setup completed')

    @allure.step("Teardown")
    @pytest.fixture(scope='function', autouse=True)
    def teardown(self):
        yield 

        if self.cabinet_created:
            self.delete_cabinet(self.campaign_page)

        self.logger.debug('Teardown completed')

    @allure.step("creating cabinet")
    def create_cabinet(self):
        registration_page = RegistrationPage(self.driver)
        
        data = {'email': EMAIL}
        campaign_page = registration_page.create_cabinet(data)
        
        return campaign_page

    @allure.step("deleting cabinet")
    def delete_cabinet(self, campaign_page):
        campaign_page.move_to('settings')

        settings_page = SettingsPage(self.driver)
        settings_page.delete_account()
