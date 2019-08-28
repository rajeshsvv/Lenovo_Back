tup1=("Zoho","Yellow","Xman","50000")
print(len(tup1))
print(max(tup1))
print(min(tup1))

tup2=(1,2,3,4,5,-5,-4,-3)
print(sorted(tup2))

tuple=([0,1,2],[2,3,4],[4,5,6])
# tuple[0]=100
# tuple[0][0]=0
# print(tuple)

for item in tuple:
    print(tuple(item))
    print(item)