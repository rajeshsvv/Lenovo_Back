# a nested function references a value in its enclosing scope.it means it

def fun(x):
    def b():
        print(x)
    return b

fun(2)()