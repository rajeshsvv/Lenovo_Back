'''
import sys
randomlist=['a',2]
for entry in randomlist:
    try:
        print("The entry is",entry)
        r=1/int(entry)
        break
    except:
        print("OOPS",sys.exc_info()[0],"occurred")
        print("Next Entry")
        print()
print("The reciprocal of",entry,"is",r)
'''

#define python user defined exceptions
class Error(Exception):
    "Base class for other exceptions"
    pass

class ValueSmallError(Error):
    "Raised when the input value is too small"

class ValueLargeError(Error):
    "Raised when the inout value is too large"
    pass

number=10
while True:
    try:
        in_num=int(input("Enter Number:"))
        if in_num<10:
            raise ValueSmallError
        if in_num>10:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("This value is too Small,try again")
    except ValueLargeError:
        print("This value is too Large,try again")
        print()

print("Congratulations.You guessed it correctly")