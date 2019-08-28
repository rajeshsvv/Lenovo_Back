'''
result=None
a=float(input("Enter first Number:"))
b=float(input("Enter second Number:"))

try:
    result=a/b
except ZeroDivisionError as e:
    print("ZeroDivisionError=",e)
except TypeError as e:
    print("ValueError=",e)
else:
    print("result",result)
finally:
    print("end")
'''

# finally block executed irrespective of exception block

result=None
a=float(input("Enter first Number:"))
b=float(input("Enter second Number:"))

try:
    result=a/b
except ZeroDivisionError as e:
    print("ZeroDivisionError=",e)
except TypeError as e:
    print("ValueError=",e)
else:
    print("__else__",result)
finally:
    print("__finally__","end")
