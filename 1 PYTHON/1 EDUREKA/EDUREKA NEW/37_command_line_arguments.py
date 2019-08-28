import sys

# print(sys.argv)
print(len(sys.argv))            # returns 1 because file name was calculated first.



#   38 sequence and File Operations 1:00:28
# str=input("Enter your input:")
# print("Received input is --",str)

name=input("Enter your name:")
age=input("Enter your Age:")
print("Welcome-",name)
print("Your Age was-",age)

print("After 5 years your age will be",(int(age)+5))
# print(f"Name was-{name} and the age was-{age}")