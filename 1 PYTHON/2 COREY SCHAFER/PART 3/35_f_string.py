first_name="rajesh"
last_name="venkat"

# fullname='My Name is {}.{}'.format(first_name,last_name)
# print(fullname)
#
#
# sentence1=f'My Name is {first_name} {last_name}'
# print(sentence1)
#
#
# sentence2=f'My Name is {first_name.upper()} {last_name.lower()}'
# print(sentence2)

person={"name":"John","age":28}
details='My name is {} have {} years old'.format(person["name"],person["age"])
print(details)

person1=f"My name is {person['name']} have {person['age']} years old"

# we can also calculations with f strings

calculation=f"4 times 11 equal to: {4*11}"
calculation=f"4 divided by 11 equal to: {4/2}"
print(calculation)



# for n in range(1,11):
#     sentence=f'the value is {n}'                      #print like numbers 1,2,3,4
#     sentence=f'the value is {n:02}'                    #print like numbers 01,02,03,04
#     print(sentence)

pi=3.145689745
value=f'Pi value equal to {pi:.2f}'
print(value)

from datetime import datetime

birthday=datetime(1990,1,1)
date=f'birthday date was {birthday}'
date=f'birthday date was {birthday:%B,%d,%Y}'
print(date)
