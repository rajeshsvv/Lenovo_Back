class Hello():
    def __init__(self,name):
        self.name=name
        self.a=10
        self._b=20
        self.__c=30

    def get_c(self):
     return self.__c

    def set_c(self,c):
        self.__c=c

h1=Hello("Maxy")
print(h1.a)
print(h1._b)
print(h1.get_c())
h1.set_c(80)
print(h1.get_c())

h1._b=90
print(h1._b)
