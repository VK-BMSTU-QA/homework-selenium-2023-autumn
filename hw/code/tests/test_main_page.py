import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.login_page import LoginPage
from ui.pages.main_page.main_page import MainPage

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
        
        assert found == True, "new page doesnt contain words from banner"
        