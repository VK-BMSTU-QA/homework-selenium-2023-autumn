import allure_commons
import allure
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.base_page import BasePageAuthorized
from ui.locators import basic_locators

class CampaignPage(BasePageAuthorized):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'

    locators = basic_locators.CampaignPageLocators

    def create_campaign(self):
        self.logger.debug("Starting authorization")
        self.click(self.locators.TRIGGER_CREATE_CAMPAIGN_LOCATOR)
        return CreateCampaignPage(self.driver)
    
    def close_onboarding(self):
        self.logger.debug("checking exists onboarding screen")

        print("heeeeeeeeeeeeeeere")
        self.click(self.locators.ONBOARDING)

        # if self.has_object(self.locators.ONBOARDING_LOCATOR):
        #     self.logger.debug("onboarding screen is exists")

        #     with allure.step("closing onboarding screen"):
        #         self.click(self.locators.ONBOARDING_CLOSE_LOCATOR)
        # else:
        #     self.logger.debug("help screen don't exists")

        # if self.has_object(self.locators.HELP_LOCATOR):
        #     self.logger.debug("help screen is exists")

        #     with allure_commons.step("closing help screen"):
        #         self.click(self.locators.HELP_CLOSE_LOCATOR)
        # else:
        #     self.logger.debug("onboarding screen don't exists")

