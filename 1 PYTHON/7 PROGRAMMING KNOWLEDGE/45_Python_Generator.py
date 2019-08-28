'''
def my_func():
    yield "a"
    yield "b"
    yield "c"
    yield "d"

x=my_func()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))              # this is extra print statement it raises stop iteration exception.


#using for loop we did not stopiteration exception.

# for i in x:
#     print(i)

'''

'''
def func():
    n=1
    print("--------------------",n)
    yield n
    print("-----------------",n)
    n+=1
    yield n
    print("----------------",n)
    n+=1
    yield n
    print("----------------", n)


x=func()
print(next(x))
print(next(x))
print(next(x))

'''

'''
def my_func():

    for i in range(6):
        print("----------",i)
        yield i

x=my_func()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

'''

def list_generator(list):
    for i in list:
        yield i

a=[1,2,3,4,5,6]
x=list_generator(a)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


for i in x:
    print(i)