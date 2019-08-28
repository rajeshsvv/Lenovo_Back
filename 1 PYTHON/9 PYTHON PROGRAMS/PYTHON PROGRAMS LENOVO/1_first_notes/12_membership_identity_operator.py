import math
print(math.floor(7//2))

#   Membership  Operator

s='me' in 'yemme'
print(s)

s="no" not in "yes"
print(s)

#   Identity Operator

print(10 is 10)
print(10 is 11)



#membership operators

s='me' in "appointment"
print(s)

y="zi" not in "dost"
print(y)

# Identity operators

state=10 is 10
print(state)

state=10 is not 10
print(state)

a=(1,2,3,4,9)
b=(4,5,6,7,9)
c=(10,11,12,13,41)
print(list(zip(a,b,c)))