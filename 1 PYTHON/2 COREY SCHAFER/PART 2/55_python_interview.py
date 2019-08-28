# pytohn interview questions

# Basic Pythonda ta types 2
# for loop
"""
for i in range(1, 20):
    print(i)
"""

# while loop
"""
i = 1
while i < 10:
    print(i)
    i += 1
"""

# if and else statements
"""
a = 0
b = 20
if a < b:
    print("{} is less than {}".format(a, b))
elif a == 20:
    print("{} is equal to {}".format(a, b))
else:
    print("{} is greater than {}".format(a, b))
"""

# python example codes 3
# Fizz Buzz
# for num in range(1, 4):
#     if num % 5 == 0 and num % 3 == 0:
#         print("Fizz Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print("num")

# fibonacci Sequence     adding previous number to the next number like this 0 1 1 2 3 5 8 13 21 34
# a, b = 0, 1
# for i in range(0, 10):
#     print(a)
#     a, b = b, a + b


# basic python data types 5
# Lists
# my_list = [2, 5, 6, 3, 4, 10, -9]
# for i in my_list:
#     print(i)

# Tuples
# my_tuple=(1,2,3,4,5,6,7,8,9)
# for i in my_tuple:
# 	print(i)


# Dictionary dont run this iteritems does not found in dict object check this okay
# my_dict = {"name": "Bronx", "age": "2", "occupation": "Corey's Dog"}
# for key, value in my_dict.items():
#     # for key, value in my_dict.iteritems():  it does not work may be it work in python 2 version because of iteritems k its work in pyton 2 v only
#     # print("My {} is {}".format(key, val))
#     print(key, value)


# Sets it looks like lists but dont have duplicate values uniques values only
# my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
# for i in my_set:
#     print(i)


# List Comprehensions 6
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # for num in my_list:  #actual for loop it is
# #     square = num * num
# #     print(square)

# #give me each number in list is squared list comprehension way
# square = [num * num for num in my_list]
# print(square)


# Fibonacci Generator
# def fib(num):
#     a, b = 0, 1
#     for i in range(0, 10):
#         yield"{}:{}".format(i + 1, a)
#         a, b = b, a + b

# for item in fib(4):
#     print(item)


# OOPS object oriente dprogramming

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        # print("My name is {}".format(self.name))
        print(f"My name is {self.name}")


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("... and Iam {}".format(self.hero_name))


# corey = Person("Core")
# corey.reveal_identity()


wade = SuperHero("Wade Wilson", "Deadpool")
wade.reveal_identity()
