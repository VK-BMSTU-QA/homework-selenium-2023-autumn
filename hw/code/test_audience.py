import pytest
from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):
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

    def test_no_source(self, audience_page):
        audience_page.click(audience_page.locators.CREATE_AUDIENCE_BTN)
        audience_page.is_disabled(audience_page.locators.SAVE_AUDIENCE_BTN)

    def test_too_long_title(self, audience_page):
        audience_page.click(audience_page.locators.CREATE_AUDIENCE_BTN)
        audience_page.fill(audience_page.locators.AUDIENCE_TITLE_INPUT, f'{"a" * 256}')
        audience_page.find_element(audience_page.locators.TITLE_ERROR)

    def test_max_title(self, audience_page):
        audience_page.create_audience('Ключевые фразы', 'маркетинг', title=f'{"a" * 255}')
        audience_page.delete_audience(f'{"a" * 255}')

    def test_create_audience(self, audience_page):
        audience_page.create_audience('Ключевые фразы', 'футбол, баскетбол', title='Тест')
        audience_page.delete_audience('Тест')

    def test_no_keywords(self, audience_page):
        audience_page.click(audience_page.locators.CREATE_AUDIENCE_BTN)
        audience_page.click(audience_page.locators.ADD_SRC_BTN)
        audience_page.click(audience_page.locators.src_by_text('Ключевые фразы'))
        audience_page.is_disabled(audience_page.locators.KEYWORDS_SAVE_BTN)

    def test_only_keywords_filled(self, audience_page):
        audience_page.create_audience('Ключевые фразы', 'маркетинг', title='Тестовая аудитория')
        audience_page.delete_audience('Тестовая аудитория')

    def test_all_fields_filled(self, audience_page):
        audience_page.create_audience('Ключевые фразы', keywords='маркетинг', title='Тестовая аудитория',
                                      keywords_title='Источник', neg_keywords='бизнес')
        audience_page.delete_audience('Тестовая аудитория')

    def test_delete_audience(self, audience_page):
        audience_page.create_audience('Ключевые фразы', 'маркетинг', title='Тестовая аудитория')
        audience_page.delete_audience('Тестовая аудитория')
