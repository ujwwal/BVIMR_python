# Q16. Check whether the given number is Armstrong number or not

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

n = 153
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
