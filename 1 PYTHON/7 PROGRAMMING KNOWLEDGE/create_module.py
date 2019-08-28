def add(a,b):
    # print(a+b)
    return a+b


def mul(a,b):
    # print(a*b)
    return a*b


if __name__=="__main__":
    print("this is main file")
    print("From Name:",__name__)

from collections import namedtuple

result=namedtuple('result',"Physics,Chemistry,Maths")
ayushi=result(Physics=89,Chemistry=60,Maths=100)
print(ayushi.Maths)


