import pytest
from ui.pages.budget_page import BudgetPage
from base import BaseCase

from selenium.webdriver.remote.webelement import WebElement


class TestSites(BaseCase):
    def test_add_pixel_btn(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.find_element(sites_page.locators.ADD_PIXEL_MODAL)
