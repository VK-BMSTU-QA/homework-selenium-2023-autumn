from base import BaseCase
from ui.fixtures import *
from ui.pages.main_page import MainPage
from ui.pages.insights_page import InsightsPage
from ui.pages.events_page import EventsPage
from ui.pages.experts_page import ExpertPage
from ui.pages.documents_page import DocumentsPage


class TestFooterNavigation(BaseCase):
    cabinet_created = False
    authorize = False
    accept_cookie = True

    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'section_idx, page',
        [
            pytest.param(1, ExpertPage),
            pytest.param(2, InsightsPage),
            pytest.param(4, EventsPage),
            pytest.param(6, DocumentsPage),
        ]
    )
    def test_footer_navigation(self, section_idx, page):
        main_page = MainPage(self.driver)
        main_page.open_footer_section(section_idx)
        assert page(self.driver).is_opened()
