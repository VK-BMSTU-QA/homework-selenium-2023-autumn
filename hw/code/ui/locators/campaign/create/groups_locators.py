from selenium.webdriver.common.by import By
from ui.locators.campaign.create.basic_locators import CreateCampaignPageLocators


class CreateCampaignGroupsPageLocators(CreateCampaignPageLocators):
    CREATE_CAMPAIGN_GROUPS_CONTINUE_BUTTON = (By.XPATH, "//*[contains(text(), 'Продолжить')]")

    CREATE_CAMPAIGN_GROUPS_SEARCH_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiSearch__input')]")

    CREATE_CAMPAIGN_GROUPS_SEARCH_CHECKBOX = (By.XPATH, "//div[contains(@data-value, '{}')]")

    CREATE_CAMPAIGN_SETTINGS_INCORRECT_REGION_LABEL = (By.XPATH, "//*[contains(text(), 'Не выбраны регионы показа')]")
