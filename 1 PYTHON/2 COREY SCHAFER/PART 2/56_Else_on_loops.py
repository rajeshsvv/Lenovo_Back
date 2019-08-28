# use of Else clause on loops whether it is for loop or while loop.use no break in that case if u dont want execute else statements in loops

"""
# 1st example
num = 2

if num < 2:
    print("number is less than 2")
elif num == 2:
    print("number is equal to 2")
else:
    print("number is greater than 2")
"""

"""
# 2nd example
my_list = [1, 2, 3, 4, 5, ]

for i in my_list:
    print(i)
    if i == 4:
        break
else:
    print("Hit For/Else statement!")
"""


"""
#3 rd example
 
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 8:
        break
else:
    print("Hit for While/Else statement!")
"""


"""
4 find index of word in list of words


def search_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


my_list = ["C#", "Java", "Python", "Perl"]
index_location = search_index(my_list, "Hello")

# print("Location of the target index is {}".format(index_location))
print(f"Location of the target index is {index_location}")
"""