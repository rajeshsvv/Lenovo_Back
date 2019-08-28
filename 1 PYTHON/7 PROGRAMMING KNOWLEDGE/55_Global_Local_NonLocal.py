'''
def func():
    global x
    print("1",x)
    x='local'
    print("2",x)

x='global'
func()
print("3",x)
'''

#       NON LOCAL VARIABLES:9:39:05

def func():
    x=70
    def inner():
        # global x                # output 70 70 100
        nonlocal x                # output 70 100 50
        x=100
    print("1",x)
    inner()
    print("2",x)

x=50
func()
print("3",x)


# print(dir(len))
