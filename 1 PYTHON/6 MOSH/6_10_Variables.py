# 6 VARIABLES       13:03
'''
price=10
price=20
print("price")
print(price)
'''

# 7 RECEIVING INPUT     18:21
'''
name=input("what is your name? ")
print("Hi", name)
# print("Hi "+ name)
'''

'''
name=input("what is your name? ")
colour=input("what is your favorite colour? ")
print(name,"likes",colour)
'''


#   9 TYPE CONVERSION   22:46
'''
birth_year=input("Birth Year: ")
print(type(birth_year))
# age=2019-birth_year               # dont give like this u got unsupport operand type.
age=2019-int(birth_year)
print(type(age))
print(age)
'''

'''
weight_lbs=input("Weight in lbs:")
weight_kg=float(weight_lbs)*.45
print(weight_kg)
'''


# 10    STRINGS       30:16


course="Python's course for Beginners"
content='''
Hi Team
Today we are going o learn Python Mosh Course
'''
print(course)
print(course[0:8])
print(content)
