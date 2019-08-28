
def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


nums = [5, 3, 8, 6, 7, 2, 56, 44, -8, -2, -96538]
sort(nums)
print(nums)
