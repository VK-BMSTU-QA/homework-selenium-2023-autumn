from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class NewCompanyPageLocators(BasePageLocators):
    SITE_REGION = (By.XPATH, '//*[@data-id="site_conversions"]')
    CATALOG_REGION = (By.XPATH, '//*[@data-id="ecomm"]')
    LEAD_FORM_REGION = (By.XPATH, '//*[@data-id="leadads"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="footer"]//button')

    SITE_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    COST_INPUT = (By.XPATH, '//input[@data-testid="targeting-not-set"]')

    MIN_STRATEGY = (By.XPATH, '//*[contains(text(), "Минимальная цена")]')
    PRED_STRATEGY = (By.XPATH, '//*[contains(text(), "Предельная цена")]')

    SELECTOR_STRATEGY = (By.XPATH, '//*[@data-testid="autobidding-mode"]')
    MAX_CLICK_COST = (By.XPATH, '//*[@data-testid="max-price"]')

    RADIO_BUTTON_VK_GROUP = (
        By.XPATH,
        '//*[contains(text(), "Сообщество ВКонтакте")]',
    )
    VK_ANOTHER_GROUP = (By.XPATH, '//*[contains(text(), "Другое сообщество")]')
    GROUP_SELECTOR = (By.CLASS_NAME, "SelectVkOwner_wrapper__ZauB2")
    VK_INPUT_ANOTHER_GROUP = (
        By.XPATH,
        '//div[@class ="AddGroupModal_inputWrap__MCYuA"]//input',
    )
    ADD_BUTTON_GROUP = (
        By.XPATH,
        '//div[@class ="vkuiModalCardBase__actions"]//button',
    )

    SPLIT_CHECKBOX = (By.XPATH, '//*[contains(text(), "Сплит-тест")]')
    SELECTOR_LEAD = (By.XPATH, '//*[@data-testid="lead-form-select"]')
    SELECT_LEAD_OPTION = (By.CLASS_NAME, "vkuiCustomSelectOption__description")

    DATE_PICKER = (By.XPATH, '//*[@data-testid="end-date"]')
    DATE_LAST_MONTH_BUTTON = (
        By.XPATH,
        '//*[contains(@aria-label, "Предыдущий месяц")]',
    )
    FIRST_DAY = (
        By.XPATH,
        '//*[contains(@class, "vkuiCalendarDay__inner")]/*[text()="1"]',
    )

    ERROR_LESS_THAN_HUN = (
        By.XPATH,
        '//*[contains(text(), "Бюджет кампании должен быть не меньше 100₽")]',
    )

    ERROR_MUST_FIELD = (
        By.XPATH,
        '//*[contains(text(), "Обязательное поле")]',
    )

    ERROR_NOT_FOUND_COM = (
        By.XPATH,
        '//*[contains(text(), "Сообщество не найдено")]',
    )

    ERROR_ALREADY_SELECTED = (
        By.XPATH,
        '//*[contains(text(), "Уже выбрана в другом селекте")]',
    )
