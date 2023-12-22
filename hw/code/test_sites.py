import time

import pytest
from ui.pages.budget_page import BudgetPage
from base import BaseCase

from selenium.webdriver.remote.webelement import WebElement


class TestSites(BaseCase):
    def test_add_pixel_btn(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.find_element(sites_page.locators.ADD_PIXEL_MODAL)

    def test_modal_site_domain(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.click_site_domain_option()
        sites_page.find_element(sites_page.locators.SITE_DOMAIN_INPUT)

    def test_pixel_id(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.click_pixel_id_option()
        sites_page.find_element(sites_page.locators.PIXEL_ID_INPUT)
        sites_page.find_element(sites_page.locators.OWNER_EMAIL_INPUT)

    def test_invalid_domain(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.fill_site_domain('test')
        sites_page.click(sites_page.locators.ADD_PIXEL_BTN)
        sites_page.find_element(sites_page.locators.INVALID_DOMAIN_MSG)

    def test_access_requesting_btn(self, sites_page):
        sites_page.open_add_pixel_modal()
        sites_page.click_pixel_id_option()
        sites_page.fill_pixel_id('')
        sites_page.fill_owner_email('')
        sites_page.is_disabled(sites_page.locators.ACCESS_REQUESTING_BTN)

    def test_pixel_creation(self, sites_page):
        domain = 'test' + str(time.time()) + '.ru'
        sites_page.open_add_pixel_modal()
        sites_page.click_site_domain_option()
        sites_page.fill_site_domain(domain)
        sites_page.click(sites_page.locators.ADD_PIXEL_BTN)
        sites_page.click(sites_page.locators.CLOSE_MODAL_BTN)
        sites_page.find_element(sites_page.locators.pixel_by_domain(domain))

    def test_more_btn(self, sites_page):
        sites_page.open_more_ctx_menu('test.ru')
        sites_page.find_element(sites_page.locators.MORE_CONTEXT_MENU)

    def test_rename_modal_cancel(self, sites_page):
        sites_page.open_more_ctx_menu('test.ru')
        sites_page.click(sites_page.locators.RENAME_DROPDOWN_ITEM)
        sites_page.click(sites_page.locators.RENAME_CANCEL_BTN)
        sites_page.is_invisible(sites_page.locators.RENAME_MODAL, 5)

    def test_rename_modal_change_btn(self, sites_page):
        sites_page.open_more_ctx_menu('test.ru')
        sites_page.click(sites_page.locators.RENAME_DROPDOWN_ITEM)
        sites_page.click(sites_page.locators.RENAME_APPLY_BTN)
        sites_page.is_invisible(sites_page.locators.RENAME_MODAL, 5)

    def test_rename_modal_close_btn(self, sites_page):
        sites_page.open_more_ctx_menu('test.ru')
        sites_page.click(sites_page.locators.RENAME_DROPDOWN_ITEM)
        sites_page.click(sites_page.locators.CLOSE_MODAL_BTN)
        sites_page.is_invisible(sites_page.locators.RENAME_MODAL, 5)

    def test_rename_modal_empty_name(self, sites_page):
        sites_page.open_more_ctx_menu('test.ru')
        sites_page.click(sites_page.locators.RENAME_DROPDOWN_ITEM)
        name_input = sites_page.find_element(sites_page.locators.RENAME_MODAL_NAME_INPUT)
        sites_page.clear_elem(name_input)
        sites_page.fill_pixel_name(' ')
        sites_page.is_disabled(sites_page.locators.RENAME_APPLY_BTN)