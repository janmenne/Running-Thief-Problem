class Loot:

    def __init__(self, value, weight):
        self._value = value
        self._weight = weight

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @weight.deleter
    def weight(self):
        del self._weight
