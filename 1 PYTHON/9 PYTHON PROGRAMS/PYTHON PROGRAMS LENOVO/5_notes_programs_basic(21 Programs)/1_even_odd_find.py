'''
def find_even(list):
    # even,odd=0,0
    even=0;odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


list=[1,2.3,4,5,6,7]
even,odd=find_even(list)
print(even)
print('--')
print(odd)
'''


def find(list):
    even=0;odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

list=[10,9,8,7,6,5,4,3,2,1,17]
even,odd=find(list)
print(even)
print(odd)