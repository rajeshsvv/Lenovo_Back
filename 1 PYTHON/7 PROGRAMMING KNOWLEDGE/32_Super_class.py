class Parent:
    def __init__(self,name):
        print("Parent __init__",name)

class Parent2:
    def __init__(self,name):
        print("Parent2 __init__",name)
class Child(Parent2,Parent):
    def __init__(self):
        print("Child __init__")
        # super().__init__("Ajay")            # this case is whe u have single parent in the sense single inheritance
        # in case of multiple inheritance call the parent class name manually and pass self keyword also
        Parent2.__init__(self,"John")
        Parent.__init__(self,"Gunman")
        super().__init__("Sankar")

child1=Child()
print(Child.__mro__)
print(Parent.__mro__)