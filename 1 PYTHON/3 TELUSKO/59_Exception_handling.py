a=5
b=1


try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a Number"))
    print(k)


except ZeroDivisionError as e:
    print("You cannot divide the number by zero",e)

except ValueError as e:
    print("Invalid Input",e)

except Exception as e:
    print("Something went wrong",e)

finally:
    print("resource closed")
print("Bye")