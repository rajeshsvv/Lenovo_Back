'''
def double(x):
    return x*2
def add(x,y):
    return x+y
def product(x,y,z):
    return x*y*z

print(double(8))
x=double(4)
print(x)
'''

'''
# Lambda Functions Creation:

double=lambda x:x*2
add=lambda x,y:x+y
product=lambda x,y,z:x*y*z


print(double(5))
print(add(5,6))
print(product(5,6,7))
'''

# MAP FILTER REDUCE FUNCTIONS WITH LAMBDA FUNCTIONS


# MAP FUNCTION  (7:49:00)
'''
a=[1,2,3,4,5,6]
# double=map(lambda x:x*2,a)      # it will return map object
double=list(map(lambda x:x*2,a))    # it will give the actual result
print(double)

b=[1,23,4,56,6,6]
c=[9,8,7,4,5,6]
add=map(lambda x,y:x+y,b,c)
print(add)      # returns the map object
print(list(add))
'''

# FILTER FUNCTION   7:52:37
# filter function takes two arguments first argument as function which gives us boolean result.

'''
a=[1,2,3,4,5,6,7,8,9,10]

# result=filter(lambda x:x%2==0,a)
# print(list(result))

result11=filter(lambda x:True if x>=5 else False,a)
print(list(result11))
'''

# Reduce Function   7:55:53
# for reduce function u need to import functools module.

from functools import reduce
a=[1,2,3,4,5,6,7]
e=reduce(lambda x,y:x-y,a)
print(e)
