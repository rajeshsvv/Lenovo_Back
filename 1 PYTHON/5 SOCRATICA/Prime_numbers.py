import time


def is_prime(n):
    """Return True if n is prime number otherwise it is false"""
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
        return True


# time function
t0 = time.time()
for n in range(1, 10):
    print(n, is_prime(n))
t1 = time.time()
print("Time Required:", t1 - t0)
