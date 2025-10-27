# Q19. Print all the leap years from year 1-2025. Also print the total count.

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

leap_years = [y for y in range(1, 2026) if is_leap(y)]
print("Leap years from 1 to 2025:", leap_years)
print("Total count:", len(leap_years))
print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
