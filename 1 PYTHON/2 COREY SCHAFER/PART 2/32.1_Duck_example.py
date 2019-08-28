#person = {"name": "John", "age": 29, "job": "Programmer"}
#person = {"name": "Jess", "age": 25}

# LBYL(Non-Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("Iam {name}.Iam {age} years old am Iam a {job}".format(**person))
# else:
#     print("Missing some keys")

# EAFP(Pythonic)easy to ask forgiveness than peermission

# try:
#     print("Iam {name}.Iam {age} years old am Iam a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))


my_list = [1, 2, 3, 4, 5, 6, 7]

# Non Pythonic
# if len(my_list) >= 6:
#     print(my_list[8])
# else:
# 	print("index out of range")

# Pythonic
try:
    print(my_list[50])
except IndexError:
    print("That index does not exist")
