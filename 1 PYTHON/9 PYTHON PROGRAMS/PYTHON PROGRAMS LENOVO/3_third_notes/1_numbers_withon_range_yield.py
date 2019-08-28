def iterate(start,end):
    current=0
    while current<end:
        yield current
        current+=1

nums=iterate(1,10)
print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


for i in nums:
    print(i,end=" ")

