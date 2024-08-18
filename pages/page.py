import allure
from playwright.sync_api import Page


class BasePage:
    BASE_URL: str = None

    def __init__(self, page: Page):
        self._page = page

    def open(self):
        with allure.step(f"Open page {self.__class__.__name__}"):
            self._page.goto(self.BASE_URL, wait_until="domcontentloaded")
            return self
