
courses = ["History", "Maths", "Physics", "Computer"]
courses_2 = ["Education", "Healthcare"]

'''   slicing
print(courses)
print(len(courses))
print(courses[0:3])
print(courses[:3])
print(courses[3:])
print(courses[-1])
# index out of range exception ok print(courses[5])
'''

# Methods
# 1 to add an value
courses.append("Art")
print(courses)
courses.insert(0, "Harman")
print(courses)
courses.append(courses_2)
print(courses)
courses.insert(0, courses_2)
print(courses)
courses.extend(courses_2)
print(courses)
courses.remove("Art")
print(courses)
poped = courses.pop()
print(poped)  # pop method delete the item from the last one this is useful wih stack and queue to store values
courses.reverse()
print(courses)

courses = ["History", "Maths", "Physics", "Computer"]
nums = [1, 6, 2, 9, 8, -190, 32]
courses.sort()
print(courses)  # sort means make it in words in alphabatical order
nums.sort()
print(nums)

courses.sort(reverse=True)
print(courses)  # it makes descending order ok
nums.sort(reverse=True)
print(nums)

sorted_numbers = sorted(nums)
print(sorted)
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses)
print(courses.index("History"))
print("Art" in courses)
print("History" in courses)
Degree = ["Commerce", "Maths", "Physics", "Computer"]
for item in Degree:
    print(Degree)

Degree = ["Commerce", "Maths", "Physics", "Computer"]
for index, item in enumerate(Degree):
    print(index, Degree)

print()

Degree = ["Commerce", "Maths", "Physics", "Computer"]
for index, item in enumerate(Degree, start=1):
    print(index, Degree)

Degree_string = "- ".join(Degree)
print(Degree_string)
new_list = Degree_string.split("- ")
print(new_list)
