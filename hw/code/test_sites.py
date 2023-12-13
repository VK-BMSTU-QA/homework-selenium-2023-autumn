from base import BaseCase
from ui.fixtures import *
from ui.pages.sites_page import SitesPage
from ui.pages.campaign_page import CampaignPage


class TestSite(BaseCase):
    @staticmethod
    def get_pixel_data():
        return {
            'by_domain': {
                'domain': 'maibx.ru',
            },
        }

    @allure.story('Create pixel')
    def test_create_pixel(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('sites')
        pixel_page = SitesPage(self.driver)
        data = self.get_pixel_data()
        pixel_page.create_pixel(data)
        assert pixel_page.find_pixel_by_domain(data['by_domain']['domain'])[0] == True
        pixel_page.delete_pixel(data['by_domain']['domain'])

    @allure.story('Delete pixel')
    def test_delete_pixel(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('sites')
        pixel_page = SitesPage(self.driver)
        data = self.get_pixel_data()
        pixel_page.create_pixel(data)
        pixel_page.delete_pixel(data['by_domain']['domain'])
        assert pixel_page.find_pixel_by_domain(data['by_domain']['domain'], 1)[0] == False
