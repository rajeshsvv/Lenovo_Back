# Boolean Operations

"""
and
or
not

"""


user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin Page")
elif user == "Admin" or logged_in:
    print("print one page")
else:
    print("Home Page")

print()

if not logged_in:
    print("Please Log in")
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))

print(a is b)  # False because a and b are refered to different objects

b = a
print(a is b)  # True because now both are refered to same object because of b=a got it
print(a == b)
print(id(a) == id(b))
