from selenium.webdriver.common.by import By


class BasePageLocators:
    GO_TO_CABINET_BTN = (By.XPATH, "//*[contains(@class, 'ButtonCabinet_primary')]")
    OPTIONS = (By.XPATH, f"//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")

    @staticmethod
    def by_css_selector(selector, id):
        return By.CSS_SELECTOR, f"[{selector}='{id}']"

    @staticmethod
    def by_option(text):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']"


class LoginPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BTN = BasePageLocators.by_css_selector('data-test-id', 'oAuthService_mail_ru')
    MAIL_RU_LOGIN_INPUT = (By.NAME, 'username')
    MAIL_RU_ENTER_PASSWORD_BTN = BasePageLocators.by_css_selector('data-test-id', 'next-button')
    MAIL_RU_PASSWORD_INPUT = (By.NAME, 'password')
    MAIL_RU_SUBMIT_BTN = BasePageLocators.by_css_selector('data-test-id', 'submit-button')


class RegistrationPageLocators(BasePageLocators):
    CREATE_CABINET_BTN = BasePageLocators.by_css_selector('data-testid', 'create-new')
    AVATAR_BTN = (By.XPATH, "//*[contains(@class, 'userMenu_avatar')]")
    LOGOUT_BTN = (By.XPATH, "//*[contains(@class, 'userMenu_logoutButton')]")
    RU_TAB = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')][contains(., 'Русский')]")
    EN_TAB = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')][contains(., 'English')]")


class CreateCabinetPageLocators(BasePageLocators):
    AGENCY_RADIO = (By.XPATH, f".//*[text()='Агентство']")
    PHYSICAL_RADIO = BasePageLocators.by_css_selector('data-testid', 'physical')
    COUNTRY_SELECT = BasePageLocators.by_css_selector('data-testid', 'country')
    CURRENCY_SELECT = BasePageLocators.by_css_selector('data-testid', 'currency')
    EMAIL_FIELD = BasePageLocators.by_css_selector('data-testid', 'email')
    TERMS_CHECK = (By.CLASS_NAME, "registration_offerTitle__BqyqW")
    SUBMIT_BTN = BasePageLocators.by_css_selector('data-testid', 'create-button')
    EMAIL_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    TERMS_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    FORM_ERROR = (By.CLASS_NAME, 'vkuiFormStatus--mode-error')


class HqPageLocators(BasePageLocators):
    CLOSE_EDU_MODAL_BTN = (By.XPATH, "//button[contains(., 'Попробовать позже')]")
    CLOSE_EDU_HINT_BTN = BasePageLocators.by_css_selector('aria-label', 'close')


class AudiencePageLocators(BasePageLocators):
    # Navigate
    AUDIENCE_TAB = (By.ID, 'tab_audience')
    USERS_TAB = (By.ID, 'tab_audience.users_list')

    # Create
    CREATE_AUDIENCE_BTN = BasePageLocators.by_css_selector('data-testid', 'create-audience')
    AUDIENCE_TITLE_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    ADD_SRC_BTN = (By.XPATH, "//button[contains(., 'Добавить источник')]")

    KEYWORDS_TITLE_INPUT = (By.XPATH,
                            "//div[contains(@class, 'ModalRoot_overlay')][contains(., 'Ключевые фразы')]//input")
    KEYWORDS_INPUT = (By.XPATH, "//*[not(contains(@class, 'KeyPhrases_negationPhrases'))]/*/textarea")
    NEG_KEYWORDS_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_row')]/*/textarea")
    KEYWORDS_SAVE_BTN = (By.XPATH,
                         "//div[contains(@class, 'ModalRoot_overlay')][contains(., 'Ключевые фразы')]//button[contains(., 'Сохранить')]")
    SAVE_AUDIENCE_BTN = (By.XPATH, "//button[contains(., 'Сохранить')]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'ModalRoot_overlay')]")

    TITLE_ERROR = (By.XPATH, "//*[contains(@class, 'vkuiFootnote')][text()='Максимальная длина 255 символов']")

    # Delete
    AUDIENCE_OPTION = (By.XPATH, "//label[contains(@data-testid, 'dropdown-item')]")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(., 'Удалить')]")

    @staticmethod
    def src_by_text(text):
        return By.XPATH, f"//div[contains(@class, 'vkuiSimpleCell')][contains(., '{text}')]"

    @staticmethod
    def audience_details_btn_by_name(name):
        return By.XPATH, f"//div[contains(@class, 'NameCell_wrapper')][contains(., '{name}')]//button[contains(@data-testid, 'audience-item-menu')]"


class SettingsPageLocators(BasePageLocators):
    # Navigate
    GENERAL_TAB = (By.ID, 'tab-settings')
    NOTIFICATIONS_TAB = (By.ID, 'tab-settings.notifications')
    ACCESS_TAB = (By.ID, 'tab-settings.access')
    HISTORY_TAB = (By.ID, 'tab-settings.logs')

    PHONE_INPUT = (By.XPATH, "//*[contains(@data-testid, 'general-phone')]")
    FIO_INPUT = BasePageLocators.by_css_selector('data-testid', 'general-ord-name')
    INN_INPUT = BasePageLocators.by_css_selector('data-testid', 'general-ord-inn')
    FORM_CONTROL_BTNS = (By.XPATH, "//*[contains(@class, 'FormControls_buttons')]")
    SAVE_BTN = (By.XPATH, "//button[contains(@data-testid, 'settings-save')]")

    PHONE_INVALID_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFootnote')][contains(., 'Некорректный номер телефона')]")
    PHONE_MIN_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFootnote')][contains(., 'Телефон не может быть короче 12 цифр')]")
    FIO_INVALID_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ФИО')][contains(., 'Значение не может содержать только пробелы')]")
    FIO_INVALID_CHARS_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ФИО')][contains(., 'Некорректные символы. Разрешена только кириллица дефис и пробел')]")
    INN_INVALID_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFormItem')][contains(., 'ИНН')][contains(., 'Некорректный ИНН')]")
    INN_TOO_SHORT_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ИНН')][contains(., 'Длина ИНН должна быть 12 символов')]")

    # Delete cabinet
    DELETE_CABINET_BTN = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    CONFIRM_DELETE_CABINET_BTN = (By.XPATH, "//button[contains(., 'Да, удалить')]")


class SettingsNotificationsPageLocators(BasePageLocators):
    NOTIFICATION_ENABLE_BTN = (By.XPATH, "//*[contains(@class, 'Emails_item')]//*[contains(@class, 'vkuiSwitch')]")
    WARNING_HINT = (By.XPATH, "//*[contains(@class, 'Warning_warning')]")
    SAVE_PANEL = (By.XPATH, "//*[contains(@class, 'Notifications_bottom')]")

    SAVE_BTN = (By.XPATH, "//button[contains(@data-testid, 'settings-save')]")

    @staticmethod
    def checkbox_by_name(name):
        return By.XPATH, f"//label[contains(@class, 'vkuiCheckbox')][contains(., '{name}')]//input"

    @staticmethod
    def item_by_name(name):
        return By.XPATH, f"//label[contains(@class, 'vkuiCheckbox')][contains(., '{name}')]"


class CampaignPageLocators:
    CAMPAIGN_TAB = (By.ID, 'dashboardV2.plans')
    GROUPS_TAB = (By.ID, 'dashboardV2.groups')
    ADS_TAB = (By.ID, 'dashboardV2.ads')
    CAMPAIGN_CREATION_BTN = BasePageLocators.by_css_selector('data-testid', 'create-button')
    CLOSE_EDU_MODAL_BTN = (By.XPATH, "//button[contains(., 'Попробовать позже')]")
    CLOSE_EDU_HINT_BTN = BasePageLocators.by_css_selector('aria-label', 'close')
    FILTER_BTN = (By.XPATH, "//button[contains(., 'Фильтр')]")
    FILTER_FORM = (
        By.XPATH, "//div[contains(@class, 'Tooltip_tooltipContainer__P1b-O') and contains(., 'Новый фильтр')]")
    RANGE_DATA_PICKER_WIDGET = (By.XPATH, "//div[contains(@class, 'RangeDatePicker')]")
    RANGE_DATA_BTN = BasePageLocators.by_css_selector('data-testid', 'filter-data-picker')
    SEARCH_INPUT = BasePageLocators.by_css_selector('name', 'filter-search-input')
    SETTINGS_BTN = (By.CLASS_NAME, 'TableSettings_settingsButton__uz8xK')
    DOWNLOAD_BTN = (By.CLASS_NAME, 'tableActions_downloadButton__Kuuoy')
    SETTINGS_CONTEXT_MENU = (By.XPATH, "//div[contains(@class, 'vkuiPopper') and contains(., 'Настроить столбцы')]")
    DOWNLOAD_CONTEXT_MENU = (By.XPATH, "//div[contains(@class, 'vkuiPopper') and contains(., 'Итоговый отчет')]")

    @staticmethod
    def search_bage(query):
        return By.XPATH, f"//div[contains(@class, vkuiChip) and contains(., {query})]"


class CampaignCreationPageLocators(BasePageLocators):
    CAMPAIGN_SECTION_TITLE = (By.CLASS_NAME, 'PlanForm_title__wffcf')
    CAMPAIGN_SECTION_TITLE_INPUT = (By.CLASS_NAME, 'EditableTitle_input__cq0UF')
    DELETE_CAMPAIGN_OPTION = (By.XPATH, "//label[contains(., 'Удалить')]")
    MORE_OPTION_BTN = BasePageLocators.by_css_selector('aria-label', 'More')
    MORE_CONTEXT_MENU = (By.XPATH, "//div[contains(@class, 'vkuiPopper')]")
    SITE_OPTION = BasePageLocators.by_css_selector('data-id', 'site_conversions')
    SITE_DOMAIN_INPUT = (
        By.XPATH, "//div[contains(., 'Рекламируемый сайт') and contains(@class, 'vkuiFormItem')]/span/input")
    CONTINUE_BTN = (By.XPATH, "//button[contains(., 'Продолжить')]")
    BUDGET_INPUT = BasePageLocators.by_css_selector('data-testid', 'targeting-not-set')
    MIN_BUDGET_MSG = (By.XPATH,
                      "//span[contains(@class, 'vkuiFormItem__bottom') and contains(., 'Бюджет кампании должен быть не меньше 100₽')]")
    FOOTER_ERROR_BTN = (By.XPATH, "//button[contains(@class, 'ErrorsTooltip_button__YyIDS')]")
    REGIONS_COUNTER = (By.CLASS_NAME, 'RegionsSelector_selectedRegionsCount__LWBfS')
    DEMOGRAPHY_SECTION = BasePageLocators.by_css_selector('data-testid', 'section-demography')
    DEVICES_SECTION = BasePageLocators.by_css_selector('data-testid', 'section-devices')
    URL_PARAMS_SECTION = BasePageLocators.by_css_selector('data-testid', 'section-urlUtm')
    URL_MANUAL_LABEL_OPTION = (
        By.XPATH, "//label[contains(@class, 'vkuiRadio') and contains(., 'Добавлять UTM-метки вручную')]")
    URL_PARAMS_REQUIRED_FIELD_MSG = (By.XPATH,
                                     "//section[contains(@data-testid, 'section-urlUtm')]//span[contains(@class, 'vkuiFormItem__bottom') and contains(., 'Обязательное поле')]")
    INCORRECT_UTM_LABEL_FORMAT_MSG = (By.XPATH,
                                      "//section[contains(@data-testid, 'section-urlUtm')]//span[contains(@class, 'vkuiFormItem__bottom') and contains(., 'Неверный формат utm-метки')]")
    UTM_LABEL_INPUT = (By.XPATH, "//span[contains(@class, 'UrlUtm_textarea__QsCLz')]//textarea")
    PLACEMENT_SECTION = BasePageLocators.by_css_selector('data-testid', 'section-placement')
    PLACEMENT_SWITCH = (
        By.XPATH, "//section[contains(@data-testid, 'section-placement')]//label[contains(@class, 'vkuiSwitch')]")
    PLACEMENT_LIST = (
        By.XPATH,
        "//section[contains(@data-testid, 'section-placement')]//div[contains(@class, 'composite_unit__1W0jc')]")
    AD_SECTION_TITLE = (By.CLASS_NAME, 'EditableTitle_container__l9GP0')
    AD_SECTION_TITLE_INPUT = (By.CLASS_NAME, 'EditableTitle_input__cq0UF')
    TITLE_INPUT = (By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Заголовок')]//input")
    SHORT_DESCRIPTION_INPUT = (
        By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Короткое описание')]//textarea")
    LONG_DESCRIPTION_INPUT = (
        By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Длинное описание')]//textarea")
    BTN_TEXT_INPUT = (
        By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Текст рядом с кнопкой')]//input")
    ADVERTISER_DATA_INPUT = (
        By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Данные рекламодателя')]//textarea")
    SITE_LINK_INPUT = (
        By.XPATH, "//div[contains(@class, 'vkuiFormItem') and contains(., 'Ссылка на сайт')]//input")
    NATIVE_BLOCK_BTN = (By.XPATH, "//button[contains(@data-value, 'native')]")
    SET_LOGO_BTN = (By.XPATH, "//button[contains(., 'Выбрать логотип')]")
    LOADER = (By.CLASS_NAME, 'Loading_loading__o-t1B')
    LOGO_IMG = (By.XPATH, "//div[contains(@class, 'ImageItems_imageItem__jdlt3') and contains(., 'emblem.png')]")
    PREVIEW_IMG = (By.XPATH, "//div[contains(@class, 'ImageItems_imageItem__jdlt3') and contains(., 'preview.png')]")
    EMPTY_MEDIA_FILES_BANNER = (By.XPATH,
                                "//div[contains(@class, 'vkuiBanner') and contains(., 'Для выбранных мест размещений не хватает медиафайлов')]")
    CHOOSE_MEDIA_FILES_BTN = (
        By.XPATH, "//div[contains(@class, 'vkuiSimpleCell') and contains(., 'Выбрать из медиатеки')]")
    ADD_MEDIA_FILES_BTN = (By.XPATH, "//button[contains(., 'Добавить')]")
    SEND_BTN = (By.XPATH, "//button[contains(., 'Отправить')]")
    PUBLISH_BTN = (By.XPATH, "//button[contains(., 'Опубликовать')]")
    CHANGES_SAVING_MSG = (By.XPATH, "//div[contains(., 'Изменения сохранены')]")
    PREVIEW_ITEM = (
        By.XPATH, "//img[contains(@class, 'MediaContainer_image__HmwFk')]")
    LOGO_MEDIA_PREVIEW = (By.CLASS_NAME, 'AdMediaPreview_loaded__g7y71')
    ACTION_SELECT = (By.XPATH, "//label[contains(@class, 'vkuiCustomSelect') and contains(., 'Действия')]")

    @staticmethod
    def campaign_checkbox(name):
        return (By.XPATH, f"//div[contains(., '{name}')]//div[contains(@class, 'vkuiCheckbox__icon--off')]")

    @staticmethod
    def region_item(region):
        return By.XPATH, f"//button[contains(@class, 'RegionsQuickSelection_item__nOY8O') and contains(., '{region}')]"

    @staticmethod
    def device_option(device):
        return By.XPATH, f"//label[contains(@class, 'vkuiCheckbox') and contains(., '{device}')]"

    @staticmethod
    def placement_option(placement):
        return By.XPATH, f"//div[contains(@class, 'vkuiSimpleCell') and contains(., '{placement}')]"

    @staticmethod
    def checked_placement_checkbox(placement):
        return By.XPATH, f"//div[contains(@class, 'vkuiSimpleCell') and contains(., '{placement}')]//*[contains(@class, 'simpleCheckbox_checked__XSLVa')]"

    @staticmethod
    def form_item_error_msg(item_title, msg):
        return (By.XPATH,
                f"//div[contains(@class, 'vkuiFormItem') and contains(., '{item_title}')]//span[contains(@class, 'vkuiFormItem__bottom') and contains(., '{msg}')]")

    @staticmethod
    def campaign_list_row(name):
        return (By.XPATH, f"//div[contains(@class, 'BaseTable__row') and contains(., '{name}')]")


class BudgetPageLocators:
    PAY_MODAL_BTN = (
        By.XPATH, '//button[contains(@class, AccountInfo_payButton__i1QFc)][contains(., "Пополнить счёт")]')
    PAY_MODAL = (By.XPATH, '//div[contains(@class, vkuiModalPage)][contains(., "Пополнение счёта")]')
    PAY_BTN = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')]//button[contains(string(), 'Пополнить счёт')]")
    AMOUNT_INPUT = (By.NAME, 'amount')
    AMOUNT_WITHOUT_VAT_INPUT = (By.NAME, 'amountWithoutVat')
    MIN_AMOUNT_ERR_MSG = (By.XPATH, "//*[contains(@class, 'vkuiFormItem__bottom') and contains(string(), 'минимальная "
                                    "сумма 600,00 ₽')]")
    PAYMENT_METHOD_FORM = (By.XPATH, "//iframe[contains(@title, 'Счёт')]")
    RANGE_DATA_PICKER_WIDGET = (By.XPATH, "//div[contains(@class, 'RangeDatePicker')]")


class SitesPageLocators:
    OPEN_PIXEL_MODAL_BTN = (By.XPATH, "//button[contains(., 'Добавить пиксель')]")
    ADD_PIXEL_MODAL = (By.XPATH, "//div[contains(., 'Добавление пикселя')]")
    SITE_DOMAIN_OPTION = (
        By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption') and contains(., 'Домен сайта')]")
    PIXEL_ID_OPTION = (
        By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption') and contains(., 'ID пикселя')]")
    SITE_DOMAIN_INPUT = (By.XPATH, "//input[@placeholder='Домен сайта']")
    PIXEL_ID_INPUT = (By.XPATH, "//input[@placeholder='ID пикселя']")
    OWNER_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email владельца']")
    ADD_PIXEL_BTN = (
        By.XPATH, "//div[contains(@class, 'vkuiModalCardBase__actions')]//button[contains(., 'Добавить пиксель')]")
    INVALID_DOMAIN_MSG = (By.XPATH, "//span[contains(., 'Введите корректный адрес сайта (вида: example.ru)')]")
    ACCESS_REQUESTING_BTN = (By.XPATH, "//button[contains(., 'Запросить доступ')]")
    CLOSE_MODAL_BTN = BasePageLocators.by_css_selector('aria-label', 'Закрыть')
    MORE_BTN = BasePageLocators.by_css_selector('aria-label', 'More')
    MORE_CONTEXT_MENU = (By.XPATH,
                         "//div[contains(@class, 'vkuiPopper') and contains(., 'Переименовать') and contains(., 'Удалить пиксель')]")
    RENAME_DROPDOWN_ITEM = (By.XPATH, "//label[contains(., 'Переименовать')]")
    RENAME_CANCEL_BTN = (By.XPATH, "//button[contains(., 'Отмена')]")
    RENAME_APPLY_BTN = (By.XPATH, "//button[contains(., 'Изменить')]")
    RENAME_MODAL = (By.XPATH, "//div[contains(@class, 'vkuiModalCard') and contains(., 'Изменить название пикселя')]")
    RENAME_MODAL_NAME_INPUT = By.XPATH, "//div[contains(@class, 'vkuiModalCard') and contains(., 'Изменить название пикселя')]/div/span/input[@name='name']"

    @staticmethod
    def pixel_by_domain(domain):
        return By.XPATH, f"//*[contains(., '{domain}')]"

    @staticmethod
    def pixel_more_btn(domain):
        return By.XPATH, f"//div[contains(@class, 'PixelsList__row') and contains(., {domain})]/div[contains(@class, 'BaseTable__row-cell')]/button[@aria-label='More']"
