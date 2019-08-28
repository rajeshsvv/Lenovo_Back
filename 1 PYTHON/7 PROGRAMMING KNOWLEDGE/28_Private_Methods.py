class Hello:
    def __init__(self):
        self.a=10                       # public member variable here inside class outside class we use aa well kk..
        self._b=20
        self.__c=30
        self.d=40
#we access the private variable inside the class only outside class we cant access that.like below example
    def public_method(self):
        print(self.a)
        print(self.__c)
        print("acceess private variable here")
        print(self.__public_method())

    def __public_method(self):
        print("private method")


c=Hello()
print(c.a)
print(c._b)
c.public_method()
# print(c.__c)
# c.__public_method()               # it will give error k