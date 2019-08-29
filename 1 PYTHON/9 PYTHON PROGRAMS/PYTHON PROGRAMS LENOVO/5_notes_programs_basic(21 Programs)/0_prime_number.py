
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num,end=" ")


# Python Program to print Prime Numbers from 1 to N using For Loop
'''


first=int(input("Enter first number:"))
last=int(input("Enter last number:"))

if __name__=="__main__":

    for num in range(first,last+1):
        count=0
        for i in range(2,(num//2+1)):
            if num%i==0:
                count=count+1
                break

        if (count==0 and num!=1):
            print("%d" %num,end=",")
'''

'''
# Python Program to print Prime Numbers from 1 to N using While Loop


minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

Number = minimum

while (Number <= maximum):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
    Number = Number + 1
'''

