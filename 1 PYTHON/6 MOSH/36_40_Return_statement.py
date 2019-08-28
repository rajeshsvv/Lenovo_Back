# 36 Return Statement   2:45:00



'''

def square(number):
    # print("result",number)
    return number*number

# print(square(3))
# result=square(3)
# print(result)
# square(3)
print(square(3))          # we get none here also

'''
#       37 Create Reusable function       2:49:06
'''
def emoji_converter(message):
    word=message.split(" ")
    # print(words)                # Hi Dear      o/p: ['Hi', 'Dear']

    emojis={
        ":)":"\U0001F602",
        ":(":"\U0001F603"
    }
    output=""
    for word in word:
        output+=emojis.get(word,word)+" "
    # print(output)       # u get None here because by default function returns none value if we dont specify that
    return output

message=input(">")
emoji_converter(message)

#one way store the result in variable and call the variable
# result=emoji_converter(message)
# print(result)

#alternative way directly call the function
print(emoji_converter(message))
emoji_converter(message)

'''


#       38 Exceptions       2:53:54



# without exception handling case(it will throw error if u enter words instead of numbers)
# age=int(input("Enter Age:"))
# print((age))

'''
try:
    age=int(input("Enter Age:"))
    income=20000;
    risk=income/age
    print("age",age)
    print("risk",risk)
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("Enter Age in digits only")
'''

#   39    COMMENTS  2:59:35
# we use comments to add notes or comments to our program.
# comments are good but too much of good thing is a bad thing.  

# this is comment part
print("this is comment")


#   40 Classes      3:01:46

class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.move()
point1.draw()

point2=Point()
point2.x=30
print(point2.x)