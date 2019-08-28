def add(x,y):
    sum=x+y
    return sum

def main():
    # x=input("Enter first Number:")                  # returns string concatenation output
    # y=input("Enter second number:")                 # returns string concatenation output
    x=int(input("Enter first Number:"))           # return add int numbers
    y=int(input("Enter second number:"))          # return add int numbers
    z=add(x,y)
    print(z)

if __name__=="__main__":
    main()





