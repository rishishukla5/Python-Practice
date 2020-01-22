class TooHot(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Weather:
    def __init__(self, temperature):
        self.temperature = temperature

    def check(self):
        if self.temperature > 85:
            raise TooHot("Coffee Temperature: " + str(self.temperature))
        elif self.temperature < 10:
            raise ValueError("Too Cold")
        else:
            print('Ok')


weather1 = Weather(90)
weather1.check()
# weather2 = Weather(5)
# weather2.check()
# weather3 = Weather(25)
# weather3.check()
