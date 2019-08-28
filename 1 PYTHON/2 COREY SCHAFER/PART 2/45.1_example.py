# how many weeks it will take us to loose a certain number of pounds
# the example in pounds if u want in kgs then make a conversion on that

import datetime

current_weight = 220
goal_weight = 160
avg_lbs_week = 3


start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week
print(end_date)
print(f"Reached goal in {(end_date-start_date).days// 7} weeks")
