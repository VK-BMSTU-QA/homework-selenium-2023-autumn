import pytest
from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):
    @pytest.mark.skip('skip')
    @pytest.mark.parametrize(
        'tab_name,tab_url',
        [
            pytest.param(AudiencePage.AUDIENCE_TAB, 'https://ads.vk.com/hq/audience'),
            pytest.param(AudiencePage.USERS_TAB, 'https://ads.vk.com/hq/audience/user_lists'),
        ]
    )
    def test_tab_navigation(self, audience_page, tab_name, tab_url):
        audience_page.go_to_tab(tab_name)
        audience_page.check_url(tab_url)
