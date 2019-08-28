'''
a=[1,2,3,4,5]
# for i in a:
#     print(i)

it=iter(a)
print(next(it))             # retrieve one by one value in list a because list is a iterable.use dir u know iter is there.
print(next(it))
print(next(it))
'''


#  create a custom Iterator

class ListIterator:
    def __init__(self,list):
        self.__list=list
        self.__index=+1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index+=1
        if self.__index>=len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

a=[1,2,3,4,5,6]
mylist=ListIterator(a)
it=iter(mylist)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


for i in it:
    print(i)

