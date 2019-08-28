from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,name):
        self.__name=name

    def area(self):
        print("implemented area method")

    def perimeter(self):
        print("implemented perimeter method")

# shape=Shape()         # cant instantiate because decorated with abstractmethod now it is abstract class.
square=Square("John")   # u have to implement the parent abstract methods in child class then only it will output. like this
square.area()
square.perimeter()