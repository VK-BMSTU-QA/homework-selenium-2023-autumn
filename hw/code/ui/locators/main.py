from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN = (By.NAME, "login")
    
    NEWS_PAGE_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Новости']")

    STUDY_NAV_BUTTON = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Обучение']")
    
    USEFULL_MATERIALS_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Полезные материалы']")
    EVENTS_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Мероприятия']")
    VIDEO_COURSES_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Видеокурсы']")
    SERTIFICATIONS_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Сертификация']")

    CASES_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Кейсы']")

    IDEAS_FORUM_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Форум идей']")

    MONETISATION_NAV = (By.XPATH, "//*[contains(@class, 'Navigation') and text()='Монетизация']")

    KNOW_MORE_BUTTONS = (By.XPATH, "*//button//*[text()='Узнать больше']")

    CAROUSEL_TOP_TEXT = (By.XPATH, "//*[contains(@class, 'active')]//*[@id='title']")

    VEBINARS_BUTTON = (By.XPATH, "//*[contains(@class, 'GetStarted')]//*[text='Подробнее']")