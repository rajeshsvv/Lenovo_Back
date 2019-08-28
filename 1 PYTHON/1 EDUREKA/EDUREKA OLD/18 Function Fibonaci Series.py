#Fibonaci series program in python using function

def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=a+b
        print(a)
    return b
num=int(input("Enter the value of n:"))
print(fibo(num))