
class Car:
    def __init__(self):
        print("the __init__ is called")

ford=Car()
honda=Car()
mercedez=Car()

ford.speed=500
honda.speed=600
mercedez.speed=700


ford.color='red'
honda.color='orange'
mercedez.color='purple'

print(ford.speed)
print(ford.color)

ford.speed=400
ford.color="white"
print("---")

print(ford.speed)
print(ford.color)

'''
class Rectangle:
    pass

rect1=Rectangle()
rect2=Rectangle()

rect1.height=20
rect1.width=30

rect2.height=40
rect2.width=50

print(rect1.height*rect1.width)
print(rect2.height*rect2.width)
'''






