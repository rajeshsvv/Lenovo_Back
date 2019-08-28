class Polygon:
    __width=None
    __height=None

    def set_values(self,width,height):
        self.__width=width
        self.__height=height

    def get_height(self):                   # public methods because we don't use __ infront of it.
        return self.__height

    def get_width(self):
        return self.__width

    # def set_height(self,value):
    #     self.__height=value
    # def set_width(self,value):
    #     self.__width=value

class Rectangle(Polygon):
    def area(self):
        # return self.__width*self.__height         # we cant access variables like this because these are private
        return self.get_height()*self.get_width()

class Triangle(Polygon):
    def area(self):
        # return self.__width*self.__height/2
        return self.get_height() * self.get_width() / 2
rect=Rectangle()
tri=Triangle()
rect.set_values(20,30)
tri.set_values(40,50)


print(rect.area())
print(tri.area())
