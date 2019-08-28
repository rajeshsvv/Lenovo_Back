# program to find even numbers in the list with basic function

# def is_even(a):
#     return a%2==0
#
# nums=[2,3,4,5,6,8,9]
#
# evens=list(filter(is_even,nums))
# print(evens)


# program to find even numbers in the list with lambda function

# nums=[2,3,4,5,6,8,9]
#
# evens=list(filter(lambda n:n%2==0,nums))
# print(evens)


# # program to double the numbers in the list with normal function
#
# def update(a):
#     return a*2
# nums=[2,3,4,5,6,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(update,evens))
# print(evens)
# print(doubles)



# program to double the numbers in the list with lambda function

# nums=[2,3,4,5,6,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(lambda n:n*2,evens))
# print(evens)
# print(doubles)

# program to add two numbers in the list in the list with reduce function
from functools import reduce

# def Add_All(a,b):
#     return a+b
nums=[2,3,4,5,6,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))

# sum=reduce(Add_All,doubles)
sum=reduce(lambda a,b:a+b,doubles)              # with lambda function
print(evens)
print(doubles)
print(sum)