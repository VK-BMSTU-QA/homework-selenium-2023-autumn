from selenium.webdriver.common.by import By


class LKPageLocators:

    COMPANIES_TAB_SVG = (
        By.XPATH, '//div[contains(@class, "MenuCell_text__MZJIn")]/span[contains(text(), "Кампании")]'
    )
    COMPANIES_MAIN_PAGE = (
        By.XPATH, '//span[contains(@class, "vkuiHeadline") and text() = "Кампании"]'
    )

    AUDITORIES_TAB_SVG = (
        By.XPATH, '//div[contains(@class, "MenuCell_text__MZJIn")]/span[contains(text(), "Аудитории")]'
    )
    AUDITORIES_MAIN_PAGE = (
        By.XPATH, '//span[contains(@class, "vkuiHeadline") and text() = "Аудитории"]'
    )

    BUDGET_TAB_SVG = (
        By.XPATH, '//span[text() = "Бюджет"]'
    )
    BUDGET_MAIN_PAGE = (
        By.XPATH, '//span[text() = "Транзакции"]'
    )

    TRAINING_TAB_SVG = (
        By.XPATH, '//span[text() = "Обучение"]'
    )
    STARTING_TRAINING_TITLE = (
        By.XPATH, '//h2[text()="С чего начнём обучение?"]'
    )

    COMMERCE_TAB_SVG = (
        By.XPATH, '//span[text() = "Центр коммерции"]'
    )
    CREATE_CATALOG_BUTTON = (
        By.XPATH, "//button[contains(@data-testid, 'create-catalog')]"
    )

    SITES_TAB_SVG = (
        By.XPATH, '//span[text() = "Сайты"]'
    )
    ADD_PIXEL_BUTTON = (
        By.XPATH, '//button[contains(., "Добавить пиксель") and contains(@class, "vkuiButton")]'
    )

    MOBILE_APP_TAB_SVG = (
        By.XPATH, '//span[text() = "Мобильные приложения"]'
    )
    APP_ADD_BUTTON = (
        By.XPATH, '//button[contains(., "Добавить приложение")]'
    )

    LEAD_FORMS_TAB_SVG = (
        By.XPATH, '//span[text() = "Лид-формы"]'
    )
    LEAD_FORMS_CREATE_BUTTON = (
        By.XPATH, '//button[contains(., "Создать лид-форму")]'
    )

    SETTINGS_TAB_SVG = (
        By.XPATH, '//span[text()="Настройки"]'
    )
    GENERAL_SETTINGS_TAB = (
        By.XPATH, '//span[text()="Общие"]'
    )

    HELP_TAB_SVG = (
        By.XPATH, '//span[text()="Помощь"]'
    )
    COMPANY_CASES = (
        By.XPATH, '//span[text()="Кейсы компаний"]'
    )

    WRAP_SIDEBAR = (
        By.XPATH, '//span[text()="Свернуть"]'
    )

