'''
nums=[1,2,3]
print(nums)

i_nums=iter(nums)
print(i_nums)
print(dir(i_nums))
# print(next(i_nums))

while True:
    try:
        item=next(i_nums)
        print(item)
    except StopIteration:
        break
'''




'''
class MyRange:
    
    def __init__(self,first,last):
        self.value=first
        self.last=last

    def __iter__(self):
        return self

    def __next__(self):
        if self.value>=self.last:
            raise StopIteration
        current=self.value
        self.value+=1
        return current


# nums=MyRange(1,9)

# for num in nums:
#     print(num)

print(next(nums))
print(next(nums))
print(next(nums))
'''

# impliment generator but it does not need impliment iter and next methods

def my_gen(start,end):
    current=start
    while current<end:
        yield current
        current +=1


# def my_gen(start):
#     current=start
#     while True:
#         yield current
#         current+=1

# nums=my_gen(1)

nums=my_gen(1,10)
for num in nums:
    print(num)

# nums=my_gen(1,9)
# for num in nums:
#     print(num)



