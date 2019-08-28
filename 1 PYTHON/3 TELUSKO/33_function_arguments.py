#python does not support pass by value or pass by reference

def update(x):
    print(id(x))
    x=18
    print(id(x))
    print("x value",x)

a=12
print(id(a))
update(a)
print(id(a))
print("a value is",a)