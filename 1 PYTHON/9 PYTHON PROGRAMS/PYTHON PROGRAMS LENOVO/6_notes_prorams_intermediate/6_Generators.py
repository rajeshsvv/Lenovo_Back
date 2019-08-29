def square_nums(nums):
    for i in nums:
        yield i*i
nums=[1,2,3,4,5,6,7,8,9]
result=square_nums(nums)            # it will return generator object
print(result)                       # it will return first element
print(next(result))                 # it will return second element
for i in result:
    print(i,end=" ")

