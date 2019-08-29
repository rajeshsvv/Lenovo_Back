class A:
    def fun(self):
        print("Hi")

    def monkey(self):
        print("hi Monkey")

    m.A.fun=monkey
    a=m.A()                         #  Answer----------Hi Monkey
    a.fun()



