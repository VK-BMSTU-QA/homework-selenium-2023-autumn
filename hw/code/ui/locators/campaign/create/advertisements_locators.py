from selenium.webdriver.common.by import By
from ui.locators.campaign.create.basic_locators import CreateCampaignPageLocators


class CreateCampaignAdvertisementsPageLocators(CreateCampaignPageLocators):
    CREATE_CAMPAIGN_ADVERTISEMENTS_CONTINUE_BUTTON = (By.XPATH, "//*[contains(text(), 'Опубликовать')]")

    CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_INPUT = (By.NAME, "заголовок, макс. 40 символов")
    CREATE_CAMPAIGN_ADVERTISEMENTS_TITLE_CATALOG_INPUT = (By.NAME, "заголовок, макс. 25 символов")

    CREATE_CAMPAIGN_ADVERTISEMENTS_SHORT_DESCRIPTION_INPUT = (By.NAME, "заголовок, макс. 90 символов")
    CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_INPUT = (By.NAME, "Описание 2000 знаков")

    CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_CAROUSEL_INPUT = (By.NAME, "Дескрипшен для карусели, общий")
    CREATE_CAMPAIGN_ADVERTISEMENTS_DESCRIPTION_BANNER_INPUT = (By.NAME, "Описание для динрема")
    CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_DESCRIPTION_INPUT = (By.NAME, "Описание до 220 знаков")
    CREATE_CAMPAIGN_ADVERTISEMENTS_SITE_LONG_DESCRIPTION_INPUT = (By.NAME, "Длинный текст для использования в лентах соцсетей (2000 знаков)")
    CREATE_CAMPAIGN_ADVERTISEMENTS_BUTTON_TEXT_INPUT = (By.NAME, "Доп. заголовок 30 знаков")
    CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiFile__input')]")
    CREATE_CAMPAIGN_ADVERTISEMENTS_CAROUSEL_CARD_INPUT = (By.NAME, "Заголовок слайда динрем карусели")

    CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiFile__input')]")
    CREATE_CAMPAIGN_ADVERTISEMENTS_ADVERTISER_INPUT = (By.NAME, "юридическая информация, макс. 115 символов")

    CREATE_CAMPAIGN_ADVERTISEMENTS_IMAGE_PREVIEW_LABEL = (
        By.XPATH, "//img[contains(@class, 'FirstTemplate_firstImage') and contains(@src, 'r.mradx.net')]",
    )
    CREATE_CAMPAIGN_ADVERTISEMENTS_VIDEO_PREVIEW_LABEL = (
        By.XPATH, "//img[contains(@class, 'MediaContainer_image__HmwFk') and contains(@src, 'ads.vk.com')]",
    )
    CREATE_CAMPAIGN_ADVERTISEMENTS_REQUIRED_LABEL = (By.XPATH, "//*[contains(text(), 'Обязательное поле')]")
    CREATE_CAMPAIGN_ADVERTISEMENTS_LONG_FIELD_LABEL = (By.XPATH, "//*[contains(text(), 'Превышена максимальная длина поля')]")
