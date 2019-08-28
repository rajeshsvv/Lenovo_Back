'''
def add(a,b):
    if(type(a)!=type(b)):
        print("Please give the arguments of same type")
        return 0
    print(a+b)

add(2,3)
add("2",5.6)

# print(add(2,3.5))
'''


'''
def add(a,b):
    if(type(a)!=type(b)):
        print("Please give the arguments of same type")
        return True
    return a+b

sum=add(2,3)
print(sum)
    # or
print(add("Hello ","Raj"))
print(add(45.26,5.6))
print(add("Hello",5))
add("Hello",5)

'''


#       22 Default Arguments in Function        3:30:47
'''
def student(name,age):
    print("name:",name)
    print("age:",age)

student("max",22)
print("----")


def student(name="Unknown name",age=0):
    print("name:",name)
    print("age:",age)

student()
'''

# args positional keyword Arguments
'''
def student(name,age,*marks):
    print("name:",name)
    print("age:",age)
    # print("marks",marks)
    for x in marks:
        print("marks:",x)

student("Hello",26,63,56,89,78)
'''

#  kwargs   keyword arguments  3:37:00

def student(name,age,**marks):
    print("name:",name)
    print("age:",age)
    print("marks",marks)

    for x,value in marks.items():
        print(x,":",value)


student("Hello",20,Telugu=26,English=63,Maths=56,Science=89,Social=78)


def students(name,age,*sections,**marks):
    print("name:",name)
    print("age:",age)
    print("marks",marks)
    print("Sections",sections)

    for x,value in marks.items():
        print(x,":",value)

    for x in sections:
        print(x)


students("Hello", 20,'A','B','C','D', Telugu=26, English=63, Maths=56, Science=89, Social=78)