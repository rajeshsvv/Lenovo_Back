f=open("MyData",'r')
# print(f.read())
print(f.readline(),end="")
print(f.readline())

f1=open("abc",'w')
f1.write("Arey")
f1.write("Babai")


f1=open("abc",'a')
f1.write("How")
f1.write("You")

for data in f:
    f1.write(data)

