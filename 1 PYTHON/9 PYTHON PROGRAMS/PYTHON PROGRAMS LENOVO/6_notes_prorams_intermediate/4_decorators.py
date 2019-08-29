
def check(func):
    def inner(a,b):
        if b==0:
            print("cannot divide by zero")
        return func(a,b)
    return inner

@check
def devide(a,b):
    return a/b

print(devide(10,5))


'''
def smart_div(func):

    def inside(a,b):
        if b==0:
            print("division cannot be possible")
        return func(a,b)
    return inside

@smart_div
def devide(a,b):
    print(a/b)

print(devide(4,2))
'''