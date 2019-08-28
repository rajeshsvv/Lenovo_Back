#   16      IF STATEMENT        58:17

'''
is_hot=True
is_cold=False
if is_hot:
    print("It's a hot day")         # use shift +back for indentation goes back to start line k
    print("Drink Plenty of Water")
elif is_cold:
    print("It's cold day")
    print("Wear Warm Clothes")
else:
    print("Its lovely Day")
print("Enjoy your Day")
'''


'''
price=1000000
good_credit=True

if good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price

print(f"Down Payment ${down_payment}")
'''


#   17   LOGICAL OPERATORS    1:06:32

'''
#(  AND & both are true         OR |  at least one case true             NOT inverses any boolean value we given it)
has_high_income=True
has_good_credit=True
has_criminal_record=False
# if has_high_income & has_good_credit:
#     print("Eligible for Loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
'''

# 18 COMPARISION OPERATORS  1:11:25

'''
temparature=35

if temparature>30:
    print("Its a Hot day")
else:
    print("Its not a Hot day")
'''

'''
name="TAJ"
name=input("Enter Name:")

# print(len(name))

if len(name)<3:
    print("Name should be atleast three characters")
elif len(name)>50:
    print("Name Should not be greater than 50 characters")
else:
    print("Name Looks Good")
'''

#  19       WEIGHT CONVERTER PROGRAM        1:16:17

'''
weight=int(input("Enter Weight:"))
unit=input("(L)bs or (K)g:")
if unit.upper()=="L":
    converter=weight*0.45
    print(f"You are {converter} kgs")
else:
    converter=weight/0.45
    print(f"You are {converter} lbs")

'''

#  20   WHILE LOOP   1:21:30

    # while condition:
i=1
while i<=6:
    print(i)
    i += 1
print("Done")


# while i<=6:
#     print("*"*i)
#     i += 1
# print("Done")









