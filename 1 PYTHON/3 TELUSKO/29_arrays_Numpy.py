#   Python array does not support multi dimensional array so we use numpy for this

from numpy import *

array=array([1,2,3,4.1,5,6])
print(array.dtype)

array=arange(0,10,2)
print(array)

# array=linspace(0,10,10)
# print(array)

array=logspace(0,10,2)
print(array)

array=zeros(5)
print(array)


array=ones(5)
print(array)


array=ones(5,int)
print(array)