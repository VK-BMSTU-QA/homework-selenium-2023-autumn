import pytest

from ui.fixtures import registration_page
from base import BaseCase
from ui.pages.base_page import BasePage
from ui.pages.create_cabinet_page import CreateCabinetPage


class TestRegistration(BaseCase):
    cabinet_created = False

    def test_create_cabinet(self, registration_page):
        registration_page.create_cabinet()
        CreateCabinetPage(driver=self.driver).is_opened()

    @pytest.mark.parametrize(
        'lang',
        [pytest.param('ru'), pytest.param('en')]
    )
    def test_switch_language(self, registration_page, lang):
        registration_page.choose_language(lang)
        registration_page.is_language(lang)

    def test_logout(self, registration_page):
        registration_page.logout()
        BasePage(driver=self.driver).is_opened()
