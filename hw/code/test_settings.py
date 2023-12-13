from base import BaseCase
from ui.fixtures import *
from ui.pages.campaign_page import CampaignPage
from ui.pages.settings_page import SettingsPage, SettingsNotificationsPage, SettingsAccessPage, SettingsLogsPage


INCORRECT_PHONE_NUMBER = 'Некорректный номер телефона'
REQUIRED_FILED = 'Обязательное поле'
INCORRECT_INN = 'Некорректный ИНН'
INN_LENGTH_ERROR = 'Длина ИНН должна быть 12 символов'

class TestSettings(BaseCase):
    @staticmethod
    def get_account_data():
        return {
            'phone': '+79000000000', 
            'fio': 'Тестов Тест Тестович',
            'inn': '112329166348'
        }

    @allure.story('Edit account info (positive)')
    def test_edit_account_info_positive(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('settings')
        settings_page = SettingsPage(self.driver)
        data = self.get_account_data()

        settings_page.edit_account_info(data)
        self.driver.refresh()
        assert data == settings_page.get_account_info()

    @allure.story('Edit account info (negative)')
    def test_edit_account_info_negative(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('settings')
        settings_page = SettingsPage(self.driver)

        invalid_data = [
            {'files': {'phone': 'test', 'fio': 'Тестов Тест Тестович', 'inn': '112329166348'}, 'error': INCORRECT_PHONE_NUMBER},
            {'files': {'phone': '+7900000', 'fio': 'Тестов Тест Тестович', 'inn': '112329166348'}, 'error': INCORRECT_PHONE_NUMBER},
            {'files': {'phone': '+79000000000', 'fio': '', 'inn': '112329166348'}, 'error': REQUIRED_FILED},
            {'files': {'phone': '+79000000000', 'fio': 'Тестов Тест Тестович', 'inn': ''}, 'error': REQUIRED_FILED},
            {'files': {'phone': '+79000000000', 'fio': 'Тестов Тест Тестович', 'inn': 'test'}, 'error': INCORRECT_INN},
            {'files': {'phone': '+79000000000', 'fio': 'Тестов Тест Тестович', 'inn': '52'}, 'error': INN_LENGTH_ERROR},
        ]

        for data in invalid_data:
            settings_page.edit_account_info(data['files'])
            assert data['error'] in settings_page.get_inner_html_of_form()
            self.driver.refresh()

    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('common', SettingsPage),
            pytest.param('notifications', SettingsNotificationsPage),
            pytest.param('access', SettingsAccessPage),
            pytest.param('logs', SettingsLogsPage),
        ]
    )
    @allure.story('Open section {to_section}')
    def test_open_section(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('settings')
        settings_page = SettingsPage(self.driver)
        settings_page.open_section(to_section)
        assert page(self.driver).is_opened()
