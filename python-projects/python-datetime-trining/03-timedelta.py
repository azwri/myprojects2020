from datetime import date, time, datetime, timedelta

# basic
print(timedelta(days=365, hours=5, minutes=1))


# today
now = datetime.now()
print(f'Today is {now}')
print(f'One year from now will be in {now + timedelta(days=365)}')
print(f'In 2 days and 12 hours will be in {str(now + timedelta(days=2, hours=12))}')