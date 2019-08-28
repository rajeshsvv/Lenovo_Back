# operator overloading is also called ad-hoc polymorphism

class itspower:
    def __init__(self,x):
         self.x=x

    def __pow__(self,other):
        return self.x**other.x
a=itspower(2)
b=itspower(2)
print(a**b)
