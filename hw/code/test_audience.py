import pytest
from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):
    create_cabinet = True

    # @pytest.mark.skip('skip')
    @pytest.mark.parametrize(
        'tab_name,tab_url',
        [
            pytest.param(AudiencePage.AUDIENCE_TAB, 'https://ads.vk.com/hq/audience'),
            pytest.param(AudiencePage.USERS_TAB, 'https://ads.vk.com/hq/audience/user_lists'),
        ]
    )
    def test_tab_navigation(self, tab_name, tab_url):
        print("test_tab_navigation start")
        self.driver.get(AudiencePage.url)
        page = AudiencePage(driver=self.driver)
        page.go_to_tab(tab_name)
        page.check_url(tab_url)
        print("test_tab_navigation end")
