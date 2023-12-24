from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class CreateCampaignPageLocators(BasePageLocators):
    CREATE_CAMPAIGN_CONTINUE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")
    CREATE_CAMPAIGN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")
