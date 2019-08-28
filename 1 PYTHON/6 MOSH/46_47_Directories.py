#  46     DIRECTORIES   3:44:37

# how to work with directories in python 3 module index,module called pathlib provide object oriented file system.
# it means it provides classes that we can use to create objects to work with directories and files.

from pathlib import Path

# we need to create path object to reference a file or directory on our computer.(root of our hard disk)
# two ways we can do this
#                                  1 absolute path
# on windows we use backslash(\) to build a path.(3:46:46)  c:\Program Files\Microsoft
# in mac or linux it is different use forward slash(/)      /usr/local/bin

#                          2 relative path(startig from the current directory)

# glob method o search files
# mkdir shortcut to create a new directory
# rmdir shortcut to remove the directory

p=Path('ecommerce')
# print(p.exists())
# print(p.mkdir())
# print(p.rmdir())
for file in p.glob("*.*"):
    print(file)




#       47 PYPY & PIP           3:50:47


