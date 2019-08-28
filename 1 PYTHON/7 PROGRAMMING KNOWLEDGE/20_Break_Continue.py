
#       20  BREAK CONTINUE

# break:: to exit from the loop immediately.

a=[0,1,2,3,4,5]
for x in a:
    if x==3:
        break
    print(x,end=" ")
print("")

i=0
while i<10:
    i += 1
    if i==3:
        continue
    print(i,end=" ")


