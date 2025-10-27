# Q14. Check whether given year is Leap year or not

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2024
if is_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
