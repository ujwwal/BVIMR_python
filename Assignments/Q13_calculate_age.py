# Q13. Calculate your age on given date

from datetime import datetime

dob = datetime(2004, 1, 1)  # Example date of birth
given_date = datetime(2025, 8, 7)
age_years = given_date.year - dob.year - ((given_date.month, given_date.day) < (dob.month, dob.day))
print("Age on", given_date.date(), "is:", age_years, "years")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
