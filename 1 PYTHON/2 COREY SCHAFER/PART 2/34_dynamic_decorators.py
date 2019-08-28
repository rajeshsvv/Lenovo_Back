# print("Dynamic decorators")

# 1st attempt


# def outer_function():
#     message = "Hi"

#     def inner_function():
#         print(message)
#     return inner_function


# my_func = outer_function()
# my_func()
# my_func()


# 2nd attempt
# def outer_function(msg):

#     def inner_function():
#         print(msg)
#     return inner_function


# hi_func = outer_function("HI")
# bye_func = outer_function("BYE")

# hi_func()
# bye_func()

# Decrators are is just a function that takes an other function as an argument
# adds some kind of functionality and then return another function

# for example
# def decorator_function(msg):

#     def wrapper_function():
#         print(msg)
#     return wrapper_function


# hi_func = decorator_function("HI Hello")
# bye_func = decorator_function("BYE")

# hi_func()
# bye_func()


# real decorator example

# def decorator_function(original_function):

#     def wrapper_function():
#         print("wrapper executed this before {}".format(original_function.__name__))
#         original_function()
#     return wrapper_function


# @decorator_function
# def display():
#     print("display function run")


# decorated_display = decorator_function(display)  # same as @decorator_function thats why i comment on this
# decorated_display()
# display()


# real example original function has number of arguments its not work
# *args and **kwargs they allow us to expect any orbitrary number of positional or keyword arguments for functions
# def decorator_function(original_function):

#     def wrapper_function(*args, **kwargs):
#         print("wrapper executed this before {}".format(original_function.__name__))
#         original_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def display():
#     print("display function run")


# @decorator_function
# def display_info(name, age):
#     print("display_info run with arguments({}, {})".format(name, age))


# display_info("john", 56)
# display()


# some people use classes as decorators instead of functions as decorators
# def decorator_function(original_function):

#     def wrapper_function(*args, **kwargs):
#         print("wrapper executed this before {}".format(original_function.__name__))
#         original_function(*args, **kwargs)
#     return wrapper_function


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print("call method executed this before {}".format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)


# @decorator_class
# def display():
#     print("display function run")


# @decorator_class
# def display_info(name, age):
#     print("display_info run with arguments({}, {})".format(name, age))


# display_info("Corey", 36)
# display()


# but corey function decorators use only here practical example shows
# probably most commonly use cases for decorators in python was LOGGING
# my_logger
# import time


# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper


# # @decorator_function
# # def display():
# #     print("display function run")


# @my_logger
# def display_info(name, age):
#     print("display_info run with arguments({}, {})".format(name, age))


# display_info("Schafer", 36)

# my_timer

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper


# # @decorator_function
# # def display():
# #     print("display function run"
# import time


# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("diplay_info run with arguments({},{})".format(name, age))


# display_info("Schafer", 36)


# my_timer and my_logger

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper


# # @decorator_function
# # def display():
# #     print("display function run"
# import time


# @my_logger			#this is the correct order ok
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("diplay_info run with arguments({},{})".format(name, age))


# display_info("Schafer", 36)

# wrapper function into timer
# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper


# # @decorator_function
# # def display():
# #     print("display function run"
# import time


# # @my_logger			#this is the correct order ok
# # @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("diplay_info run with arguments({},{})".format(name, age))


# display_info = my_timer(display_info)
# # display_info("Schafer", 36)
# print(display_info.__name__)


# wrapper function into timer
# good idea to preserve the information of our original function whenever we use decorators
# we can preserve the information by using functools module and wraps decorator

# from functools import wraps


# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper


# @decorator_function
# def display():
#     print("display function run"
# import time


# @my_logger  # this is the correct order ok
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("diplay_info run with arguments({},{})".format(name, age))


# display_info = my_timer(display_info)		#@my_timer thats why i comment it k
# print(display_info.__name__)
# display_info("Andria", 96)
