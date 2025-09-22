import random

class Coin:
    def __init__(self):
        self._sideup = "Орел"

    def toss(self):
        if random.randint(0, 1) == 0:
            self._sideup = "Орел"
        else:
            self._sideup = "Решка"

    def get_sideup(self):
        return self._sideup