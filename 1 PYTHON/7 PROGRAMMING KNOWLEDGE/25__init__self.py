'''
class Car:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
            # or
        # print(name)
        # print(speed)

        # print("the __init__ is called")

ford=Car("Ford",200)
# print(ford.name)
bugatti=Car("Bugatti",300)
# print(bugatti.name
lamborghini=Car("Lamborghini",500)
# print(lamborghini.name)
# ford.speed=500
# honda.speed=600
# mercedes.speed=700
#
#
# ford.color='red'
# honda.color='orange'
# mercedez.color='purple'
#
print(ford.speed)
print(ford.name)

print(lambargini.name)
print(lambargini.speed)
print("--")
#
# ford.speed=400
# ford.color="white"
# print("---")
#
# print(ford.speed)
# print(ford.color)
'''


# class Rectangle:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#
# rect1=Rectangle(50,60)
# rect2=Rectangle(40,30)
#
# print(rect1.width*rect1.height)
# print(rect2.height*rect2.width)

class Rectangle:
    def __init__(self,height,width):
        self.__height=height
        self.__width=width

    def get_height(self):
        return self.__height

    def set_height(self,value):
        self.__height=value

    def get_width(self):
        return self.__width

    def set_width(self,value):
        self.__width=value

    def area(self):
        return self.__height*self.__width


rect1=Rectangle(50,60)
rect2=Rectangle(40,30)

# print(rect1.width*rect1.height)
# print(rect2.height*rect2.width)

print(rect1.area())
print(rect2.area())
print(rect1.get_height())
print(rect1.get_width())
print(rect2.get_height())
print(rect2.get_width())