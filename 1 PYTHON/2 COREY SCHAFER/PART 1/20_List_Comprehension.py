# List comprehensions in python
# it is easier and more readble way to create a list


# i want 'n' for each 'n' in nums

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# eaiest way for list comprehension
# my_list = [n for n in nums]
# print(my_list)


# i want 'n*n' for each 'n' in nums

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for n in nums:
#     my_list.append(n * n)
# print(my_list)


# eaiest way for list comprehension
# my_list = [n * n for n in nums]
# print(my_list)

# easiest way to lambda expressions map+lambda
# my_list = map(lambda n: n * n, nums)
# print(my_list)


"""
# I want 'n' for a each 'n' in nums if 'n' is even

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# using list comprehension
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# easiest way to filter expressions filter+lambda
my_list = filter(lambda n: n % 2 == 0, nums)
print(my_list)
"""

# i want a (letter,num) pair for each letter in "abcd" and each number in "0123"
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
print(my_list)


# using list comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
"""

# Dictionary Comprehensions

"""
names = ["Bruce", "Clark", "Peter", "Logan", "wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverin", "Deadpool"]
print(zip(names, heroes))  # it does not return result because zip returns a object so when u try to print you just get the object method k
print(list(zip(names, heroes)))

# i want dict{'name':'hero'} for each name,hero in zip(names,heroes)
my_dict = {}

for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)

# using list comprehension
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heroes) if name != "Bruce"}
print(my_dict)
"""

# Set comprehensions
# set is pretty must list except set has uniques values k got it

"""
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9, 5]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
# using list comprehensions

my_set = {n for n in nums}
print(my_set)
"""


# Generator Expressions is similar to list comprehension
# generators are lot of differences things list dictioanries and sets
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)

# using comprehension

# my_gen = (n * n for n in nums)
# for i in my_gen:
#     print(i)
