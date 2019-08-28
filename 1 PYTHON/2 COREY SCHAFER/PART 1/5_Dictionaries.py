# Dictionaries these are work with key value pairs okay

student = {"name": "Corey", "age": 25, "courses": ["Python", "DJango"]}


# print(student["name"])
# print(student["age"])
# print(student["courses"])


# student["Phone"] = "5555-5555"
# student["name"] = "Shinde"
# print(student)

student.update({"name": "Schafer", "age": 50, "Phone": "4444-5555"}); print(student)

# del student["age"]
# age = student.pop("age")
# print(student)

# print(age)
# print()
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())
# print()

# print(student["Phone"])

# print(student.get("name"))
# print(student.get("Address"))
# print(student.get("Address", "Not Found"))
# print()


# for key in student:
#     print(key)
# print()

for key, value in student.items():
    print(key, value)
print(student)
