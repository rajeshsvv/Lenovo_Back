class A:
    def sayHi(self):
        print("HI from A")

class B(A):
    def sayHi(self):
        print("Hi from B")

a=A()
a.sayHi()                       # hi from A

b=B()
b.sayHi()                       # hi from B


