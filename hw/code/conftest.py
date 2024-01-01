from ui.fixtures import (
    driver,
    download_directory,
    service,
    base_page,
    login_page,
    lk_page,
    company_page,
    center_of_commerce_page,
    new_company_page,
    group_adv_page,
    adv_page,
    audience_page,
    site_page,
    main_page,
    cases_page,
    events_page,
    ideas_forum_page,
    monetisation_page,
    news_page,
    useful_materials_page,
)
import pytest

DEFAULT_YANDEX_BROWSER_PATH = "/Applications/Yandex.app/Contents/MacOS/Yandex"
YANDEX_DRIVER_PATH = "../../chromedriver-mac-x64/chromedriver"


def pytest_addoption(parser):
    parser.addoption("--browser", default="yandex")
    parser.addoption("--yandex_driver_path", default=YANDEX_DRIVER_PATH)
    parser.addoption(
        "--yandex_browser_path", default=DEFAULT_YANDEX_BROWSER_PATH
    )


@pytest.fixture(scope="session")
def config(request):
    browser = request.config.getoption("--browser")
    ya_driver_path = request.config.getoption("--yandex_driver_path")
    ya_browser_path = request.config.getoption("--yandex_browser_path")

    return {
        "browser": browser,
        "yandex_driver_path": ya_driver_path,
        "yandex_browser_path": ya_browser_path,
    }
