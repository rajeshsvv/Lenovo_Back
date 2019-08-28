from numpy import *

# array=array([1,3,4,5,2])
# array=array+5
# print(array)
# print(array.dtype)
# print(sin(array))
# print(cos(array))
# print(tan(array))
# print(tan(array[1]))
# print(log(array))
# print(sqrt(array))
# print(sort(array))
# print(min[array])
# print(max[array])



#    add two arrays
# array1=array([1,2,3,4,5])
# array2=array([5,4,3,2,1])
# print(concatenate([array1,array2]))
# array3=array1+array2
# print(array3)


arr1=array([2,6,9,8,7,4,6,5])
# arr2=arr1                                                #same address
# arr2=arr1.view()                                       #different address     SHALLOW COPY    both are reflected
arr2=arr1.copy()                                         #different address     DEEP COPY       ORIGINAL NOT reflected
arr1[1]=25
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))