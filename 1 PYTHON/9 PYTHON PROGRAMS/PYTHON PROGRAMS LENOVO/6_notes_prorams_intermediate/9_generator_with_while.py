def print_num(n):
    i=1
    while i<=n:
        yield i**2
        i+=1

for i in range(10):
    print(i,end=" ")
print('---')


# print odd numbers with the help of generators

def odd(n):
    odd=[i for i in range(n) if i%2!=0]
    for i in odd:
        yield i

for i in odd(9):
    print(i,end=" ")
