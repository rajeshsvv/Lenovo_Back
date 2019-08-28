lucky_numbers=[1,2,3,4,5,6,7,87,9]
friends=["Arjun","Arjun","Sudheer","Krushna","Govind"]
print(friends.append("Dhanujaya"))
print(lucky_numbers)
friends.extend(lucky_numbers)
# print(friends.sort())
print(lucky_numbers.sort())
print(friends.insert(2,"Sumathi"))

print(friends)
print(friends.pop())
print(friends.index("Sudheer"))
print(friends.index("Arjun"))
print(friends.count("Arjun"))

print(lucky_numbers.reverse())
friends2=friends.copy()
print(friends2)
print(friends.remove("Govind"))
print(friends.clear())