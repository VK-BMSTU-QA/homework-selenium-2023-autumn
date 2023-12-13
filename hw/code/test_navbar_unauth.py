from base import BaseCase
from ui.fixtures import *
from ui.pages.main_page import MainPage
from ui.pages.news_page import NewsPage
from ui.pages.cases_page import CasesPage
from ui.pages.forum_page import ForumPage
from ui.pages.monetization_page import MonetizationPage
from ui.pages.oauth_page import OauthPage
from ui.pages.help_page import HelpPage


class TestCabinetNavigation(BaseCase):
    authorize = False
    cabinet_created = False

    @allure.story('Navbar unauthorised')
    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('logo', MainPage),
            pytest.param('news', NewsPage),
            pytest.param('cases', CasesPage),
            pytest.param('ideas_forum', ForumPage),
            pytest.param('monetization', MonetizationPage),
            pytest.param('help', HelpPage),
            pytest.param('cabinet', OauthPage),
        ]
    )
    def test_navigation(self, to_section, page):
        base_page = MainPage(self.driver)
        base_page.move_to(to_section)
        assert page(self.driver).is_opened()
