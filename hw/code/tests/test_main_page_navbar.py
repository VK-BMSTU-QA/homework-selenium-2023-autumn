import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.login_page import LoginPage
from ui.pages.main_page.main_page import MainPage

from selenium.common.exceptions import TimeoutException

HELP_URL = "https://ads.vk.com/help"
COURSES_URL = "https://expert.vk.com/catalog/courses/"
SERTIFICATION_URL = "https://expert.vk.com/certification/"

class TestNavbarMainPage(BaseCase):
    authorize = False

    def test_go_to_news_page(self, main_page: MainPage):
        with self.not_raises():
            main_page.go_to_news_page()

    def test_go_to_usefull_materials_page(self, main_page: MainPage):
        with self.not_raises():
            main_page.go_to_usefull_materials_page()

    def test_go_to_events_page(self, main_page: MainPage):
        with self.not_raises():
            main_page.go_to_events_page()

    def test_go_to_ideas_forum_page(self, main_page: MainPage):
        with self.not_raises():
            main_page.go_to_ideas_forum_page()

    def go_to_monetisation_page(self, main_page: MainPage):
        with self.not_raises():
            main_page.go_to_monetisation_page()

    def test_go_to_help_page(self, main_page: MainPage):
        main_page.go_to_help_page()

        with self.not_raises():
            self.assert_url(HELP_URL)

    def test_go_to_sertification_page(self, main_page: MainPage):
         main_page.go_to_sertification_page()

         with self.not_raises(), self.switch_to_window(self.driver.current_window_handle, True):
            self.assert_url(SERTIFICATION_URL), 

    def test_go_to_courses_page(self, main_page: MainPage):
        main_page.go_to_video_courses_page()

        with self.not_raises(), self.switch_to_window(self.driver.current_window_handle, True):
            self.assert_url(COURSES_URL)


    # @pytest.mark.skip
    # @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
    # def test_login_neg(self, invalid_creds, login_page: LoginPage):
    #     with pytest.raises(TimeoutException):
    #         login_page.login(invalid_creds["user"], invalid_creds["password"])
