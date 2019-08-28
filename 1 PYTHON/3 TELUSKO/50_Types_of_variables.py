class Car:

    wheels=4
    def __init__(self):
        self.mil=6
        self.com="BMW"

c1=Car()
c2=Car()

c1.mil=45
Car.wheels=10
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
