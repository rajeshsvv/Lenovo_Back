#   26   2D Lists               2:01:45

'''
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# matrix[0][1]=200
# print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
'''

#   28 List Methods(Mutable)        2:06:00

'''
#       append method to add a new item in the list.

numbers=[5,2,1,7,4,50,5]
numbers.append(20)
numbers.insert(0,200)
numbers.remove(20)
# numbers.clear()               # to clear all the items in the list
numbers.pop()                   # remove last item in the list pop means

print(numbers)
print(numbers.index(5))
print(numbers.index(7))
# print(numbers.index(100))           # to check the number in the list

print(50 in numbers)
print(numbers)
numbers.append(5)
print(numbers.count(5))

# None is a object in python that represents the absence of value.

numbers.sort()
# numbers.sort(reverse=True)

print(numbers)
number2=numbers.copy()
numbers.append(300)
print(numbers)
print(number2)

'''
# write  a program to remove duplicate numbers in the list

numbers=[1,2,3,4,5,6,5,4,3,2,1,-1,-2,3,-4,-3,-2,-1]
# print(list(set(numbers)))         # Built in short cut method

place=[]

for number in numbers:
    if number not in place:
        place.append(number)
print(place)



#       29  TUPLES(Immutable)               2:13:25

# like list but we cannot modify, add new items, remove existing items

#   count---to count the number of occurrences in an item.
#   index---to find the index of the first occurrences of an item.
#   so we can only get info about tuple. we cannot change it ok got it.
#   we cannot mutate or change the tuple they are immutable.

'''
numbers=(1,2,3,4,5,6,7,8,9)
print(numbers[0])
numbers[0]=1
print(numbers)

'''

#       30  UNPACKING           2:15:34    we can use unpacking with tuples and lists also

coordinates=(1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

x,y,z=coordinates
print(x,y,z)



