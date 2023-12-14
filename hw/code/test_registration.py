import pytest

from ui.fixtures import registration_page
from base import BaseCase
from ui.pages.create_cabinet_page import CreateCabinetPage


class TestRegistration(BaseCase):
    cabinet_created = False

    def test_create_cabinet(self, registration_page):
        registration_page.create_cabinet()
        CreateCabinetPage(driver=self.driver).is_opened()
