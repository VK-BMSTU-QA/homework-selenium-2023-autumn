from ui.pages.lk_page import LKPage
from ui.pages.base_page import BasePage
from ui.locators.login import LoginPageLocators

class LoginPage(BasePage):
    url = "https://ads.vk.com/hq"
    locators = LoginPageLocators

    def login(self, user: str, password: str, timeout=None):
        self.fill(self.locators.LOGIN, user, timeout=timeout)

        self.click(self.locators.LOGIN_GO_ON_BOY_BUTTON, timeout=timeout)

        self.fill(self.locators.PASSWORD, password, timeout=timeout)

        self.click(self.locators.PASSWORD_GO_ON_BOY_BUTTON, timeout=timeout)
        self.close_cookie_banner()

        return LKPage(self.driver)
