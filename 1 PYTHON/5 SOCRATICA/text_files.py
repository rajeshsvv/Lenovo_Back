# help(open)
# print(dir(open))
import os

# f = open("F:\\4 PYTHON\\THEORY\\1 PYTHON\\4 TELUSKO\\Telusko Python Index Link URL.txt")
# with open("F:\\4 PYTHON\\THEORY\\1 PYTHON\\4 TELUSKO\\Telusko Python Index Link URL.txt") as f:
#     text = f.read()
# # f.close()

# print(text)


# write the file

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arcitic"]
with open("oceans.txt", 'w') as write:
    for ocean in oceans:
        print(ocean, file=write)
with open("oceans.txt", 'a') as append:
    print(23 * "=", file=append)
    print("this is appended at the end", file=append)
