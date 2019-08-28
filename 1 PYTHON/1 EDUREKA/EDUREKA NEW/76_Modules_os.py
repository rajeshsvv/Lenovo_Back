import os

import math
# print(dir(os))

'''
print(os.name)                  # return the name of the operating system
# print(os.environ)             #   return the mapping object represent the string environment.
print(os.getlogin())            # return the name of the user logged in on the controlling terminal of the process
print(os.getppid)               # return th parent process id
print(os.getcwd)                   # cwd means current working directory.
# print(os.chdir("d:/python"))
'''

print(os.path.join('G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW/Edureka.txt',
                   'G:\4 PYTHON\PRACTICE\BACKEND\1 PYTHON\1 EDUREKA\EDUREKA NEW\Edurekha.txt'))

print(os.path.abspath("76_Modules_sys.py"))     # it takes the relative path and gives the absolute path name.
print(os.path.abspath("oneforuthree.txt"))

print(os.path.normpath('G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW/76_Modules_os.py'))
print(os.path.normpath('G:\4 PYTHON\PRACTICE\BACKEND\1 PYTHON\1 EDUREKA\EDUREKA NEW\76_Modules_os.py'))
print(os.path.split("G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW/67_Polymorphism.py"))
print(os.path.exists("G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW/76_Modules_os.py"))
print(os.path.exists('G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW/76_Modules.py'))
print(os.path.isdir("G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW"))
print(os.walk("G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW"))

for i in os.walk("G:/4 PYTHON/PRACTICE/BACKEND/1 PYTHON/1 EDUREKA/EDUREKA NEW"):
    print(i)