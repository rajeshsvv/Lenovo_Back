class A:
    def fun(self):
        print("Hi")
class B:
    def monkey(self):
        print("hi Monkey")

    A.fun=monkey
    a=monkey.A()                         #  Answer----------Hi Monkey
    a.fun()



