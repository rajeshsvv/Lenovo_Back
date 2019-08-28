import datetime

# d = datetime.date(2018, 9, 26)
# print(d)
today = datetime.date.today()
print(today)
# print(today.year)
# print(today.day)


# #Monday 0 Sunday 6  weekday
# #Monday 1 Sunday 7  isoweekday

# print(today.weekday())
# print(today.isoweekday())

# tdelta means 7 days from today date now
# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)
# print(today - tdelta)

# date2=date1+tdelta
# tdelta=date1+date2

bday = datetime.date(1990, 1, 8)  # dont put 0s on month or days k otherwise u will get invalid token error
# till_bday = bday - today
till_bday = bday - today
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())


# t = datetime.time(21, 30, 45, 60)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# dt = datetime.datetime(2018, 9, 26, 21, 50, 36, 58)

# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)
# tdelta = datetime.timedelta(days=6)
# tdelta = datetime.timedelta(hours=96)
# print(dt + tdelta)


# dt_today = datetime.datetime.today()  #returns current local date time with time zone of none
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

import pytz 							# pytz for UTC timezones okay it has seperate url for pytz to work with

# dt = datetime.datetime(2018, 9, 26, 22, 10, 00, tzinfo=pytz.UTC)
# print(dt)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_now = datetime.datetime.now(tz=pytz.UTC)							# most used corey schafer ok got it
# print(dt_now)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

#dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
#dt_mtn = dt_utcnow.astimezone(pytz.timezone("Asia/Calcutta"))
# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)


#dt_mntn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))

# mtn_tz = pytz.timezone("US/Mountain")
# dt_mntn = mtn_tz.localize(dt_mntn)
# dt_east = dt_mntn.astimezone(pytz.timezone("US/Eastern"))
# print(dt_east)
# print(dt_mntn)

# astimezone() cannot be applied to naive datetime


# dt_mntn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
# print(dt_mntn.isoformat())
# print(dt_mntn.strftime("%B %d, %Y"))  # %B for month %d two digit day

# dt_str = "September 26, 2018"
# dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
# print(dt)


# strfitme-datetime to string
# strpitme-string to datetime
