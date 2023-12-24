from ui.locators import basic_locators
from ui.pages.hq_page import HqPage


class SettingsNotificationsPage(HqPage):
    FINANCE_OPTION = 'Финансы'
    MODERATION_OPTION = 'Модерация'
    ADS_CAMPAIGNS_OPTION = 'Рекламные кампании'
    RULES_OPTION = 'Правила для объявлений'
    API_CHANGE_OPTION = 'Изменения в API'

    NEWS_OPTION = 'Новости'
    EVENTS_OPTION = 'Мероприятия'
    OTHER_OPTION = 'Акции, спецпредложения и прочие'

    OPTIONS = (FINANCE_OPTION, MODERATION_OPTION, ADS_CAMPAIGNS_OPTION, RULES_OPTION, API_CHANGE_OPTION,
               NEWS_OPTION, EVENTS_OPTION, OTHER_OPTION)

    url = 'https://ads.vk.com/hq/settings/notifications'
    locators = basic_locators.SettingsNotificationsPageLocators

    def switch_notification_enabled(self):
        self.click(self.locators.NOTIFICATION_ENABLE_BTN)

    def is_options_disabled(self):
        for option in self.OPTIONS:
            self.is_disabled(self.locators.checkbox_by_name(option))

    def switch_option(self, option_name):
        self.click(self.locators.item_by_name(option_name))
