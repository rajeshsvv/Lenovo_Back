#41      CONSTRUCTORS    (3:07:46)

# self refers to the current object.
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

point=Point(10,20)
point.x=50                          # refers to the set new value to the variable
print(point.x)


# excersize on constructor(3:11:28)
class Person:
    name="";
    def __init__(self,name):
        self.name=name
        print("initialise construcotr")

    def talk(self):
        print(f"Hi Iam {self.name}")

john=Person("Bachha")
bob=Person("Bob Smith")
john.talk()
bob.talk()
'''

#       42 INHERITANCE      3:14:41

'''
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
        def bark(self):
            print("Dogs are Barking")

class Cat(Mammal):
    def Sound(self):
        print("Cats Makes Sound Mew Mew Mew")
dog=Dog()
dog.bark()
cat=Cat()
cat.Sound()
'''

    # 43 Modules in Python              3:19:33

# A module in python is basically a file with some python code.

'''
import converter_Module
from converter_Module import lbs_to_kg
from converter_Module import find_max

numbers=[50,60,70,80,90,100,200]
print(find_max(numbers))

print(converter_Module.kg_to_lbs(2000))
print(lbs_to_kg(3666))
'''

#       44 PACKAGES         3:30:28



'''
import ecommerce.shipping                                       # one way
from ecommerce.shipping import calc_shopping                    # two way (most prefer)
from ecommerce import shipping                                  # third way


ecommerce.shipping.calc_shopping()                  # one way calling
calc_shopping()                                     # two way calling
shipping.calc_shopping()                            # three way calling
'''

#   45 GENERATING RANDOM VALUES         3:36:22

# python has so many built in modules search in google "python 3 module index"

import random
# for i in range(3)
    # print(random.random())
    # print(random.randint(1,4))


# members=["John","Mary","Bob","Mash"]
# result=random.choice(members)
# print(result)

import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,3)
        print(f"{first},{second}")
        # return first,second

dice=Dice()
dice.roll()
# print(dice.roll())


s="String"
print(s[::2])