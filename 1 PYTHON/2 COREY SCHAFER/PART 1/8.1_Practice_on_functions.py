# number of days per month.First value place holder for indexing purposes

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	""" called doc string is useful for classes and functions suppose to what to do"""
	""" Return true for leap years and False for non leap years"""

	return year%4==0 and (year%100 !=0 or year%400==0)


def days_in_month(year,month):
	# return number of days in that month and in that year

	#checking purpose year 2017 and month 2
	if not 1<=month<=12:
		return "invalid Month"

	if month==2 and is_leap(year):
		return 29

	return month_days[month]

print(days_in_month(2012,2))
print(is_leap(2015))
