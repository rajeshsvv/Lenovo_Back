'''
list=[1,2,3,4,5,6,7,8,9]
list.pop()
print(list)
print(list.pop(1))
print(list)

print(list.pop(6))
print(list)
'''


# 50    LIST COMPREHENSION        1:22:49

list=[]
for x in [1,2,3,4,5]:
    list.append(x**2)
print(list)

            #   or

'''
list=[x**2 for x in [1,2,3,4,5]]
print(list)
list.insert(5,36)
print(list)

list=["Zoho","Uber","Ola","flipcart"]
s=sorted(list)
print(s)

for course in list[::-1]:
    print(course)
'''


list=[(1,2,3),("Python","Java")]
print(list)
print(len(list))
# list[0][1]=40
print(list)
del(list)
print(list)
