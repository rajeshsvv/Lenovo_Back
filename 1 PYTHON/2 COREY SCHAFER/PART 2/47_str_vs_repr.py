# difference between str() vs repr()
"""
when a variable contains a string then str gives without quoted string
while repr gives with quoted string

The goal of __repr__ is to be unambiguous      for developers perspective debug and get the value in debug case it show string and datetime
The goal of __str__ is to be readable			for non developers perspective just returns a string 
"""

"""
a = [1, 2, 3, 4]
b = "sample string"

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

"""


import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# a = datetime.datetime.today()
b = str(a)

print(f"str(a):{str(a)}")
print(f"str(b):{str(b)}")

print()


print(f"repr(a):{repr(a)}")
print(f"repr(b):{repr(b)}")
