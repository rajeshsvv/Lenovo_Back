# program for to search an element from list

list=[5,8,4,6,9,2]

n=2

pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1

if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")