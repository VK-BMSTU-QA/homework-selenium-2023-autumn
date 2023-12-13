from time import sleep

from selenium.webdriver.common.by import By

from base import BaseCase
from ui.pages.help_documents_page import HelpDocumentsPage
from ui.pages.help_features_page import HelpFeaturesPage
from ui.pages.help_general_page import HelpGeneralPage
from ui.pages.help_mini_ads_page import HelpMiniAdsPage
from ui.pages.help_statistics_page import HelpStatisticsPage
from ui.pages.main_page import MainPage
from ui.pages.help_authorization_page import HelpAuthorizationPage
from ui.fixtures import *
from ui.pages.help_page import HelpPage


class TestHelpNavigation(BaseCase):
    cabinet_created = False
    authorize = False
    accept_cookie = True

    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'section_idx, page',
        [
            pytest.param(0, HelpAuthorizationPage),
            pytest.param(1, HelpGeneralPage),
            pytest.param(2, HelpFeaturesPage),
            pytest.param(3, HelpStatisticsPage),
            pytest.param(4, HelpDocumentsPage),
            pytest.param(5, HelpMiniAdsPage),
        ]
    )
    def test_help_navigation(self, section_idx, page):
        main_page = MainPage(self.driver)
        main_page.move_to('help')

        help_page = HelpPage(self.driver)
        help_page.open_help_section(section_idx)
        assert page(self.driver).is_opened()
