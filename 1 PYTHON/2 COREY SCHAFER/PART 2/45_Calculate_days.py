# write a script to calculate the number of months that it would take to pay off a credit card

import datetime
import calendar

balance = 2000
interest_rate = 0.6
monthly_payment = 500

today_date = datetime.date.today()
# print(today_date)

days_in_current_month = calendar.monthrange(today_date.year, today_date.month)[1]
# print(days_in_current_month)
days_till_end_month = days_in_current_month - today_date.day
# print(days_till_end_month)
start_date = today_date + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date
# print(start_date)
"""
 interest calculate on year annual basis so we need to divided by 12 to get the monthly value then we can multiply
 that with our balance to get the total interest charge
"""
while balance > 0:
    interest_change = (interest_rate / 12) * balance
    balance += interest_change
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

 # instead of above two lines we use terinary conditional like this
    # balance = 0 if balance < 0 else round(balance, 2)

    print(end_date, balance)
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_till_end_month)
