#program to print the values in array based on user input
from array import *

array=array('i',[])

n=int(input("Enter the length of the array"))

for i in range(n):
    x=int(input("Enter the next value"))
    array.append(x)

print(array)


#program to search the values in array based on user input

value=int(input("Enter the value for search"))

k=0
for i in array:
    if i==value:
        print(k)
        break

    k+=1


print(array.index(value))



