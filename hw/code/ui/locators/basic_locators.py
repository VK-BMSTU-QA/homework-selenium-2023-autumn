from selenium.webdriver.common.by import By


class BasePageLocators:
    MAIN_MOVE_TO_CABINET_BUTTON = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary')]")
