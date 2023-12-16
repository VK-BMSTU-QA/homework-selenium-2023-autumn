from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.CLASS_NAME, "vkuiInput__el")
    LOGIN_GO_ON_BOY_BUTTON = (By.CLASS_NAME, 'vkuiButton__content vkuiText vkuiText--sizeY-compact vkuiText--w-2')
    PASSWORD_GO_ON_BOY_BUT = (By.CLASS_NAME, 'vkuiButton vkuiButton--sz-l vkuiButton--lvl-primary vkuiButton--clr-accent vkuiButton--aln-center vkuiButton--sizeY-compact vkuiButton--stretched vkuiTappable vkuiTappable--sizeX-regular vkuiTappable--hasHover vkuiTappable--hasActive vkuiTappable--mouse')
    PASSWORD = (By.CLASS_NAME, 'vkc__TextField__input')

class LKPageLocators:
    pass
