#  19 FOR LOOP      3:03:50


A=[0,1,2,3,4,5]
B=(0,1,2,3,4,5)
c={0,1,2,3,4,5}
D="012345"
E={
    "name":"max",
    "age":20
}



print(0 in A)
print(0 in B)
print(0 in c)
print('0' in D)

for x in A:
    print(x)

for x,value in E.items():
    print(x,value)



for x in range(0,30,5):
    print(x-1,end=",")


