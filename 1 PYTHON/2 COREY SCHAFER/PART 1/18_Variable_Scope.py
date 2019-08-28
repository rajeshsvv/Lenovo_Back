"""
Variable scope

LEGB
Local, Enclosing, Global, Built-in

Local-variables defined with in a function
Enclosing-variables in the local scope of an closing function.enclosing functions has to do with the nested functions
Global-variables defined at the top level of module or explicitly declared global using the global keyword

Built-in- are just names are pre-assigned in the python
"""

"""
x = "global x"


def test():
    y = "local scope y"

    # print(y)
    print(x)


test()
print(y)
"""

"""
x = "global x"


def test():
    global x
    x = "local scope x"
    print(x)


test()
print(x)
"""

"""Local scope
def test(z):
    x = "local x"
    print(z)


test("local z")
"""

"""
#Built in scope
import builtins
# print(dir(builtins))  # dir is just gets list of attributes of a given object
# print(dir(min))


# def min(): #it will give error because it checks global level but it is defined as function so it will give errrorb
def my_min():
    pass


m = min([8, 5, 3, 6, 4, 8, 9])
print(m)
"""
x = "global x"


def outer():
    x = "outer x"

    def inner():
        # nonlocal x  # nonlocal statement more often than the global statemenet because can be useful in order to change the state of closures and decorators
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
print(x)
