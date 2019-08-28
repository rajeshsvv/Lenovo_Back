def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(5))


# using recursion

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))

