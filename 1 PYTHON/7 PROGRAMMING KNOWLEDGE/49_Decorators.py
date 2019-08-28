'''
def decorator_function(func):
    def warpper_func():
        #before executing the function
        print("X value is 10")
        func()
        print("X value is 20")
        # after executing the function
    return wrapper_func

@decorator_function                     # don pass parenthesis()  here it will asks one argument then
def say_hello():
    print("Hello World")

# hello=decorator_function(say_hello)
# hello()
say_hello()

'''

# with two decorators

'''
def dec_x(func):
    def wrap_func():
        print("x"*20)
        func()
        print("x"*20)
    return wrap_func
def dec_y(func):
    def warp_func():
        print("y"*20)
        func()
        print("y"*20)
    return warp_func

# @dec_y
# @dec_x
def say_hello():
    print("say Hello")

# say_hello()

hello=dec_y(dec_x(say_hello))
print(hello())
'''

# decorator function for division operation
'''
def dec_func(func):
    def wrap_func(x,y):
        print("divide",x,"and",y)
        if y==0:
            print("y value cannot be zero division operation failed")
            return 0
        return x/y
    return wrap_func

@dec_func
def divide(x,y):
    return x/y

print(divide(100,20))
divide(20,0)
'''

# Real time exxample
from time import time

def timig_func(func):
    def wrap_func(*args,**kwargs):
        start=time()
        print(start)
        result=func(*args,**kwargs)
        end=time()
        print(end)
        print("Elapsed TIme: {}".format(end-start))
        return result
    return wrap_func

@timig_func
def addition(num):
    result=0
    for i in range(num+1):
        result+=i
    return result

print(addition(1063900))
print(addition(620000856))