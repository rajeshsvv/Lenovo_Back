# without try except block
'''
result=None
a=float(input("Enter first Number:"))
b=float(input("Enter second number:"))

result=a/b
print(result)
print("End")
'''

# with try except block
'''
result=None
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
try:
    result=a/b
except:
    print("float division by zero")

print("result",result)
print("End")
'''

# try except else finally case
'''
result=None
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
try:
    result=a/b
except:
    print("float division by zero")
else:
    print("result",result)
finally:
    print("End")
'''

# try except with base exception class
'''
result=None
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
try:
    result=a/b
except Exception as e:
    print("Error=",type(e))
else:
    print("result",result)
finally:
    print("End")
'''

# try except with more except block to handle more errors don't mention  base Exception class it is not good practice
result=None
a=float(input("Enter first Number:"))
b=float(input("Enter second Number:"))

try:
    result=a/b
except ZeroDivisionError as e:
    print("ZeroDivisionError=",e)
except TypeError as e:
    print("ValueError=",e)
except ValueError as e:
    print("ValueError",e)
finally:
    print("result",result)
    print("end")