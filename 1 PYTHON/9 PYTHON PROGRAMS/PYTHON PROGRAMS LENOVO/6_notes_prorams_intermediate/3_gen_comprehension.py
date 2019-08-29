nums=[1,2,3,4,5,6,7,8,9]

def generate_fun(nums):
    for i in nums:
        yield i*i
result=generate_fun(nums)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for i in result:
    print(i,end=" ")