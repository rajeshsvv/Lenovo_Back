from array import *
import array
#
# # values=array.array('I',[4,8,9,6,-3,7,4,5])
# values=array.array('i',[8,9,6,-3,7,4,5])          #signed integer means negative to positive integers
#
# for i in range(7):
#     print(values[i])

# print(values.buffer_info())
# print(values.typecode)
# print(values[0])


# value=array.array('u',['a','e','i','o'])
# for i in value:
#     print(i)

values=array.array('i',[8,9,6,-3,7,4,5])
newArray=array.array(values.typecode,(a for a in values))

#for loop
# for e in newArray:
#      print(e)

#while loop
i=0
while i<len(newArray):
    print(newArray[i])
    i+=1