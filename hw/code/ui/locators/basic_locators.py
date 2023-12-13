from selenium.webdriver.common.by import By


class BasePageLocators:
    FOOTER_ABOUT = (By.XPATH, "//a[contains(@class, 'Footer_about')]")
    FOOTER_LOGO_VK_BUSINESS = (By.LINK_TEXT, "//a[contains(@href, 'https://vk.company/ru/company/business/')]")
    FOOTER_BUTTON_CABINET = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary')]")
    FOOTER_CONTROL = (By.XPATH, "//div[contains(@class, 'SelectLanguage_wrapper')]")
    FOOTER_ITEMS = (By.XPATH, "//li[contains(@class, 'Footer_item_')]")
    FOOTER_NEWS = (By.XPATH, "//a[contains(@href, '/news')]")
    HELP_ITEMS_LOCATOR = (By.XPATH, "//a[contains(@class, 'CategoryCard_wrapper')]")
    MONETIZATION_ITEMS_LOCATOR = (By.XPATH, "//div[contains(@class, 'Slider_title')]")
    MONETIZATION_TOGGLE_LOCATOR = (By.XPATH, "//button[contains(@class, 'Tabs_tab')]")
    MONETIZATION_NAME_LOCATOR = (By.ID, "name")
    MONETIZATION_EMAIL_LOCATOR = (By.ID, "email")
    MONETIZATION_FORM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'Form_button')]")
    MONETIZATION_FORM_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'Form_success')]")


class MonetizationPageLocators(BasePageLocators):
    MONETIZATION_TOGGLE_LOCATOR = (By.XPATH, "//button[contains(@class, 'Tabs_tab')]")
    MONETIZATION_NAME_LOCATOR = (By.ID, "name")
    MONETIZATION_EMAIL_LOCATOR = (By.ID, "email")
    MONETIZATION_FORM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'Form_button')]")
    MONETIZATION_FORM_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'Form_success')]")


class HelpPageLocators(BasePageLocators):
    HELP_ITEMS_LOCATOR = (By.XPATH, "//a[contains(@class, 'CategoryCard_wrapper')]")


class LoginPageLocators(BasePageLocators):
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//a[contains(@class, 'ButtonCabinet')]")
    OAUTH_MAIL_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")

    EMAIL_LOCATOR = (By.NAME, "username")
    ENTER_PASSWORD_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    RECAPTCHA_BTN_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'recaptcha-inter-next')]")


class RegistrationPageLocators(BasePageLocators):
    CREATE_CABINET_LOCATOR = (By.ID, "click-createNewButton")
    EMAIL_LOCATOR = (By.NAME, "email")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'create-button')]")
    SWITCH_ACCOUNT_LOCATOR = (By.XPATH, "//div[contains(@class, 'AccountSwitch_changeAccountName')]")
    AC_TYPES_CHECKBOX_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiRadio__container')]")
    AC_TYPES_LOCATOR = (By.XPATH, "//span[contains(@class, 'registration_itemWitContextHelpText')]")
    PHYS_AC_TYPE_LOCATOR = (By.XPATH,"//span[.='Физическое лицо']")
    ACCEPT_RULES_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiCheckbox__icon')]")
    BOTTOM_ERROR_LOCATOR = (By.XPATH, "//span[contains(@class, 'vkuiFormItem__bottom')]")


class BasePageAuthorizedLocators(BasePageLocators):
    CAMPAIGN_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'dashboardV2')]")
    AUDIENCE_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'audience')]")
    BUDGET_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'budget')]")
    ECOMM_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'catalogs')]")
    SITE_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'pixels')]")
    MOBAPP_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'mobApps')]")
    LEADAD_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'leadads')]")
    SETTINGS_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'settings')]")


class CampaignPageLocators(BasePageLocators):
    ONBOARDING_LOCATOR = (By.XPATH, "//div[contains(@class, 'ModalManagerPage_modalContent')]")
    ONBOARDING_CLOSE_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiModalDismissButton')]")
    HELP_LOCATOR = (By.XPATH, "//div[contains(@class, 'Content_container_')]")
    HELP_CLOSE_LOCATOR = (By.XPATH, "//button[contains(@class, 'CloseButton_wrapper_')]")

    START_CREATING_CAMPAIGN = (By.XPATH, "//a[contains(@data-testid, 'create-button')]")
    CAMPAIGN_LOCATOR = (By.XPATH, "//button[contains(@class, 'nameCellContent_link_')]")
    CHECHBOX_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiCheckbox__icon--off')]")
    OPTIONS_LOCATOR = (By.XPATH, "//span[contains(@data-testid, 'select-options')]")
    SELECT_OPTIONS_LOCATOR = (By.NAME, "actionType")

    CAMPAIGNS_SECTION_LOCATOR = (By.ID, 'dashboardV2.plans')
    GROUPS_SECTION_LOCATOR = (By.ID, 'dashboardV2.groups')
    ADS_SECTION_LOCATOR = (By.ID, 'dashboardV2.ads')


class CampaignSettingsPageLocators(CampaignPageLocators):
    SITE_LOCATOR = (By.XPATH, "//div[contains(@data-id, 'site_conversions')]")
    SITE_MODAL_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'object')]")
    SITE_FIELD_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    BUDGET_MODAL_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'budget')]")
    BUDGET_FIELD_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'targeting-not-set')]")
    FOOTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'CreateFooter_footer_')]")
    CONTINUE_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class GroupPageLocators(CampaignPageLocators):
    pass


class AddGroupPageLocators(GroupPageLocators):
    SEARCH_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiSearch__input')]")
    CHECKBOX_LOCATOR = (By.XPATH, "//div[contains(@data-value, '{}')]")
    CONTINUE_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class AdvertisementPageLocators(CampaignPageLocators):
    pass


class AddAdvertisementPageLocators(AdvertisementPageLocators):
    TITLE_LOCATOR = (By.NAME, "заголовок, макс. 40 символов")
    SHORT_DESCRIPTION_LOCATOR = (By.NAME, "заголовок, макс. 90 символов")
    IMAGE_INPUT_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiFile__input')]")
    PREVIEW_LOCATOR = (
        By.XPATH, "//img[contains(@class, 'FirstTemplate_firstImage') and contains(@src, 'r.mradx.net')]")

    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class AudiencePageLocators(BasePageLocators):
    START_CREATING_AUDIENCE = (By.XPATH, "//button[contains(@data-testid, 'create-audience')]")
    TITLE_AUDIENCE_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    ADD_SOURCE_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'vkuiButton--stretched') and contains(@class, 'vkuiButton--mode-secondary')]")
    SOURCE_LOCATOR = (By.XPATH, "//div[contains(@tabindex, '0') and contains(@role, 'button')]")
    KEYWORDS_LOCATOR = (By.XPATH, "//textarea[contains(@class, 'vkuiTextarea__el')]")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")
    MODAL_WINDOW_LOCATOR = (By.XPATH, "//div[contains(@class, 'ModalRoot_componentWrapper')]")

    AUDIENCE_TITLE_LOCATOR = (By.XPATH, "//h5[contains(@class, 'NameCell_name_')]")
    AUDIENCE_OPTIONS_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'audience-item-menu')]")
    DELETE_AUDIENCE_LOCATOR = (By.XPATH, "//label[contains(@data-testid, 'dropdown-item')]")
    CONFIRM_DELETE_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--appearance-negative')]")

    AUDIENCES_SECTION_LOCATOR = (By.ID, 'tab_audience')
    USERS_SECTION_LOCATOR = (By.ID, 'tab_audience.users_list')


class AudienceUsersPageLocators(AudiencePageLocators):
    pass


class BudgetPageLocators(BasePageLocators):
    pass


class ECommPageLocators(BasePageLocators):
    pass


class SitesPageLocators(BasePageLocators):
    SITES_LOCATOR = (By.XPATH, "//a[contains(@data-route, 'pixels')]")
    PIXEL_MODAL_LOCATOR = (By.XPATH, "//div[contains(@id, '_modal_')]")
    ADD_PIXEL_BUTTON_MAIN_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--stretched')]")
    ADD_PIXEL_BUTTON_LOCATOR = (By.XPATH,
                                "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--appearance-accent')]")
    PIXEL_DOMAIN_FIELD_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    MORE_PIXEL_BUTTON_LOCATOR = (
        By.XPATH, "//button[contains(@class, 'PixelMoreCell_moreButton') and contains(@class, 'vkuiIconButton')]")
    PIXEL_CONFIRMATION_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiModalPage__in')]")
    CREATE_NEW_PIXEL_LOCATOR = (By.XPATH, "//span[.='Создать новый пиксель']")
    CLOSE_CREATE_PIXEL_LOCATOR = (By.XPATH, "//div[contains(@aria-label, 'Закрыть')]")
    DELETE_PIXEL_LOCATOR = (By.XPATH, "//span[.='Удалить пиксель']")
    CONFIRM_DELETE_PIXEL_LOCATOR = (By.XPATH, "//span[.='Удалить']")
    PIXEL_LIST_LOCATOR = (By.ID, "pixels")
    PIXEL_FORMAT_LOCATOR = (By.XPATH, "//a[contains(@href, '{}')]")


class MobAppsPageLocators(BasePageLocators):
    pass


class LeadAdsPageLocators(BasePageLocators):
    pass


class SettingsLocators(BasePageLocators):
    DELETE_ACCOUNT_LOCATOR = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    MODAL_ACTIONS_DELETE_ACCOUNT = (By.XPATH, "//div[contains(@class, 'DeleteAccountConfirmModal_actions')]")
    CONFIRM_DELETE_ACCOUNT = (By.XPATH,
                              "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--appearance-negative')]")

    PHONE_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'general-phone')]")
    FIO_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'general-ord-name')]")
    INN_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'general-ord-inn')]")
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'settings-save')]")

    COMMON_SECTION_LOCATOR = (By.ID, 'tab-settings')
    NOTIFICATIONS_SECTION_LOCATOR = (By.ID, 'tab-settings.notifications')
    ACCESS_SECTION_LOCATOR = (By.ID, 'tab-settings.access')
    LOGS_SECTION_LOCATOR = (By.ID, 'tab-settings.logs')

    FORM_LOCATOR = (By.XPATH, "//form[contains(@class, 'General_container_')]")


class SettingsNotificationsLocators(SettingsLocators):
    pass


class SettingsAccessLocators(SettingsLocators):
    pass


class SettingsLogsLocators(SettingsLocators):
    pass


class MainPageLocators(BasePageLocators):
    LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'HeaderLeft_home')]")
    NEWS_LOCATOR = (By.XPATH, "//a[contains(@href, '/news')]")
    CASES_LOCATOR = (By.XPATH, "//a[contains(@href, '/cases')]")
    FORUM_LOCATOR = (By.XPATH, "//a[contains(@href, '/upvote')]")
    MONETIZATION_LOCATOR = (By.XPATH, "//a[contains(@href, '/partner')]")
    HELP_LOCATOR = (By.XPATH, "//a[contains(@href, '/help')]")
    CABINET_LOCATOR = (By.XPATH, "//a[contains(@href, '/hq/dashboard')]")

    ACCEPT_COOKIE_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'cookie-banner-button-vkads')]")
    FOOTER_ITEM_LOCATOR = (By.XPATH, "//li[contains(@class, 'Footer_item_')]")


class NewsPageLocators(BasePageLocators):
    pass


class CasesPageLocators(BasePageLocators):
    pass


class NewsPageLocatorsFooter(MainPageLocators):
    pass


class EventsPageLocators(MainPageLocators):
    pass


class DocumentsPageLocators(MainPageLocators):
    pass


class MonetizationFooterPageLocators(MainPageLocators):
    pass


class ExpertPageLocators(MainPageLocators):
    pass


class HelpAuthorizationPageLocators(HelpPageLocators):
    pass


class HelpGeneralPageLocators(HelpPageLocators):
    pass


class HelpFeaturesPageLocators(HelpPageLocators):
    pass


class HelpMiniAdsPageLocators(HelpPageLocators):
    pass


class HelpStatisticsPageLocators(HelpPageLocators):
    pass


class HelpDocumentsPageLocators(HelpPageLocators):
    pass


class ForumPageLocators(BasePageLocators):
    pass


class HelpPageLocators(BasePageLocators):
    pass


class OauthPageLocators(BasePageLocators):
    pass


class InsightsPageLocators(MainPageLocators):
    pass
