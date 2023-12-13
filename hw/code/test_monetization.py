from time import sleep

from selenium.webdriver.common.by import By

from base import BaseCase
from ui.pages.monetization_page import MonetizationPage
from ui.pages.main_page import MainPage
from ui.fixtures import *

class TestHelpNavigation(BaseCase):
    cabinet_created = False
    authorize = False
    accept_cookie = True

    @allure.story('Banners')
    @pytest.mark.parametrize(
        'section_idx, banner',
        [
            pytest.param(4, "Баннер"),
            pytest.param(5, "Instream"),
            pytest.param(6, "Адаптивный блок"),
            pytest.param(7, "InPage"),
            pytest.param(8, "Полноэкранный блок"),
            pytest.param(9, "Sticky-баннер"),
        ]
    )
    def test_web_banners(self, section_idx, banner):
        main_page = MainPage(self.driver)
        main_page.move_to('monetization')

        monetization_page = MonetizationPage(self.driver)
        section = monetization_page.find_monetization_section()
        assert (section[section_idx].text == banner)

    @allure.story('app_banners')
    @pytest.mark.parametrize(
        'section_idx, banner',
        [
            pytest.param(10, "Баннер"),
            pytest.param(11, "Нативный формат"),
            pytest.param(12, "Полноэкранный блок"),
            pytest.param(13, "Видео за вознаграждение"),
        ]
    )
    def test_app_banners(self, section_idx, banner):
        main_page = MainPage(self.driver)
        main_page.move_to('monetization')

        monetization_page = MonetizationPage(self.driver)
        monetization_page.click_app_button()
        section = monetization_page.find_monetization_section()
        assert (section[section_idx].text == banner)
