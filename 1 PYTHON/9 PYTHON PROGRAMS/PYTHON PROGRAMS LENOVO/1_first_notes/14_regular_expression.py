import re
string="rajeshsvv01@gmail.com"
e=re.search(r'[0-9a-zA-Z]+@[a-zA-Z]+\.(com|co\.in)$',string)
print(e.group())

a=0
while a<10:
    a+=1
    print(a)
