from datetime import datetime


#_____________________________Read current date
today = datetime.now()
print(today)
#2024-03-15 17:28:29.374230

#_____________________________Read current date
# Attributes :year, month, day, hour, minute, second, and microsecond
today_hour = datetime.now().hour
print(today_hour)
#17
today_month = datetime.now().month
print(today_month)
#3


#______________________________ Format datetime
formatted_today = today.strftime("%d-%m-%Y")
print(formatted_today)
#15-03-2024

formatted_today2 = today.strftime("%d %B %Y")
print(formatted_today2)
#15 March 2024


#____________________________Create own datetime
my_date = datetime(year=2023, month=12, day=13).strftime("%d.%m.%Y")
print(my_date)
#13.12.2023

