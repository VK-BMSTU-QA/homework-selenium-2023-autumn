import pytest
from ui.pages.budget_page import BudgetPage
from base import BaseCase

from selenium.webdriver.remote.webelement import WebElement
class TestBudget(BaseCase):
    def test_pay_btn(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.find(BudgetPage.locators.PAY_MODAL)

    def test_min_amount_sum(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.fill_amount('100')
        budget_page.find(budget_page.locators.MIN_AMOUNT_ERR_MSG)

    def test_min_amount_without_vat_sum(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.find(budget_page.locators.PAY_BTN)

    def test_amount_without_vat_calculating(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.fill_amount('600')
        amount_without_vat = budget_page.find(budget_page.locators.AMOUNT_WITHOUT_VAT_INPUT).get_attribute('value')
        assert amount_without_vat == '500 ₽'

    def test_amount__calculating(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.fill_amount_without_vat('500')
        amount_without_vat = budget_page.find(budget_page.locators.AMOUNT_INPUT).get_attribute('value')
        assert amount_without_vat == '600 ₽'

    def test_valid_amount_fill(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.fill_amount('600')
        budget_page.click(budget_page.locators.PAY_BTN)
        budget_page.find(budget_page.locators.PAYMENT_METHOD_FORM)

    def test_valid_amount_without_vat_fill(self, budget_page):
        budget_page.open_pay_modal()
        budget_page.fill_amount_without_vat('500')
        budget_page.click(budget_page.locators.PAY_BTN)
        budget_page.find(budget_page.locators.PAYMENT_METHOD_FORM)

    def test_range_data_picker_btn(self, budget_page):
        budget_page.open_range_data_picker()
        budget_page.find(budget_page.locators.RANGE_DATA_PICKER_WIDGET)


