# how to create multiple python build systems within sublime text so that browse we can run python 2 and python 3
# this will be useful switch between different versions of python

# {
#     "cmd": ["C:/Users/raji/AppData/Roaming/Sublime Text 3/Packages/User/python3.7", "-u", "$file"],
#     "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
#     "selector": "source.python"
# }

# import time

# for i in range(2):
#     print("Hello World")
#     time.sleep(5)


import sys
print(sys.executable)

# output python path note this C:\ProgramData\Anaconda3\python.exe this is python 3 code so we have to set build system to python 3.5 ok

# import sys
# print sys.executable

# # output python path note this C:\ProgramData\Anaconda3\python.exe this is python 2 code so we have to set build system to python 2.7 ok
