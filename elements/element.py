from playwright.sync_api import Page


class Element:
    def __init__(self, page: Page, locator: str):
        self._element = page.locator(locator)

    def wait(self, timeout: int = 500):
        self._element.wait_for(timeout=timeout)

    def is_visible(self) -> bool:
        return self._element.is_visible()

    def is_enable(self) -> bool:
        return self._element.is_enabled()

    def is_hidden(self) -> bool:
        return self._element.is_hidden()

    def get_text(self) -> str:
        return self._element.text_content()

    def get_border_color(self) -> str:
        return self._element.evaluate('element => window.getComputedStyle(element).borderColor')
