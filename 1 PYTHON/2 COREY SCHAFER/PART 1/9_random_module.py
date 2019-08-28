import random       # select random options from collection of items
import math 	 	# for mathematical calculations
import datetime 	# for dates and times
import calendar
import os			# give access for underlying operating systems

courses = ["History", "Maths", "Physics", "Arts"]

random_courses = random.choice(courses)
print(random_courses)


rads = math.radians(90)

print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2018))
print(os.getcwd())
print(os.__file__)
