import datetime
print(datetime.datetime.today())

now=datetime.datetime.today()
other=datetime.datetime(1990,8,1,22,10)
print(now-other)
datetime.timedelta(18901,55547,410000)
print(now-other)

print(datetime.MAXYEAR)             # returns the largest year number allowed in the date or datetime object maxyear is 9999
print(datetime.MINYEAR)             # returns the largest year number allowed in the date or datetime object maxyear is 1
print(datetime.time())              # return the time object with hour minute second and microsecond
print(datetime.timezone)            # returns a timezone object         work with some systems does not work with some other systems.