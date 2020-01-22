from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, __side):
        self.__side = __side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


square = Square(4)

print(square.area())
