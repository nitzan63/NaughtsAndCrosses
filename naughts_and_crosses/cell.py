
class Cell:
    """
    Represents a cell in the game
    """
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def is_empty(self):
        return self._value is None

