class upside_down:

    def __init__(self, val):
        self.__var = val

    def __add__(self, second):
        return self.__var - second.__var

    def __sub__(self, second):
        return self.__var + second.__var

    def __mul__(self, second):
        return self.__var / second.__var

    def __truediv__(self, second):
        return self.__var * second.__var

    def __lt__(self, second):
        return self.__var > second.__var

    def __gt__(self, second):
        return self.__var < second.__var

    def __eq__(self, second):
        return self.__var != second.__var

    def get_var(self):
        return self.__var


u1 = upside_down(1)
u2 = upside_down(2)

print("u1 = " + str(u1.get_var()))
print("u2 = " + str(u2.get_var()))

print("u1 + u2 = " + str(u1 + u2))
print("u1 - u2 = " + str(u1 - u2))
print("u1 * u2 = " + str(u1 * u2))
print("u1 / u2 = " + str(u1 / u2))
print("u1 > u2 = " + str(u1 > u2))
print("u1 < u2 = " + str(u1 < u2))
print("u1 == u2 = " + str(u1 == u2))
