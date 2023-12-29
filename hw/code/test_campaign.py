import datetime
from base import BaseCase
from ui.pages.campaign_page import CampaignPage
import os

class TestCampaign(BaseCase):

    def get_settings(self, repo_root):
        return dict({
        'url': 'sub-me.ru',
        'budget': '100',
        'region' : 'Москва',
        'title' : 'название объявления',
        'summary' : 'краткое описание',
        'image_path': os.path.abspath(os.path.join(repo_root, '../images/image.jpg')),
        })

    def test_create_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        new_company_elem = campaign_page.create_campaign(self.get_settings(repo_root))
        assert "Кампания " + datetime.datetime.today().strftime("%Y-%m-%d") in new_company_elem.text


