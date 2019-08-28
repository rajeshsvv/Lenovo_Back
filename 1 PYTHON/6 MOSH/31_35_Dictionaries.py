#       31 Dictionaries             2:18:21

# store info in key value pairs

"""
customer={
    "name":"John",
    "age":30,
    "is_verified":True
}

print(customer["age"])
# print(customer["birthdate"])            #keyerror does not exist
# print(customer["Name"])
print(customer.get("Name",None))
customer["name"]="Michael"
print(customer["name"])
customer["birthdate"]="Jan 1 1990"
print(customer["birthdate"])

"""

# program on dictionary enter numbers it converts into words k


phone=input("Enter numbers:")
digit_mapping={
    "1":"One",
    "2":"Two",
    "3":"Threee",
    "4":"Four",
    "5":"Five" 
}
output=""
for ch in phone:
    output+=digit_mapping.get(ch,"!")+" "
print(output)



#  32 Emoji Converter(https://unicode.org/emoji/charts/full-emoji-list.html)        2:26:21


message=input(">")
word=message.split(" ")
# print(words)                # Hi Dear      o/p: ['Hi', 'Dear']

emojis={
    ":)":"\U0001F602",
    ":(":"\U0001F603"
}
output=""
for word in word:
    output+=emojis.get(word,word)+" "
print(output)



#   33  FUNCTIONS           2:30:31

"""

def greet_user():
    print("Hi")
    print("Greet Message")

print("Start")
# greet_user
# print(greet_user)
# print(greet_user())
greet_user()
print("Finish")

"""

#   34 PARAMETERS        [passing parameters to functions]

'''
def greet_user(name):
    # name="John"
    print(f"Hi {name}")
    print("Greet Message")

print("Start")
# greet_user
# print(greet_user)
# print(greet_user())
greet_user("Shalini")
greet_user("Ravindra")
print("Finish")
'''

'''
def greet_users(first_name,last_name):
    print(f"Hello {first_name} {last_name} !")
    print("Welcome to India")

print("start")
greet_users("John","Michael")
print("End")
'''

#  35 Keyword Arguments     2:39:24 [keyword argument should come after positional arguments remember this]

'''
def greet_users(first_name,last_name):
    print(f"Hello {first_name} {last_name} !")
    print("Welcome to India")
'''

print("start")
# greet_users(last_name="John","Michael")
print("End")

# keywords example=(50,5,0.1)       No one can understand which value is for which key
# keywords example=(total=50,shipping=5,discount=.1)