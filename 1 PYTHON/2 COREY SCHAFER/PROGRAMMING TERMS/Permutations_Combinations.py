import itertools

# COMBINATIONS

my_list=[1,2,3]
# result=itertools.combinations(my_list,2)
# for c in result:
#     print(c)

# PERMUTATIONS

# result=itertools.permutations(my_list,2)
# for p in result:
#     print(p)

# combination and permutation for geoup of numbers whose sum was 10

my_list=[1,2,3,4,5,6]

combinations=itertools.combinations(my_list,3)
permutations=itertools.permutations(my_list,3)

value=print(result for result in combinations if sum(result)==10)




