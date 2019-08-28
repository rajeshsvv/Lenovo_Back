'''
i=1
while i<5:
    print("the value is",i)
    i+=1
else:
    print("Statement was exit")
'''

'''
num=1
sum=0
print("Enter Number.Plese enter zero(0) to exit")
while num!=0:
    num=float(input("Number?:"))
    sum=sum+num
    print("sum=",sum)
else:
    print("Sum is totalized")
'''

a=[0,1,2,3,4,5]
for  x in a:
    if x==3:
        continue
    print(x,end=",")
print("")


i=0
while i<5:
    i += 1                  # if u mention increment here it will increment the numbers
    if i==2:
        continue
    print(i,end=",")
    # i+=1                    # if u mention increment here it will not increment here
