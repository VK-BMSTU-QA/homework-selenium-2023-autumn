from base import EMAIL, BaseCase
from ui.fixtures import *
from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.audience_page import AudiencePage
from ui.pages.budget_page import BudgetPage
from ui.pages.ecomm_page import ECommPage
from ui.pages.sites_page import SitesPage
from ui.pages.mobapps_page import MobAppsPage
from ui.pages.leadads_page import LeadAdsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.registration_page import RegistrationPage


LEGAL_ENTITY_NAME = 'Юридическое лицо'
REQUIRED_FIELD_ERROR = 'Обязательное поле'
INCORRECT_EMAIL_ERROR = 'Некорректный email адрес'


class TestCabinet(BaseCase):
    cabinet_created = False
    data = {'email': EMAIL}

    @allure.story('Create Cabinet')
    def test_success_create_cabinet(self):
        campaign_page = self.create_cabinet()
        assert campaign_page.is_opened()
        self.delete_cabinet(campaign_page)

    @allure.story('Delete Cabinet')
    def test_delete_cabinet(self):
        campaign_page = self.create_cabinet()
        self.delete_cabinet(campaign_page)
        assert LoginPage(self.driver).is_opened()

    @allure.story('Cabinet for agency')
    def test_cabinet_agency(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.fill_agency_type()
        assert registration_page.get_allowed_ac_types() == [LEGAL_ENTITY_NAME]

    @allure.story('Create Cabinet with empty email')
    def test_cabinet_email_required(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.create_cabinet_empty_email()
        assert registration_page.get_email_error_message() == REQUIRED_FIELD_ERROR

    @allure.story('Create Cabinet without rule accept')
    def test_cabinet_without_accept(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.create_cabinet_without_accept(self.data)
        assert registration_page.get_rules_error_message() == REQUIRED_FIELD_ERROR

    @allure.story('Create Cabinet with wrong email format')
    @pytest.mark.parametrize(
        'email',
        [
            pytest.param('testvkcom'),
            pytest.param('testvk.com'),
            pytest.param('test@vkcom'),
            pytest.param('@test@vk.com'),
            pytest.param('test@vk.com@'),
        ]
    )
    def test_cabinet_wrong_email_format(self, email):
        registration_page = RegistrationPage(self.driver)
        registration_page.create_cabinet_with_wrong_email(email)
        assert registration_page.get_email_format_error_message() == INCORRECT_EMAIL_ERROR


class TestCabinetNavigation(BaseCase):
    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('campaigns', CampaignPage),
            pytest.param('audience', AudiencePage),
            pytest.param('budget', BudgetPage),
            pytest.param('ecomm', ECommPage),
            pytest.param('sites', SitesPage),
            pytest.param('mobapps', MobAppsPage),
            pytest.param('leadads', LeadAdsPage),
            pytest.param('settings', SettingsPage),
        ]
    )
    def test_navigation(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to(to_section)
        assert page(self.driver).is_opened()
