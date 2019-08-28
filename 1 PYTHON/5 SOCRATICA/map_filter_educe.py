"""Map function"""
# import math


# def area(r):
#     return math.pi * (r**2)


# radii = [2, 5, 7.1, 0.3, 10]

# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)

# print(areas)

# # with map function

# # s = map(area, radii)			#it is map object which is actually iterate over the results
# s = list(map(area, radii))
# print(s)


# Filter function

# import statistics

# data = [1.3, 2.7, .8, 4.1, 4.3, -0.1]
# avg = statistics.mean(data)
# print(avg)

# # result = filter(lambda x: x < avg, data)	#it traverse through the object
# # print(result)
# result = list(filter(lambda x: x < avg, data))
# print(result)
# result = list(filter(lambda x: x > avg, data))
# print(result)


# Reduce functon

from functools import reduce

# Multiply all numbers in a list

data = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def multiplier(x, y): return x * y


p = reduce(multiplier, data)
print(p)


product = 1
for x in data:
    product = product * x

print(product)
