def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i-=1
    return False
list=[1,2,3,4,5,6,7,8,9]
n=8

# print(search(list,10))
if search(list,n):
    print("Found Number",n)
else:
    print("Number not found")


