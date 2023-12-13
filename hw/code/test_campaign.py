from base import BaseCase
from ui.pages.campaign_page import CampaignPage

class TestCampaign(BaseCase):

    def test_create_campaign(self):
        campaign_page = CampaignPage(self.driver)

        create_campaign_page = campaign_page.create_campaign()
        assert create_campaign_page.is_opened()

