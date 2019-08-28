def fun(x):
    def b():
        print(x)
    return b

fun(2)()