class Client():
    def __init__(self):
        self._diet = None
        self._balance = 0

    @property
    def diet(self):
        return self._diet

    @diet.setter
    def diet(self, value):
        self._diet = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def eatBreakfast(self):
        self.diet.eatBreakfast(self)