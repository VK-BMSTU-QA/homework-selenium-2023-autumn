from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class NewCompanyPageLocators(BasePageLocators):
    SITE_REGION = (By.XPATH, '//*[@data-id="site_conversions"]')
    CATALOG_REGION = (By.XPATH, '//*[@data-id="ecomm"]')
    LEAD_FORM_REGION = (By.XPATH, '//*[@data-id="leadads"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="footer"]//button')
