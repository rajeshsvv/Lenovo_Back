# iter to create an iterator
# next  to iterate through the next element

a=iter([1,2,3,4,5,6])
print(a)
print(next(a))

for i in a:
    print(i,end=" ")