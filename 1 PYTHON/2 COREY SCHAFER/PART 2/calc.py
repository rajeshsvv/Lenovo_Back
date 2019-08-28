# unit testing in python
# unit test module is in standard library so there is no need to insatll anythingyou can just say import unittest
# to create test case first we need to create test class  that inherits from unittest.testcase
# floor division in the sense it does not give the remainder


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        raise ValueError("cannot devided by zero")
    return x / y
    # return x // y 				this is called floor division means it does not give remainder for example 5//2=2.5 but it gives 2 only  got it


# print(mul(5, 2))
