
#   11 FORMATTED STRINGS    37:36

'''
first="Rajesh"
last="Veeru"
message=first+' ['+last+'] is a coder'
msg=f"{first} [{last}] is a coder"
m1="{0},{1}".format(first,last)
print(message)
print(msg)
print(m1)
'''

#   12 STRING METHODS(find replace in upper lower title)    40:50

'''
course="Python for beginners"
print(len(course))
print(course.upper())
print(course.lower())               # these are create a new variables and store thee result into new one k
print(course)


print(course.find('y'))
print(course.find("S"))             # -1 because S is not exist in the string k
print(course.find("beginners"))     # 11 because b starts at word 11 k
print(course.replace("Python","Ruby"))
print("Python" in course)
'''

#       13 ARITHMATIC OPERATORS     48:33

'''
print(10/3)         #   3.3333
print(10//3)        #  3
print(10%3)         #  1
print(10*3)         #  30
print(10**3)        # 1000
'''


#   50:14    AUGMENTED ASSIGNMENT OPERATOR

'''
x=10
x=x+3
x+=3            #(Augmentes Assignment Operator or enhanced assignment operator)
x-=3
x*=3
x/=3
print(x)
'''

#   14  51:33  OPERATOR PRECEDENCE OPERATOR:

# first parenthesis
# exponentiation 2**3
# multiplication or division
# addition or subtraction

'''
x=10+3*2**2
print(x)                    #   22

y=(10+3)*2**2
print(y)                    #   52

x=(2+3)*10-3
print(x)                    #   47

'''

#   15   MATH FUNCTIONS    55:38

'''
x=-2.9
print(round(x))
print(abs(x))           # abs retruns returns positive representtation value even if it is negative value


import math
print(math.ceil(-2.9))      # -2
print(math.floor(-2.9))     #  -3
'''