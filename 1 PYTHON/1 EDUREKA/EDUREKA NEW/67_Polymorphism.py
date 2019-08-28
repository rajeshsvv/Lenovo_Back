class Animal():
    def __init__(self,name):
        self.name=name
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Bow Bow")

c=Cat("Cat")
c.talk()
d=Dog("Dog")
d.talk()
