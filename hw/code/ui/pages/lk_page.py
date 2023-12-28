from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.lk import LKPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LKPage(BasePage):
    url = "https://ads.vk.com/hq"
    locators = LKPageLocators

    def switch_tab(self, tab, timeout=None):
        match tab:
            case "Кампании":
                return self.click(self.locators.COMPANIES_TAB_SVG, timeout)
            case "Аудитории":
                return self.click(self.locators.AUDITORIES_TAB_SVG, timeout)
            case "Бюджет":
                return self.click(self.locators.BUDGET_TAB_SVG, timeout)
            case "Обучение":
                return self.click(self.locators.TRAINING_TAB_SVG, timeout)
            case "Центр коммерции":
                return self.click(self.locators.COMMERCE_TAB_SVG, timeout)
            case "Сайты":
                return self.click(self.locators.SITES_TAB_SVG, timeout)
            case "Мобильные приложения":
                return self.click(self.locators.MOBILE_APP_TAB_SVG, timeout)
            case "Лид-формы":
                return self.click(self.locators.LEAD_FORMS_TAB_SVG, timeout)
            case "Настройки":
                return self.click(self.locators.SETTINGS_TAB_SVG, timeout)
            case "Помощь":
                return self.click(self.locators.HELP_TAB_SVG, timeout)

    def check_tab_switched(self, tab, timeout=None) -> bool:
        match tab:
            case "Кампании":
                return (
                    self.find(self.locators.COMPANIES_MAIN_PAGE, timeout)
                    is not None
                )
            case "Аудитории":
                return (
                    self.find(self.locators.AUDITORIES_MAIN_PAGE, timeout)
                    is not None
                )
            case "Бюджет":
                return (
                    self.find(self.locators.BUDGET_MAIN_PAGE, timeout)
                    is not None
                )
            case "Обучение":
                return (
                    self.find(self.locators.STARTING_TRAINING_TITLE, timeout)
                    is not None
                )
            case "Центр коммерции":
                return (
                    self.find(self.locators.CREATE_CATALOG_BUTTON, timeout)
                    is not None
                )
            case "Сайты":
                return (
                    self.find(self.locators.ADD_PIXEL_BUTTON, timeout)
                    is not None
                )
            case "Мобильные приложения":
                return (
                    self.find(self.locators.APP_ADD_BUTTON, timeout)
                    is not None
                )
            case "Лид-формы":
                return (
                    self.find(self.locators.LEAD_FORMS_CREATE_BUTTON, timeout)
                    is not None
                )
            case "Настройки":
                return (
                    self.find(self.locators.GENERAL_SETTINGS_TAB, timeout)
                    is not None
                )
            case "Помощь":
                return (
                    self.find(self.locators.COMPANY_CASES, timeout) is not None
                )

        return False

    def click_on_wrap(self, timeout=None):
        self.click(self.locators.WRAP_SIDEBAR, timeout)

    def found_redirect_titles(self, timeout=None) -> bool:
        try:
            self.find(self.locators.COMPANIES_TAB_SVG, timeout)
            return True
        except TimeoutException:
            return False
