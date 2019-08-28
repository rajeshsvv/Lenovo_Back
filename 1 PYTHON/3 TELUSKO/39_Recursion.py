# Calling a function itself is known as Recursion

import sys                           # to know the limit of the recursion
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())

i=0

def greet():
    global i
    i+=1
    print("Hell",i)
    greet()

greet()