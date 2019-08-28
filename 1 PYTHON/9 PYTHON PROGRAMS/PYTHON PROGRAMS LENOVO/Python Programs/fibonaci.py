def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)


for n in range(1,11):
    print(n,"fibonaci value:",fib(n))

# print(fib(9))