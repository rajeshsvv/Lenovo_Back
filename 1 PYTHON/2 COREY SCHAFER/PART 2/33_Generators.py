# Generators have advantages over Lists


# Actual way to find the square root of the numbers
# def sqaure_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


# my_numbers = sqaure_numbers([1, 2, 3, 4, 5])
# print(my_numbers)


# through Generator we can find the square root of the numbers
# Generators don't hold entire list in memory it gives one by one result

# def sqaure_numbers(nums):

#     for i in nums:
#         yield(i * i)


# my_numbers = sqaure_numbers([1, 2, 3, 4, 5])
# print(my_numbers)  									# it generates object instead of ressult
# # print(next(my_numbers))				#
# # print(next(my_numbers))
# # print(next(my_numbers))
# # print(next(my_numbers))
# # print(next(my_numbers))

# # instead of use next keyword create for loop so it will give line by line output

# for num in my_numbers:
#     print(num)


# simplify the above code in list comprehension way k

# my_numbers = [i * i for i in [1, 2, 3, 4, 5]]  # list comprehension way  u will get print(my_numbers) result also

# print(my_numbers)


my_numbers = (i * i for i in [1, 2, 3, 4, 5])  # list comprehension way for generatos.u dont get print(my_numbers) result here.for loop requird
print(list(my_numbers))  # if we add list to my numbers then no need of  for loop we get result k
