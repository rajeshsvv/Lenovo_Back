def fun(*args):
    for i in args:
        print(i,end=" ")

print(fun(1.6,2,3,4,5))


def fun(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
    return True

print(fun(a=1,b=2,c=3))

def fun(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

fun(a=10,b=20,c=30)