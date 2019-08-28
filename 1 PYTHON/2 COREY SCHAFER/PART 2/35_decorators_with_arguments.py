# decorators without arguments example


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Execute Before:", original_function.__name__)
#         result = original_function(*args, **kwargs)
#         print("Executed After:", original_function.__name__, "\n")
#         return result
#     return wrapper_function


# @decorator_function
# def display_info(name, age):
#     print("display_info run with arguments({},{})".format(name, age))


# display_info("Ramesh", 34)
# display_info("Rakesh", 45)


# decorators with arguments

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Execute Before:", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed After:", original_function.__name__, "\n")
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('TESTING:')
def display_info(name, age):
    print("display_info run with arguments({},{})".format(name, age))


display_info("Ramesh", 34)
display_info("Rakesh", 45)
