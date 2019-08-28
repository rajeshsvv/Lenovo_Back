# def greet():
#     print("Hello")
#     print("Good Evening")
#
#
# greet()
# greet()
# functions are of two types. it may can return a  value or store a value

#   function return a value
def add(a,b):
    c=a+b
    print(c)

# it may can store a  value
# def ad(a,b):
#     c=a+b
#     return c

# result=ad(5,4)
# print(result)

add(3,4)



def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(20,29)
print(result1)
print(result2)