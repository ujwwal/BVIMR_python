# Q18. Print all prime, all perfect and all Armstrong number in a given range

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

start, end = 1, 1000
primes = [i for i in range(start, end+1) if is_prime(i)]
perfects = [i for i in range(start, end+1) if is_perfect(i)]
armstrongs = [i for i in range(start, end+1) if is_armstrong(i)]

print("Primes:", primes)
print("Perfect numbers:", perfects)
print("Armstrong numbers:", armstrongs)
print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
