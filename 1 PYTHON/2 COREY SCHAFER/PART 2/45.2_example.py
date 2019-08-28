"""
scenario corey have a youtube channel to hit a certain number of subscribers here on youtube and 
would llike to see how long it will take to reach that goal

"""


import datetime
import math

# math module is for ceiling the calculations ceil -round up to the next value

current_subs = 85000
goal_subs = 100000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)

today = datetime.date.today()
print(today, datetime.timedelta(days=days_to_go))
print(today + datetime.timedelta(days=days_to_go))
