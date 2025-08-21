# Q15. Check whether the given number is perfect number or not

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

n = 28
if is_perfect(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")