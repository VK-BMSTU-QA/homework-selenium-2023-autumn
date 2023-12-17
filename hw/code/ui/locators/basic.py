from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BANNER_BUTTON = (
        By.XPATH, "//button[contains(@class, 'CookieBanner_button__')]"
    )
    BANNER_BUTTON = (By.CLASS_NAME, 'vkuiIcon--cancel_20')
    
    '''QUERY_LOCATOR = (By.NAME, "q")
    QUERY_LOCATOR_ID = (By.ID, "id-search-field")
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, "start-shell")
    PYTHON_CONSOLE = (By.ID, "hterm:row-nodes")'''
    