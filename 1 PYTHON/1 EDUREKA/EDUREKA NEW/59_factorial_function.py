'''
def factorial():
    num=int(input("Enter Number:"))
    factorial=1

    if num<0:
        print("Must be Positive")
    elif num==1:
        print("Factorial=1")
    else:
        for i in range(1,num+1):
            factorial=factorial*i

    return factorial

print(factorial())
'''

# function return
'''
def add(a,b):
    sum=a+b
    return sum
print(add(2,30))
print(add(-15,-15))
'''


#   2:04:41 enumeate function

'''
grocery=['bread',"milk","butter"]
enumerateGrocery=enumerate(grocery)

print(type(enumerateGrocery))
print(enumerateGrocery)                 # it returns object. convert to list to get the actual result.
print(list(enumerateGrocery))

enumerateGrocery=enumerate(grocery,10)
print(list(enumerateGrocery))
'''


#   lambda function 2:06:13

# ans=lambda z:z*3
# print(ans(4))
#
# def ans(z):
#     return z*4
# print(ans(4))


'''
# map function
items=[1,2,3,4,5]
squares=print(list(map(lambda x:x**2,items)))

        #   or      but it is more difficult to write right so follow above one.

# def squares(items):
#     r=[]
#     for i in items:
#         r.append(i**2)
#     return r
# items=[1,2,3,4,5]
# print(squares(items))

# filter function

items=range(-5,5)
filter=print(list(filter(lambda x:x<0,items)))


# reduce function

from functools import reduce

# product=print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
product=print(reduce(lambda x,y:(x**2)*(y),[1,2,3,4]))
product=print(reduce(lambda x,y:(x)*(y**2),[1,2,3,4]))
product=print(reduce(lambda x,y:(x)*(y),[1,2,3,4]))

'''

# Scope of Functions Global vs Local

a=50
def number():
    b=30
    print(b)

print(a)
number()


a=10
b=20
print(id(a))
print(id(b))