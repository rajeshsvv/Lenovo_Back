# count=0
# while count<5:
#     print(count)
#     count+=1

# rank=5
# while rank!=12:
#     print(rank)
#     rank+=1

'''
number=int(input("Enter Number:"))
if number==10:
    print("Number is too small")
elif number==15:
    print("Number is too large")
elif number==13:
    print("exit congrats you made it")
else:
    print("you enter wrong number")
'''


# For Loop

# fruits=["Banana","Apple","Grapes"]
#
# for fruit in fruits:
#     print(fruit)

day="Thursday"
while day=="Wednesday":
    for i in [1,2,3,4]:
        print("something")
else:
      print("Nothing")


#   Nested Loop:

count=1

# for i in range(10):
#     print(str(i)*i)
#     for j in range(0,i):
#         count+=1


# Control Statements (break continue pass)

for i in range(1,11):
    if i==5:
        # continue          #   (in output it does not print 5)
        break                #  (in output stops the execution at 5 only k)
    print(i)