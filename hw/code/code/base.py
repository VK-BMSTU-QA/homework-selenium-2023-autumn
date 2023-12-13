from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage

CLICK_RETRY = 3


# Base case for tests


class BaseCase:
    driver = None

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    # Setup driver, config and logger to self. Add base page to self
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue("base_page")
