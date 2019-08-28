def count(list):
    even=0
    odd=0

    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

list=[10,20,30,40,50,60,11,21,31,41,51,66]

even,odd=count(list)

print(even)
print(odd)

print("Even:{} and Odd:{}".format(even,odd))
