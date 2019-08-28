# Error Handling in Python

# code standard for handling errors in python

# try:
#     pass
# except Exception:
#     pass
# else:
#     	pass
# finally:
#     	pass

import os
# customise exception
# try:
# 	f = open("testfile.txt")
# except Exception:
# 	print("Sorry.file does not exist")

# Python regular trackback exception
# try:
#     f = open("31.1_test_file.txt")
#     var = bad_var
# except FileNotFoundError:
#     print("Sorry.file does not exist")
# except Exception:
# 	print("Sorry,Something wrong")


# try:
#     f = open("31.1_test_file.txt")

# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)


# now else block ok else block will be execute if try block does not get an error then it will get execute

# try:
#     f = open("31.1_test_file.txt")

# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
# 	print("Executing Finally...irespective of whether code get successfully run or might throw an error does not matter")


# try:
#     f = open("31.2_corrupt_file.txt")
#     # if f.name == "31.2_corrupt_file.txt":
#     #     raise Exception
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print("Error")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally...irespective of whether code get successfully run or might throw an error does not matter")
