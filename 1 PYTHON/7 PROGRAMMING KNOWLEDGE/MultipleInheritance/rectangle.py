from MultipleInheritance.polygon import Polygon
from MultipleInheritance.shape import Shape

class Rectangle(Polygon,Shape):
    def area(self):
        return self.get_width()*self.get_height()
        #   return self.__width*self.__height
        # dont access like this because these are provate attributes.access throuth method only