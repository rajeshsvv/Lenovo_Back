nums=[1,2,3,4,5,6]
value=list(filter(lambda x:x%2==0,nums))
print(value)

val1=list(map(lambda x:x//2,value))
print(val1)

from functools import reduce
val2=reduce(lambda x,y:x*y,val1)
print(val2)
