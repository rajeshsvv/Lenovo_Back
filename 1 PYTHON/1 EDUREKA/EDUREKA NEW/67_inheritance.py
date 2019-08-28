'''
class base():
    def __init__(self):
        self.parent="parent attribute"
    def impliment(self):
        print("In parent class")

class child(base):
    # if u implement the same method in parent child class relationship first it will look into the child class
    # in the sense same class if its not available then go to the parent class.

    def impliment(self):
        print("In child class")


b=base()
c=child()
print(c.parent)

c.impliment()
'''

# Multiple Inheritance
# a single derived class inherited from more than two or more base classes.

class A:
    def __init__(self):
        super(A,self).__init__()
        print("first")

class B():
    def __init__(self):
        super(B,self).__init__()
        print("second")

class C(A,B):                       # because of method resolution order(MRO)
    def __init__(self):
        super(C, self).__init__()
        print("third")

# a=A()
# b=B()
c=C()

