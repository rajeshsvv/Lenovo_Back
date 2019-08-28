'''
marks=20
if(marks>80) and (marks<=100):
    print("GRADE A")
elif(marks>60) and (marks<=80):
    print("GRADE B")
elif(marks>40) and (marks<=60):
    print("GRADE C")
elif marks>=20 and marks<=40:
    print("GRADE D")
else:
    print("Please Enter Marks in between range 0 to 100")
'''

#while loop add numbers upto from given number to zero for example 5 then 5+4+3+2+1=15
num=int(input("Enter the value of n="))
if (num<=0):
    print("Enter a valid value")
else:
    sum=0
    while (num>0):
        sum+=num
        num-=1

print(sum)
