# 21 Build Guess Game(its secret number u have to guess k within 3 times option after that it failed k) 1:24:07

'''
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess:"))
    guess_count+=1
    if guess==secret_number:
        print("You Won in this Game")
        break
else:
     print("Better Luck next time")
'''


#       22 Build A Car Game         1:30:51

# ""====> Empty String
"""
command=""
while True:
# while command!="quit":
    command=input(">").lower()
    if command=="start":
        print("Car Started")
    elif command=="stop":
        print("Car Stopped")
    elif command=="help":
        print('''
start=to start the Car
stop=to stop the Car
quit=to quit
        ''')
    elif command=="quit":
        break
    else:
        print("Sorry We don't understand that")
"""

# Excersize on Car Game

'''
command=""
started=False

while True:
# while command!="quit":
    command=input(">").lower()
    if command=="start":
        if started:
            print("Car is already Started:")
        else:
            started=True
            print("Car Started")
    elif command=="stop":
        if not started:
            print("Car is already Stopped")
        else:
            started=False
            print("Car Stopped")

    elif command=="help":
        print("""
start=to start the Car
stop=to stop the Car
quit=to quit
        """)
    elif command=="quit":
        break
    else:
        print("Sorry We don't understand that")
'''

#       23  FOR LOOPS      1:41:00

'''
for item in "Python":
    print(item)
print("\n")

for item in ["John","Mosh","Khan"]:
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in range(1,10):
    print(item)


for item in range(5,10):
    print(item)


for item in range(5,10,2):          # 2 is step like start stop ok increment the number with 2
    print(item)
'''

'''
prices=[10,20,30]
total=0
for price in prices:
    total +=price
print(f"Total {total}")
'''


#     24  Nested For Loop       1:47:46

'''
for x in range(4):
    for y in range(3):
         # print(x,y)
         print(f"({x},{y})")

for i in [5,2,5,2,2]:
    print('x'*i)
'''

'''
numbers=[5,2,5,2,10]

for x_count in numbers:
    output=""
    for count in range(x_count):
        output+="x"
    print(output)
'''


#    25   LISTS             1:55:50

# names=["John","Bob","Mosh","Sarah","Maria"]
# print(names)
# print(names[0])
# print(names[1])
# print(names[-1])
# print(names[-2])
# print(names)
# print(names[2:])
# print(names[2:4])
# print(names[:])                 # [] in the sense dont modify the original list they simply return a new list



# find the largest number in the list


numbers=[-50,-60,-70,-80,-90,10]
max=numbers[0]
for number in numbers:
     if number>max:
         max=number

print(number)
print(min(numbers))

