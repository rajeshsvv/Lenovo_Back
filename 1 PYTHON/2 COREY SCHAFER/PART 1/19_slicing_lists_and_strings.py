# slicing in the sense its a way for us to extract certain elements from lists and strings
"""
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 +ve index
# -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 -ve index
print(my_list[1])

print(my_list[0:9:1])
print(my_list[0:9:2])
print(my_list[0:9:3])
print(my_list[0:9:4])
print(my_list[0:9:5])
print(my_list[0:9:6])
print(my_list[0:9:7])
print(my_list[0:9:8])
print(my_list[0:9:9])
print(my_list[0:8:3])
print(my_list[1:])
print(my_list[::1])
print(my_list[::-1])
"""
# slicing the strings

sample_url = "http://coreyms.com"
print(sample_url)

# Reverse the url
print(sample_url[::-1])
print(sample_url[::1])

# Get the top level domain
print(sample_url[-4:])

# print the url without http
print(sample_url[7::])

# print the url without http:// or the top level domain
print(sample_url[7:-4])
