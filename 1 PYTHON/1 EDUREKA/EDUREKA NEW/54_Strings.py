'''
str1="Welcome"
str2="to"
str3="Edureka"

print(str1)
print(str2)
print(str3)

string="Python"

print(string)
print(len(string))
print(string[1:3])
print('t' in string)
print('z' in string)

str2=('a','b','c','d','e')
# str2[3]='1'
print(str2)
'''

print("Welcome to %s.Have a good day" %("python"))
                # instead of this
course_name="Java"
print("Welcome to"+" "+course_name+" "+"Enter into the Course")


name="Ajit"
age=22
print("My name is "+name+" my age is "+str(age))        # if u dont case age to str u get an errror k.


string="RajeshlovesPython"
s=string.encode('utf-8',"strict")
print(s)