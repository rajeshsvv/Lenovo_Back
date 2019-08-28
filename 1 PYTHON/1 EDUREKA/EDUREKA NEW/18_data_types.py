tuple=(0,1,2)
print(tuple[0])
print(tuple[1])
print(tuple[2])
# tuple[0]=1
# tuple[2]=7

b=[[1,2,3],4,'third element',(2,4,5)]

print(b[3][2])


b=([1,2,3],4,'third element',(2,4,5))
b[0][2]="Hello"
print(b[0][2])
print(b)

# dictionaries  36:16

A={"Age":24,"Name":"John"}
A["Age"]=34
print(A["Age"])

B={1:1,2:2,3:3}
print(B[2])