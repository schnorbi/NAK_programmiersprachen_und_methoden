class Rectangle:
    def __init__(self, width, hight):
        self.__width = width
        self.__hight = hight

    def area(self):
        return self.__width * self.__hight

    def perimeter(self):
        return 2*self.__width + 2*self.__hight

rec = Rectangle(5, 4)
print(rec.area())
print(rec.perimeter())

class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size**2

    def perimeter(self):
        return 4*self.__size

squ = Square(5)
print(squ.area())
print(squ.perimeter())
