import time

import utils
from ui.fixtures import *
from base import BaseCase
from ui.pages.campaign.campaign_page import CampaignPage


class TestCampaign(BaseCase):

    @allure.story('Create campaign via site')
    def test_create_campaign_via_site(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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

        campaign_page.create_campaign_via_site(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Create campaign via community')
    def test_create_campaign_via_community(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'description': 'Тестовое описание',
                'image_path': os.path.abspath(os.path.join(repo_root, '../data/img/advertisement.jpg')),
                'advertiser': 'Тест',
            }
        }

        campaign_page.create_campaign_via_community(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Create campaign via classmates')
    def test_create_campaign_via_classmates(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'odkl': 'mdk',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'description': 'Тестовое описание',
                'image_path': os.path.abspath(os.path.join(repo_root, '../data/img/advertisement.jpg')),
                'advertiser': 'Тест',
            }
        }

        campaign_page.create_campaign_via_classmates(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Create campaign via catalog')
    def test_create_campaign_via_catalog(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'carousel_description': 'Тест',
                'banner_description': 'Тест',
                'long_description': 'Тест',
                'video_path': os.path.abspath(os.path.join(repo_root, '../data/img/catalog.mp4')),
                'carousel_card': 'Тест',
                'advertiser': 'Тест',
            }
        }

        campaign_page.create_campaign_via_catalog(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Create campaign via catalog')
    def test_create_campaign_via_vk_apps(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'miniapps': 'game',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'description': 'Тест',
                'image_path': os.path.abspath(os.path.join(repo_root, '../data/img/advertisement.jpg')),
            }
        }

        campaign_page.create_campaign_via_vk_apps(data)
        campaign_name = f'Кампания {utils.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Delete campaign')
    def test_delete_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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

        campaign_page.create_campaign_via_site(data)
        campaign_name = f'Кампания {utils.get_today()}'

        campaign_page.delete_campaign(campaign_name)
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind == -1

    @allure.story('Delete draft')
    def test_delete_draft(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
        }

        campaign_page.create_draft_via_site(data)

        draft_name = f'Кампания {utils.get_today()}'

        campaign_page.delete_draft(draft_name)
        ind, _ = campaign_page.find_ind_campaign_by_name(draft_name)
        assert ind == -1

    @allure.story('Create campaign via site empty url')
    def test_create_campaign_via_site_empty_url(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
        }

        settings_page = campaign_page.create_campaign_via_site_empty_url(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_EMPTY_URL_LABEL
        ) == True

    @allure.story('Create campaign via site incorrect url')
    def test_create_campaign_via_site_incorrect_url(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'gdfgdgdg',
            },
        }

        settings_page = campaign_page.create_campaign_via_site_incorrect_url(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_URL_LABEL
        ) == True

    @allure.story('Create campaign via site incorrect budget')
    def test_create_campaign_via_site_incorrect_budget(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
                'budget': '99',
            },
        }

        settings_page = campaign_page.create_campaign_via_site_incorrect_budget(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_BUDGET_LABEL
        ) == True

    @allure.story('Create campaign via site incorrect region')
    def test_create_campaign_via_site_incorrect_region(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
        }

        groups_page = campaign_page.create_campaign_via_site_incorrect_region(data)
        assert groups_page.find_elem_by_locator(
            groups_page.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_REGION_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via site empty title')
    def test_create_campaign_via_site_empty_title(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_empty_title(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via site long title')
    def test_create_campaign_via_site_long_title(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': utils.long_text(41)
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_long_title(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via site empty short description')
    def test_create_campaign_via_site_empty_short_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_empty_short_description(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_site_long_short_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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
                'short_description': utils.long_text(91),
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_long_short_description(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_site_long_long_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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
                'short_description': 'Тест',
                'long_description': utils.long_text(2001),
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_long_long_description(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_site_long_button_text(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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
                'short_description': 'Тест',
                'long_description': 'Тест',
                'button_text': utils.long_text(31),
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_long_button_text(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_site_long_advertiser(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
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
                'short_description': 'Тест',
                'long_description': 'Тест',
                'button_text': 'Тест',
                'advertiser': utils.long_text(116),
            }
        }

        advertisements_page = campaign_page.create_campaign_via_site_long_advertiser(data)
        assert advertisements_page.find_elem_by_locator(
            advertisements_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via catalog empty url')
    def test_create_campaign_via_catalog_empty_url(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
        }

        settings_page = campaign_page.create_campaign_via_catalog_empty_url(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_EMPTY_URL_LABEL
        ) == True

    @allure.story('Create campaign via catalog incorrect url')
    def test_create_campaign_via_catalog_incorrect_url(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'sgfgsgsfg',
            },
        }

        settings_page = campaign_page.create_campaign_via_catalog_incorrect_url(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_INCORRECT_URL_LABEL
        ) == True

    @allure.story('Create campaign via catalog empty catalog')
    def test_create_campaign_via_catalog_empty_catalog(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'site': 'vk.com',
            },
        }

        settings_page = campaign_page.create_campaign_via_catalog_empty_catalog(data)
        assert settings_page.find_elem_by_locator(
            settings_page.locators.CREATE_CAMPAIGN_SETTINGS_EMPTY_URL_LABEL
        ) == True

    @allure.story('Create campaign via empty title')
    def test_create_campaign_via_catalog_empty_title(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_empty_title(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via long title')
    def test_create_campaign_via_catalog_long_title(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': utils.long_text(26)
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_long_title(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    @allure.story('Create campaign via empty carousel description')
    def test_create_campaign_via_catalog_empty_carousel_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_empty_carousel_description(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_catalog_long_carousel_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'carousel_description': utils.long_text(51),
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_long_carousel_description(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_catalog_empty_banner_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'carousel_description': 'Тест',
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_empty_banner_description(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_catalog_long_banner_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'carousel_description': 'Тест',
                'banner_description': utils.long_text(126)
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_long_banner_description(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)

    def test_create_campaign_via_catalog_long_long_description(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = {
            'settings': {
                'ecomm': 'club_vsemayki',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'carousel_description': 'Тест',
                'banner_description': 'Тест',
                'long_description': utils.long_text(221)
            }
        }

        advertiser_page = campaign_page.create_campaign_via_catalog_long_long_description(data)
        assert advertiser_page.find_elem_by_locator(
            advertiser_page.locators.CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL
        ) == True

        draft_name = f'Кампания {utils.get_today()}'
        campaign_page.delete_draft(draft_name)
