from base import BaseCase
from ui.fixtures import main_page, cases_page, webinar_page


class TestWebinar(BaseCase):

    def test_webinar_redirect_click(self, webinar_page):
        webinar = webinar_page.get_webinar_card()
        ref = webinar.get_attribute('href')
        webinar.click()
        assert self.is_url_open(ref)

    def test_back_click_redirect(self, webinar_page):
        webinar = webinar_page.get_webinar_card()
        webinar.click()
        webinar_page.click_back_button()
        assert self.is_url_open(webinar_page.url)

    def test_register_redirect(self, webinar_page):
        webinar = webinar_page.get_webinar_card()
        webinar.click()
        webinar_page.click_register_button()
        assert self.is_url_open('https://expert.vk.com')
