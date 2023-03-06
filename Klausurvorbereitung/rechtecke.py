class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_area(self):
        return self.__a * self.__b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

rechteck = Rectangle(10,5)
print(rechteck.get_area())

quadrat = Square(10)
print(quadrat.get_area())