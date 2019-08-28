import sys

#import Find_index9 as fi
# import the function itself this is only for find_index function if u want text variable access into this module then add text like below
#from Find_index9 import find_index
from Find_index9 import find_index, text

# from Find_index9 import *  # it will give access to all variables in Find_index9 module but dont use okay

courses = ["History", "Maths", "Physics", "Arts"]

# index=fi.find_index(courses,"Arts")
index = find_index(courses, "Arts")

print(index)
# print(text)

print(sys.path)
