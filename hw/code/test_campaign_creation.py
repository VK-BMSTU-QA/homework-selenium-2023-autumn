import pytest
from base import BaseCase

from ui.pages.campaign_creation_page import CampaignCreationPage
from itertools import combinations
from datetime import date


class TestCampaignCreation(BaseCase):

    @staticmethod
    def get_test_campaign_info():
        return {
            'domain': 'test.com',
            'budget': 200,
            'region': 'Россия',
            'title': 'title',
            'description': 'description',
            'link': 'http://test.com'
        }

    @staticmethod
    def get_vk_campaign_info():
        return {
            'domain': 'vk.com',
            'budget': 200,
            'region': 'Россия',
            'title': 'vk title',
            'description': 'vk description',
            'link': 'http://vk.com'
        }

    placements = ['ВКонтакте', 'Одноклассники', 'Проекты VK', 'Рекламная сеть']

    def test_title_input(self, campaign_creation_page):
        campaign_creation_page.click(campaign_creation_page.locators.CAMPAIGN_SECTION_TITLE)
        campaign_creation_page.find_element(campaign_creation_page.locators.CAMPAIGN_SECTION_TITLE_INPUT)

    def test_more_btn(self, campaign_creation_page):
        campaign_creation_page.click(campaign_creation_page.locators.MORE_OPTION_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.MORE_CONTEXT_MENU)

    def test_min_budget(self, campaign_creation_page):
        domain = 'test.ru'
        budget = '1'
        campaign_creation_page.click(campaign_creation_page.locators.SITE_OPTION)
        campaign_creation_page.fill_site_domain(domain)
        campaign_creation_page.fill_budget(budget)
        campaign_creation_page.click(campaign_creation_page.locators.CONTINUE_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.MIN_BUDGET_MSG)

    def test_budget_length(self, campaign_creation_page):
        domain = 'test.ru'
        budget = '111111111111111'
        expected = '1 111 111 111 111 ₽'
        campaign_creation_page.click(campaign_creation_page.locators.SITE_OPTION)
        campaign_creation_page.fill_site_domain(domain)
        campaign_creation_page.fill_budget(budget)

        got = campaign_creation_page.get_budget_value()

        assert expected == got

    def test_zero_regions_error(self, campaign_creation_page):
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.CONTINUE_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.FOOTER_ERROR_BTN)

    def test_pick_region(self, campaign_creation_page):
        region = 'Россия'
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.region_item(region))
        assert campaign_creation_page.get_selected_regions_count() == 1

    @pytest.mark.parametrize(
        'disabling_device, enabling_device',
        [
            pytest.param(CampaignCreationPage.locators.device_option('Десктопные'),
                         CampaignCreationPage.locators.device_option('Мобильные')),

            pytest.param(CampaignCreationPage.locators.device_option('Мобильные'),
                         CampaignCreationPage.locators.device_option('Десктопные')),

        ]
    )
    def test_devices_disabling(self, campaign_creation_page, disabling_device, enabling_device):
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.DEVICES_SECTION)
        campaign_creation_page.click(disabling_device)
        campaign_creation_page.is_disabled(enabling_device)


    def test_placement_switch(self, campaign_creation_page):
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.PLACEMENT_SECTION)
        campaign_creation_page.click(campaign_creation_page.locators.PLACEMENT_SWITCH)
        campaign_creation_page.is_visible(campaign_creation_page.locators.PLACEMENT_LIST)

    def test_url_params_empty(self, campaign_creation_page):
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.URL_PARAMS_SECTION)
        campaign_creation_page.click(campaign_creation_page.locators.URL_MANUAL_LABEL_OPTION)
        campaign_creation_page.click(campaign_creation_page.locators.CONTINUE_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.URL_PARAMS_REQUIRED_FIELD_MSG)

    def test_url_params_incorrect_format(self, campaign_creation_page):
        utm_format = 'test'
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.URL_PARAMS_SECTION)
        campaign_creation_page.click(campaign_creation_page.locators.URL_MANUAL_LABEL_OPTION)
        campaign_creation_page.fill(campaign_creation_page.locators.UTM_LABEL_INPUT, utm_format)
        campaign_creation_page.click(campaign_creation_page.locators.CONTINUE_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.INCORRECT_UTM_LABEL_FORMAT_MSG)
    @pytest.mark.parametrize(
        'placements', combinations(placements, 3)
    )
    def test_placement_disabling(self, campaign_creation_page, placements):
        campaign_creation_page.go_to_ad_groups(self.get_test_campaign_info())
        enabled_place = [place for place in self.placements if place not in placements][0]
        campaign_creation_page.click(campaign_creation_page.locators.PLACEMENT_SECTION)
        campaign_creation_page.click(campaign_creation_page.locators.PLACEMENT_SWITCH)
        for place in placements:
            campaign_creation_page.click(campaign_creation_page.locators.placement_option(place))

        campaign_creation_page.click(campaign_creation_page.locators.placement_option(enabled_place))
        campaign_creation_page.find_element(campaign_creation_page.locators.checked_placement_checkbox(enabled_place))

    def test_ad_title_input(self, campaign_creation_page):
        campaign_creation_page.go_to_ads(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.AD_SECTION_TITLE)
        campaign_creation_page.find_element(campaign_creation_page.locators.AD_SECTION_TITLE_INPUT)

    @pytest.mark.parametrize(
        'input_item, input_name',
        [
            pytest.param(CampaignCreationPage.locators.TITLE_INPUT,
                         'Заголовок'),

            pytest.param(CampaignCreationPage.locators.SHORT_DESCRIPTION_INPUT,
                         'Короткое описание'),

        ]
    )
    def test_input_required(self, campaign_creation_page, input_item, input_name):
        error_msg = 'Обязательное поле'
        campaign_creation_page.go_to_ads(self.get_test_campaign_info())
        campaign_creation_page.fill(input_item, '')
        campaign_creation_page.click(campaign_creation_page.locators.PUBLISH_BTN)
        campaign_creation_page.find_element(CampaignCreationPage.locators.form_item_error_msg(input_name, error_msg))

    @pytest.mark.parametrize(
        'input_item, input_name, max_length',
        [
            pytest.param(CampaignCreationPage.locators.TITLE_INPUT, 'Заголовок', 40),
            pytest.param(CampaignCreationPage.locators.SHORT_DESCRIPTION_INPUT, 'Короткое описание', 90),
            pytest.param(CampaignCreationPage.locators.LONG_DESCRIPTION_INPUT, 'Длинное описание', 2000),
            pytest.param(CampaignCreationPage.locators.BTN_TEXT_INPUT, 'Текст рядом с кнопкой', 30),
            pytest.param(CampaignCreationPage.locators.ADVERTISER_DATA_INPUT, 'Данные рекламодателя', 115),
        ]
    )
    def test_max_input_length(self, campaign_creation_page, input_item, input_name, max_length):
        title = 'a' * (max_length + 1)
        error_msg = 'Превышена максимальная длина поля'
        campaign_creation_page.go_to_ads(self.get_test_campaign_info())
        campaign_creation_page.fill(input_item, title)
        campaign_creation_page.click(campaign_creation_page.locators.PUBLISH_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.form_item_error_msg(input_name, error_msg))

    def test_incorrect_site_link(self, campaign_creation_page):
        error_msg = 'Неверный формат URL'
        input_name = 'Ссылка на сайт'
        link = 'test'
        campaign_creation_page.go_to_ads(self.get_test_campaign_info())
        campaign_creation_page.fill_site_link(link)
        campaign_creation_page.click(campaign_creation_page.locators.PUBLISH_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.form_item_error_msg(input_name, error_msg))

    def test_empty_logo(self, campaign_creation_page):
        error_msg = 'Обязательное поле'
        input_name = 'Логотип'
        campaign_creation_page.go_to_ads(self.get_test_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.NATIVE_BLOCK_BTN)
        campaign_creation_page.click(campaign_creation_page.locators.PUBLISH_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.form_item_error_msg(input_name, error_msg))

    def test_empty_media_files(self, campaign_creation_page):
        campaign_creation_page.go_to_ads(self.get_vk_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.NATIVE_BLOCK_BTN)
        campaign_creation_page.fill_ad_info(self.get_vk_campaign_info())
        campaign_creation_page.click(campaign_creation_page.locators.PUBLISH_BTN)
        campaign_creation_page.click(campaign_creation_page.locators.SEND_BTN)
        campaign_creation_page.find_element(campaign_creation_page.locators.EMPTY_MEDIA_FILES_BANNER)

    def test_successful_campaign_creation(self, campaign_creation_page):
        campaign_name = 'Кампания ' + str(date.today())
        campaign_creation_page.go_to_ads(self.get_vk_campaign_info())
        campaign_creation_page.fill_ad_section(self.get_vk_campaign_info())
        campaign_creation_page.find_element(campaign_creation_page.locators.campaign_list_row(campaign_name))
        campaign_creation_page.delete_campaign(campaign_name)

