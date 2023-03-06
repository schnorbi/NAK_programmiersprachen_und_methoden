import math
from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Form):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_area(self):
        return self.__a * self.__b

class Square(Form):
    def __init__(self, a):
        self.__a = a

    def get_area(self):
        return self.__a ** 2

class Circle(Form):
    def __init__(self, a):
        self.__a = a

    def get_area(self):
        return 2 * math.pi * (self.__a**2)


rechteck = Rectangle(10,5)
print(rechteck.get_area())

quadrat = Square(10)
print(quadrat.get_area())

kreis = Circle(5)
print(kreis.get_area())