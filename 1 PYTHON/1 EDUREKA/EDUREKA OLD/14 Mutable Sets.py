'''
A set is an unordered collection of items
Every Element is unique(no duplicates) and must be immutable(not changed)

my set={1,2,3}
'''
#creating a set
my_set={1,2,5,7,5,10,8,2,1}
print(my_set)

#
mys1={1,2,3,4,'l'}
mys2={2,3,4,5}
print("Union=",mys1|mys2)
#
print("intersection=",mys1&mys2)
#
print("difference=",mys1-mys2)
print("difference=",mys2-mys1)
