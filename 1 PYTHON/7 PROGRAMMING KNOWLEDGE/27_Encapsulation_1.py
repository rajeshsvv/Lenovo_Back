class Car:
    def __init__(self,color,speed):
        # self.speed=speed
        # self.color=color
        self.__speed = speed
        self.__color = color

    def get_speed(self):
        return self.__speed

    def set_speed(self,value):
        self.__speed=value

    def get_color(self):
        return self.__color

    def set_color(self,color):
        self.__color=color


ford=Car("orange",200)
honda=Car("yellow",300)
benz=Car("blue",400)

# ford.speed=500
# ford.speed="500kmph"

ford.set_speed(700)
ford.set_color("purple")

# ford.speed=500            # we create setter and getter methods but still we are able to assign the value .it is to be restricted.
ford.__speed=1000           # now we cant do set speed because in set speed we make variable as private so this is neglizible.
ford.__colour="yellow"

print(ford.get_speed())
print(ford.get_color())
ford.set_color("Re")
ford.set_color("Red")
print(ford.get_color())

