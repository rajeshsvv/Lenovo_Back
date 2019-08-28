"""
person = {"name": "John", "age": 23}
l = ["John", 23]
sentence = 'My name is ' + person['name'] + " and Iam " + str(person['age']) + " years old."
#sentence = "My name is {} and Iam {} years old".format(person['name'], person['age'])  # {}is like place holder got it
#sentence = "My name is {0} and Iam {1} years old".format(person['name'], person['age'])
#sentence = "My name is {0[name]} and Iam {1[age]} years old".format(person, person)
#sentence = "My name is {0[name]} and Iam {0[age]} years old".format(person)
sentence = "My name is {0[0]} and Iam {0[1]} years old".format(l)

tag = "hi"
text = "This is Head Line"

#sentence = "<{0}>{1}</{0}>".format(tag, text)
print(sentence)
"""

# dictionaries
"""
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Ajit", "30")
sentence = "My name is {0.name} and Iam {0.age}  years old".format(p)
print(sentence)
"""

# we can also pass keyword arguments into format

sentence = "My name is {name} and Iam {age} years old".format(name="John", age="30")
print(sentence)

person = {"name": "John", "age": 23}
sentence = "My name is {name} and Iam {age} years old".format(**person)  # kwargs keyword arguments
print(sentence)

person = ["John", 23]
sentence = "My name is {0} and Iam {1} years old".format(*person)  # args position argument
print(sentence)


# how we can format na dprint out numbers
"""
for i in range(1, 11):
    # sentence = "The value is {}".format(i)
    sentence = "The value is {:03}".format(i)
    print(sentence)
"""

# format for decimal places
"""
pi = 3.1456895654589

sentence = "Pi equal to {:.2f}".format(pi)
print(sentence)
"""
# print out a large number
"""
sentence = "1 mb equal to {:,}".format(1000 * 2)
sentence1 = "1 mb equal to {:,} bytes".format(1000 ** 2)
sentence2 = "1 mb equal to {:,.2f} bytes".format(1000 ** 2)
print(sentence)
print(sentence1)
print(sentence2)
"""

# format and print out the dates
import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# May 01,2016 i want to print like this

sentence = '{:%B %d,%Y}'.format(my_date)  # %B in the sense month it is
print(sentence)

# March 01 2016 fell on Tuesday and was the 061 day of the year

sentence = '{0:%B %d,%Y} fell on a {0:%A} and was the {0:%j} of the year'.format(my_date)  # for day %A and for date %j
print(sentence)
