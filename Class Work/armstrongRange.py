def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end}:")
for n in range(start, end + 1):
    if is_armstrong(n):
        print(n)