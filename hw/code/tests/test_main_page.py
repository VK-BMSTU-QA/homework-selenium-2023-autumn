import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.login_page import LoginPage
from hw.code.ui.pages.main_page.main_page import MainPage

from selenium.common.exceptions import TimeoutException

class TestMainPage(BaseCase):
    authorize = False

    def test_carousel(self, main_page: MainPage):
        banner_txt = main_page.get_slide_text()
        banner_words = banner_txt.split()

        main_page.click_on_know_more()

        found = False
        for word in banner_words:
            if word in self.driver.page_source:
                found = True
        
        assert found, "new page doesnt contain words from banner"
    
    def test_open_all_cases(self, main_page: MainPage):
        with self.not_raises():
            main_page.open_all_cases()
    
    def test_open_news(self, main_page: MainPage):
        with self.not_raises():
            main_page.click_on_top_news()
    
    def test_click_on_vebinars(self, main_page: MainPage):
        with self.not_raises():
            main_page.click_on_vebinars()
            