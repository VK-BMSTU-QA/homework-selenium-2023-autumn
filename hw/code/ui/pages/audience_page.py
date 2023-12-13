import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized
from selenium.common.exceptions import TimeoutException


class NoSaveButton(Exception):
    pass


class NoSource(Exception):
    pass


class AudienceNotFound(Exception):
    pass


class AudiencePage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/audience.*$'

    locators = basic_locators.AudiencePageLocators
    sections = {
        'audiences': locators.AUDIENCES_SECTION_LOCATOR,
        'users': locators.USERS_SECTION_LOCATOR,
    }


    def _find_current_save_button(self):
        primary_buttions = self.find_list(self.locators.SUBMIT_BUTTON_LOCATOR)
        save_buttons = []
        for button in primary_buttions:
            if 'Сохранить' in button.get_attribute("innerHTML"):
                save_buttons.append(button)

        if len(save_buttons) == 0:
            raise NoSaveButton

        return save_buttons[-1] 

    def _find_source_by_text(self, text):
        sources = self.find_list(self.locators.SOURCE_LOCATOR)
        for source in sources:
            if text in source.get_attribute("innerHTML"):
                return source
            
        raise NoSource
    
    def _find_certain_modal_window(self):
        modals = self.find_list(self.locators.MODAL_WINDOW_LOCATOR)
        return modals[-1]
    
    def find_ind_audience_by_name(self, name):
        try:
            campaigns = self.find_list(self.locators.AUDIENCE_TITLE_LOCATOR)
        except TimeoutException:
            return -1, []

        for i in range(len(campaigns)):
            if campaigns[i].get_attribute("innerHTML") == name:
                return i, campaigns
        
        return -1, []
    
    @allure.step("Creating audience")
    def create_audience(self, data):
        self.click(self.locators.START_CREATING_AUDIENCE)
        self.fill_field(self.locators.TITLE_AUDIENCE_LOCATOR, data['title'])
        self.click(self.locators.ADD_SOURCE_LOCATOR)

        source = self._find_source_by_text(data['source'])
        source.click()
        self.fill_field(self.locators.KEYWORDS_LOCATOR, data['keywords'])

        modal_window = self._find_certain_modal_window()
        save_button = self._find_current_save_button()
        save_button.click()
        self.wait_for_remove(modal_window)
        modal_window = self._find_certain_modal_window()
        save_button = self._find_current_save_button()
        save_button.click()
        self.wait_for_remove(modal_window)

    @allure.step("Deleting audience")
    def delete_audience(self, name):
        ind, audiences = self.find_ind_audience_by_name(name)
        self.hover_and_click(self.locators.AUDIENCE_OPTIONS_LOCATOR)
        
        delete_buttons = self.find_list(self.locators.DELETE_AUDIENCE_LOCATOR)
        delete_buttons[-1].click()
        self.click(self.locators.CONFIRM_DELETE_LOCATOR)

        self.wait_for_remove(audiences[ind])

    @allure.step("Opening section {section_name}")
    def open_section(self, section_name):
        super().move_to(section_name, sections=self.sections)


class AudienceUsersPage(AudiencePage):
    url = r'^https:\/\/ads\.vk\.com\/hq\/audience\/user_lists.*$'

    locators = basic_locators.AudienceUsersPageLocators
