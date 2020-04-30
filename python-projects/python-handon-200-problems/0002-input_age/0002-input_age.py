# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import datetime

name = input('What\'s your Name ... ')
while True:
  try:
    age = input('How old are you ... ')
    age = int(age)
    if isinstance(age, int): break
  except:
    print('Enter numbers only.')
_year = datetime.now()
now_year = _year.year
msg = f'Hi {name}, you will be 100 years old in {(100 - age) + now_year}'
print(msg)