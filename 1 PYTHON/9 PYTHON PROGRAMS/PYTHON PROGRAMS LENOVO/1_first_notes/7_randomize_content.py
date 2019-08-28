import random
from random import shuffle

mylist=[9,8,7,6,5,4,3,2,1]
# print(shuffle(mylist))            if u print like this u get None k
random.shuffle(mylist)
print(mylist)

#       15   generate random numbers

import random

result=random.random()
print(result)


#       20  Random the string elements

list=["Abay","Raju","Shekhar","Mallemala"]
random.shuffle(list)
print(list)
random.choice(list)
print(list)