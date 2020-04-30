from datetime import date, datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = date.today()
print(today)

# Day -> Date day -> Month -> Year
day, date_day, month, year = days[today.weekday()], today.day, today.month, today.year
print(f'Today is {day}, {date_day}/{month}/{year}')



# Get the current time
today = datetime.now()
print(today)
# time
time = datetime.time(today)
print(time)