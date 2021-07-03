class Loot:
    """
    Repraesentiert die Beute
    """

    def __init__(self, value, weight):
        self._value = value
        self._weight = weight

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value >= 0:
            self._value = value
        else:
            raise ValueError("Wert muss >= 0 sein!")

    @value.deleter
    def value(self):
        del self._value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self._weight = weight
        else:
            raise ValueError("Gewicht muss > 0 sein!")

    @weight.deleter
    def weight(self):
        del self._weight

    def calculate_vw(self):
        return self._value/self.weight

    def compare_to(self, loot):
        if self.calculate_vw() > loot.calculate_vw():
            return True
