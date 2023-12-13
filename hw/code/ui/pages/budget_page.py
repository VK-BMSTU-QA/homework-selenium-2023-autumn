from selenium.webdriver.common.by import By

from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class BudgetPage(HqPage):
    url = 'https://ads.vk.com/hq/budget'
    locators = basic_locators.BudgetPageLocators
    min_amount_err_msg = 'минимальная сумма 600,00 ₽'

    def open_pay_modal(self):
        self.click(self.locators.PAY_MODAL_BTN, 2)

    def fill_amount(self, sum):
        self.fill(self.locators.AMOUNT_INPUT, sum)

    def fill_amount_without_vat(self, sum):
        self.fill(self.locators.AMOUNT_WITHOUT_VAT_INPUT, sum)

    def pay(self):
        self.click(self.locators.PAY_BTN)

    def open_range_data_picker(self):
        self.click(self.locators.RANGE_DATA_PICKER_BTN)

