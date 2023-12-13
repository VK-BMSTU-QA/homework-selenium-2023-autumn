import time

from base import BaseCase
from ui.fixtures import *
from ui.pages.campaign_page import CampaignPage, GroupPage, AdvertisementPage
import utils


class TestCampaign(BaseCase):
    @staticmethod
    def get_campaign_data(repo_root):
        return {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'short_description': 'Тестовое описание',
                'image_path': os.path.abspath(os.path.join(repo_root, '../data/img/advertisement.jpg')),
            }
        }

    @allure.story('Create campaign')
    def test_create_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = self.get_campaign_data(repo_root)
        campaign_page.create_campaign(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Delete campaign')
    def test_delete_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        files = self.get_campaign_data(repo_root)

        campaign_page.create_campaign(files)
        campaign_name = f'Кампания {utils.get_today()}'

        campaign_page.delete_campaign(campaign_name)
        self.driver.refresh()
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind == -1

    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('campaigns', CampaignPage),
            pytest.param('groups', GroupPage),
            pytest.param('ads', AdvertisementPage),
        ]
    )
    @allure.story('Open section {to_section}')
    def test_open_section(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.open_section(to_section)
        assert page(self.driver).is_opened()
