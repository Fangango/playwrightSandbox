from elements.element import Element


class ButtonElement(Element):

    def click(self):
        self._element.click()

    def double_click(self):
        self._element.dblclick()
