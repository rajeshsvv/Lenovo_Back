number1=int(input("Enter a number1:"))
number2=int(input("Enter Number2:"))
result=number1/number2
try:

    if number2==0:
        print("cannot devide by zero")
except ZeroDivisionError:
        print("cannot divided by zero")
except ValueError:
        print("Enter correct data format")

else:
    print(result)
