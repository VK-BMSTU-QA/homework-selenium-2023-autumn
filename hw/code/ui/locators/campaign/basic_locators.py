from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class CampaignPageLocators(BasePageLocators):
    MOVE_TO_MAIN_PAGE_BUTTON = (By.XPATH, "//img[contains(@src, '/static/media/logo_ru.df53cbe6.svg')]")
    CAMPAIGN_CREATING_BUTTON = (By.XPATH, "//a[contains(@data-testid, 'create-button')]")
    CAMPAIGN_DRAFTS_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'drafts-button')]")
    CAMPAIGN_DELETE_DRAFT_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'delete-button')]")
    CAMPAIGN_CONFIRM_DELETE_DRAFT_BUTTON = (By.XPATH, "//*[contains(text(), 'Удалить')]")

    CAMPAIGN_LIST = (By.XPATH, "//button[contains(@class, 'nameCellContent_link_')]")

    CAMPAIGN_LIST_CHECKBOX = (By.XPATH, "//div[contains(@class, 'vkuiCheckbox__icon--off')]")

    CAMPAIGN_LIST_OPTIONS_POPUP = (By.XPATH, "//span[contains(@data-testid, 'select-options')]")
    CAMPAIGN_LIST_OPTIONS_SELECT_POPUP = (By.NAME, "actionType")
