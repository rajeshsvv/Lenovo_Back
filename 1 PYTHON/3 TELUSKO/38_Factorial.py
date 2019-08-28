#   find a factorial in python
# from math import *
# print(factorial(5))

# calculate factorial in function way

def fact(x):

    f=1
    for i in range(1,x+1):
        f=f*i
    return f

x=3
result=fact(x)
print(result)