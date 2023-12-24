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
    def get_page(self, adv_page: AdvPage):
        yield adv_page.get_page()

    def test_empty_fields(self, get_page: AdvPage):
        get_page.click_continue_button()

        assert get_page.is_on_site_text("ошибк")

    def test_more_chars_than_max(self, get_page: AdvPage):
        max_size = get_page.get_title_max()

        get_page.send_text_to_title(
            "слово" * (max_size // 5 + 1)
        ).click_continue_button()

        assert get_page.is_on_site_text("Превышена максимальная длина поля")

    def test_latin_symbols(self, get_page: AdvPage):
        get_page.send_text_to_title("word")

        assert get_page.is_on_site_text(
            "Используйте латиницу только там, где без неё не обойтись"
        )

    def test_wrong_site(self, get_page: AdvPage):
        get_page.send_url("https://labudiduba.com/")

        assert get_page.is_on_site_text("Ссылка содержит запрещённый редирект на домен")

    def test_after_create_company(self, get_page: AdvPage):
        get_page.select_logo(0).write_to_inputs("https://vk.com/").write_to_textarea(
            "https://vk.com/"
        )
        name = get_page.get_company_name()

        get_page.click_media_upload().select_media_options().add_media_option()
        get_page.click_continue_button().click_send_button(10)

        assert get_page.is_on_site_text(name, 5)
