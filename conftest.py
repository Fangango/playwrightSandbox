import allure
import pytest
from playwright.sync_api import sync_playwright, Browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Choose browser: chromium, firefox, webkit",
    )
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        choices=[True, False],
        type=bool,
        help="Enable headless mode"
    )
    parser.addoption(
        "--slow_mo",
        action="store",
        default=500,
        type=int,
        help="Задержка в миллисекундах между действиями"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    slowmo = request.config.getoption("--slow_mo")
    browser: Browser

    with sync_playwright() as p:
        with allure.step("Open browser"):
            with allure.step('Driver setup'):
                if browser_name is "chromium":
                    browser = p.chromium.launch(headless=headless, slow_mo=slowmo)
                elif browser_name is "firefox":
                    browser = p.firefox.launch(headless=headless, slow_mo=slowmo)
                elif browser_name is "webkit":
                    browser = p.webkit.launch(headless=headless, slow_mo=slowmo)

            yield browser

        with allure.step("Close browser"):
            with allure.step('Driver teardown'):
                browser.close()


@pytest.fixture(scope="function")
def page(browser):
    with allure.step("Open new page"):
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

    yield page

    with allure.step("Close page"):
        page.close()
        context.close()
