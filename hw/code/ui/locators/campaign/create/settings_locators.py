from selenium.webdriver.common.by import By
from ui.locators.campaign.create.basic_locators import CreateCampaignPageLocators


class CreateCampaignSettingsPageLocators(CreateCampaignPageLocators):
    CREATE_CAMPAIGN_SETTINGS_SITE_BUTTON = (By.XPATH, "//div[contains(@data-id, 'site_conversions')]")
    CREATE_CAMPAIGN_SETTINGS_COMMUNITY_BUTTON = (By.XPATH, "//div[contains(@data-id, 'social')]")
    CREATE_CAMPAIGN_SETTINGS_COMMUNITY_ADD_BUTTON = (By.XPATH, "//*[contains(text(), 'Добавить')]")
    CREATE_CAMPAIGN_SETTINGS_CLASSMATES_BUTTON = (By.XPATH, "//div[contains(@data-id, 'odkl')]")
    CREATE_CAMPAIGN_SETTINGS_CLASSMATES_ADD_BUTTON = (By.XPATH, "//*[contains(text(), 'Добавить')]")
    CREATE_CAMPAIGN_SETTINGS_CATALOG_BUTTON = (By.XPATH, "//div[contains(@data-id, 'ecomm')]")
    CREATE_CAMPAIGN_SETTINGS_CATALOG_ADD_BUTTON = (By.XPATH, "//*[contains(text(), 'Добавить')]")
    CREATE_CAMPAIGN_SETTINGS_VK_APPS_BUTTON = (By.XPATH, "//div[contains(@data-id, 'miniapps')]")

    CREATE_CAMPAIGN_SETTINGS_SITE_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    CREATE_CAMPAIGN_SETTINGS_COMMUNITY_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    CREATE_CAMPAIGN_SETTINGS_CLASSMATES_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    CREATE_CAMPAIGN_SETTINGS_BUDGET_INPUT = (By.XPATH, "//input[contains(@data-testid, 'targeting-not-set')]")
    CREATE_CAMPAIGN_SETTINGS_CATALOG_INPUT = (By.XPATH, "//div[contains(@class, 'ModalRoot_componentWrapper__uzHTL')]//input[contains(text(), '')]")
    CREATE_CAMPAIGN_SETTINGS_VK_APPS_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")

    CREATE_CAMPAIGN_SETTINGS_CLASSMATES_OBJECT_POPUP = (By.XPATH, "//div[contains(@class, 'OdklObject_formWrapper__lm8xs')]")
    CREATE_CAMPAIGN_SETTINGS_CLASSMATES_OBJECT_SELECT_POPUP = (By.XPATH, "//*[contains(text(), 'Другая группа')]")
    CREATE_CAMPAIGN_SETTINGS_COMMUNITY_OBJECT_POPUP = (By.XPATH, "//div[contains(@class, 'SelectVkOwner_wrapper__ZauB2')]")
    CREATE_CAMPAIGN_SETTINGS_COMMUNITY_OBJECT_SELECT_POPUP = (By.XPATH, "//*[contains(text(), '4ch')]")
    CREATE_CAMPAIGN_SETTINGS_CATALOG_OBJECT_POPUP = (By.XPATH, "//*[contains(text(), 'Выберите объект')]")
    CREATE_CAMPAIGN_SETTINGS_CATALOG_OBJECT_SELECT_POPUP = (By.XPATH, "//*[contains(text(), 'Другое сообщество')]")
    CREATE_CAMPAIGN_SETTINGS_VK_APPS_OBJECT_POPUP = (By.XPATH, "//div[contains(@class, 'VkMiniAppSelector_wrapper__swue0')]")
    CREATE_CAMPAIGN_SETTINGS_VK_APPS_OBJECT_SELECT_POPUP = (By.XPATH, "//*[contains(text(), 'Game App')]")

    CREATE_CAMPAIGN_SETTINGS_CATALOG_CIRCLE = (By.XPATH, "//*[contains(text(), 'Сообщество ВКонтакте')]")

    CREATE_CAMPAIGN_SETTINGS_EMPTY_URL_LABEL = (By.XPATH, "//*[contains(text(), 'Обязательное поле')]")
    CREATE_CAMPAIGN_SETTINGS_INCORRECT_URL_LABEL = (By.XPATH, "//*[contains(text(), 'Неверный формат URL')]")
    CREATE_CAMPAIGN_SETTINGS_INCORRECT_BUDGET_LABEL = (By.XPATH, "//*[contains(text(), 'Бюджет кампании должен быть не меньше 100₽')]")
