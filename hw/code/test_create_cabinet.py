from ui.fixtures import create_cabinet_page
from base import BaseCase
import pytest

from ui.pages.campaign_page import CampaignPage
from ui.pages.settings_page import SettingsPage


class TestCreateCabinet(BaseCase):
    cabinet_created = False

    def test_physical_disabled_due_to_agency(self, create_cabinet_page):
        create_cabinet_page.click(create_cabinet_page.locators.AGENCY_RADIO)
        create_cabinet_page.is_invisible(create_cabinet_page.locators.PHYSICAL_RADIO)

    @pytest.mark.parametrize(
        'country,currencies',
        [
            pytest.param('Россия', ('Российский рубль (RUB)',)),
            pytest.param('Германия', ('Доллар США (USD)', 'Евро (EUR)')),
        ]
    )
    def test_available_currencies(self, create_cabinet_page, country, currencies):
        create_cabinet_page.select_country(country)
        assert create_cabinet_page.available_currencies(currencies[0]) == currencies

    def test_empty_email(self, create_cabinet_page):
        create_cabinet_page.fill_email('')
        create_cabinet_page.submit_form()
        assert create_cabinet_page.has_email_error()

    def test_too_long_email(self, create_cabinet_page):
        create_cabinet_page.fill_email(f'{"a" * 255}@mail.ru')
        create_cabinet_page.submit_form()
        assert create_cabinet_page.has_form_error()

    def test_unaccepted_terms(self, create_cabinet_page, credentials):
        create_cabinet_page.fill_email(credentials[0])
        create_cabinet_page.switch_terms()
        create_cabinet_page.submit_form()
        assert create_cabinet_page.has_terms_error()

    def test_valid_form(self, create_cabinet_page, credentials):
        create_cabinet_page.fill_email(credentials[0])
        create_cabinet_page.submit_form()
        CampaignPage(driver=self.driver).is_opened()

        self.driver.get(SettingsPage.url)
        page = SettingsPage(driver=self.driver)
        page.delete_cabinet()
