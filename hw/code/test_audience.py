from base import BaseCase
from ui.fixtures import *
from ui.pages.campaign_page import CampaignPage
from ui.pages.audience_page import AudiencePage, AudienceUsersPage


class TestAudience(BaseCase):
    @staticmethod
    def get_audience_data():
        return {
            'title': 'test_audience', 
            'source': 'Ключевые фразы',
            'keywords': 'машины, тачки'
        }

    @allure.story('Create audience')
    def test_create_audience(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('audience')
        audience_page = AudiencePage(self.driver)
        data = self.get_audience_data()

        audience_page.create_audience(data)
        ind, _ = audience_page.find_ind_audience_by_name(data['title'])
        assert ind != -1

        audience_page.delete_audience(data['title'])

    @allure.story('Delete audience')
    def test_delete_audience(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('audience')
        audience_page = AudiencePage(self.driver)
        data = self.get_audience_data()

        audience_page.create_audience(data)
        audience_page.delete_audience(data['title'])

        self.driver.refresh()
        ind, _ = audience_page.find_ind_audience_by_name(data['title'])
        assert ind == -1

    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('audiences', AudiencePage),
            pytest.param('users', AudienceUsersPage),
        ]
    )
    @allure.story('Open section {to_section}')
    def test_open_section(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('audience')
        audience_page = AudiencePage(self.driver)
        audience_page.open_section(to_section)
        assert page(self.driver).is_opened()
