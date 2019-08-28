'''
print(type(2))      # 2 is a object of class int
print(type(2.0))
print(type("hello"))
# print("e"*"e")      # cant multiply sequence by non int of str.
print("str"*3)
'''

import math

class Area:
    def __init__(self,area):
        self.__area=area

    def get_area(self):
        return self.__area

    def set_area(self,area):
        self.__area=area

    def calculate_area(self):
        return math.pi*self.__area**2

    # add operator method overloading method
    def __add__(self, class_object):
        return Area(self.__area+class_object.__area)

    # less than operator method overloading method
    def __lt__(self, class_object):
        # return Area(self.__area<class_object.__area)            # it returns the main area object
          return self.__area<class_object.__area

    # greater than operator  method overloading method
    def __gt__(self, class_object):
        # return Area(self.__area>class_object.__area)            # it returns the main area object
          return self.__area>class_object.__area
    def __str__(self):
        return "Cirlce Area:"+str(self.get_area())
a=Area(2)
print(a.calculate_area())

a1=Area(30)
a2=Area(2)
# print(dir(a))
# print(help(a))
# print(a1+a2)              # for this we need to implement method called __add__ method in our class.
a3=a1+a2
print(a3.get_area())


print(a1>a2)
print(a1<a2)
print(a1<a1)
print(dir(a))
print(str(a1))