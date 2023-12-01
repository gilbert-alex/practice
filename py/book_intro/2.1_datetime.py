# examples for the datatime module

import datetime as dt

# store today's date as a variable
today = dt.date.today()

# store a static date as a variable
last_of_teens = dt.date(2019, 12, 31)

print("date class")
print(today)
print(last_of_teens)

# isolate month, day and year from a date
print("\nisolate parts of date class")
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

# print with format strings
print("\nformat strings:")
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m/%d/%y}"
print(todays_date)