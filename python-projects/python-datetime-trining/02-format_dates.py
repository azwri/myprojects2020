from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes
now = datetime.now()  # get the current date and time

#### Date Formatting ####
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# Year
print(now.strftime('The current year is %Y'))
print(now.strftime('The current year is %y'))
# Month
print(now.strftime('The current month is %B'))
print(now.strftime('The current month is %b'))
# Day
print(now.strftime('The current day is %d'))


# %c - locale's date and time, %x - locale's date, %X - locale's time
# Local date & time
print(now.strftime('The current local date & time is %c'))
# Local date
print(now.strftime('The current local date is %D'))
# Local time
print(now.strftime('The current local time is %X'))


#### Time Formatting ####
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
# 12-Hour:Minute:Second:AM
print(now.strftime('The current time time is %I:%M:%S %p'))
print(now.strftime('The current time time is %H:%M:%S %p'))  # 24-Hour:Minute
