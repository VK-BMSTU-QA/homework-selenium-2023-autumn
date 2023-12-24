import time

import pytest
from ui.pages.campaign_page import CampaignPage
from base import BaseCase


class TestCampaign(BaseCase):

    create_new_plan_url = 'https://ads.vk.com/hq/new_create/ad_plan'

    @pytest.fixture(autouse=True)
    def try_close_edu_modal(self, campaign_page):
        campaign_page.close_edu_modal()

    @pytest.mark.parametrize(
        'tab_name,tab_url',
        [
            pytest.param(CampaignPage.CAMPAIGN_TAB, 'https://ads.vk.com/hq/dashboard/ad_plans'),
            pytest.param(CampaignPage.GROUPS_TAB, 'https://ads.vk.com/hq/dashboard/ad_groups'),
            pytest.param(CampaignPage.ADS_TAB, 'https://ads.vk.com/hq/dashboard/ads'),
        ]
    )
    def test_tab_navigation(self, campaign_page, tab_name, tab_url):
        campaign_page.close_edu_modal()
        campaign_page.go_to_tab(tab_name)
        campaign_page.check_url(tab_url)

    def test_campaign_creation_btn(self, campaign_page):
        campaign_page.close_edu_modal()
        campaign_page.click(campaign_page.locators.CAMPAIGN_CREATION_BTN)
        campaign_page.check_url(self.create_new_plan_url)

    def test_filter_btn(self, campaign_page):
        campaign_page.close_edu_modal()
        campaign_page.click(campaign_page.locators.FILTER_BTN)
        campaign_page.find_element(campaign_page.locators.FILTER_FORM)

    def test_data_range_picker_btn(self, campaign_page):
        campaign_page.close_edu_modal()
        campaign_page.click(campaign_page.locators.RANGE_DATA_BTN)
        campaign_page.find_element(campaign_page.locators.RANGE_DATA_PICKER_WIDGET)


    def test_search_input(self, campaign_page):
        campaign_page.close_edu_modal()
        query = 'test'
        campaign_page.fill_search_input(query)
        campaign_page.find_element(campaign_page.locators.search_bage(query))

    def test_settings_btn(self, campaign_page):
        campaign_page.close_edu_modal()
        campaign_page.is_disabled(campaign_page.locators.SETTINGS_BTN)

    def test_download_btn(self, campaign_page):
        campaign_page.close_edu_modal()
        campaign_page.is_disabled(campaign_page.locators.DOWNLOAD_BTN)
