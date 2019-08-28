

list1=[i for i in range(-2,16,2) if i>10]
print(list1)
print("---")

list2 = [(x,x**2,y) for x in range(1,5) for y in range(2,4)]
print(list2)



list3=[[1 for i in range(3)] for j in range(5)]
print(list3)
