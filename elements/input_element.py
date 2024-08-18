from elements.element import Element


class InputElement(Element):

    def input(self, string: str):
        self._element.fill(string)

    def tape(self, string: str):
        self.tape(string)
