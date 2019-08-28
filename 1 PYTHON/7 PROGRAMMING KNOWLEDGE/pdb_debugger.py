import pdb              # this is the second way to use pdb 1st is through command prompt.
def add(x,y):
    sum=x+y
    return sum
    # return x+y
    # print("Addition:",x+y)

def main():
    x=int(input("Enter first Number:"))
    y=int(input("Enter second number:"))

    # pdb.set_trace()
    # import pdb;pdb.set_trace()        # second way
    z=add(x,y)
    print(z)

if __name__=="__main__":
    main()