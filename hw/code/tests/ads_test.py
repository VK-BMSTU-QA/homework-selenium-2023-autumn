import pytest
import time

from tests.base_case import BaseCase, credentials, AllLinks
from tests.base_case import cookies_and_local_storage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ui.pages.adv_page import AdvPage


class TestGroup(BaseCase):
    authorize = True

    @pytest.fixture(scope="function")
    def get_page(self, adv_page:AdvPage):
        adv_page.get_page()
        yield adv_page
    
    def test_empty_fields(self, get_page: AdvPage):
        get_page.click_continue_button()

        assert get_page.is_on_site("ошибка") or get_page.is_on_site("ошибки")

    def test_more_chars_than_max(self, get_page: AdvPage):
        max_size = get_page.get_title_max()
        get_page.send_text_to_title("слово"*(max_size/5))

        assert get_page.is_on_site("Превышена максимальная длина поля")
        
    def test_latin_symbols(self, get_page: AdvPage):
        get_page.send_text_to_title("word")

        assert get_page.is_on_site("Используйте латиницу только там, где без неё не обойтись")

    def test_wrong_site(self, get_page:AdvPage):
        get_page.send_url('https://labudiduba.com/')

        assert get_page.is_on_site("Ссылка содержит запрещённый редирект на домен")

    # def after_create_company(self, get_page:AdvPage):
        
    #     get_page.select_logo(0).write_to_inputs('https://vk.com/').write_to_textarea('https://vk.com/')


    # Кампании. После создания компании, компания появляется на странице "https://ads.vk.com/hq/dashboard/ad_plans".
# Кампании. Выбрать кампанию, иконка "шестеренки" и выпадающий список "Действия", станут доступны.
# Кампании. Довести кампанию до этапа создания группы, вернуться на "https://ads.vk.com/hq/dashboard/ad_plans", кампания появится в черновиках.
# Кампании. Удалить кампанию, в фильтрах выбрать "Удалённые кампании", кампания появляется на странице.