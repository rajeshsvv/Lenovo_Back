

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums.insert(0, 50)
nums.append(97)

print(nums)
nums.remove(97)
nums.remove(50)
print(nums)
nums.pop()
print(nums)

del nums[1:]
print(nums)

nums.extend([15, 25, 35, 45])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
