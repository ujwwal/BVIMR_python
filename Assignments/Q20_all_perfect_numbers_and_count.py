# Q20. Print all the perfect numbers from 1-2025. Also print the total count.

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

perfect_numbers = [i for i in range(1, 2026) if is_perfect(i)]
print("Perfect numbers from 1 to 2025:", perfect_numbers)
print("Total count:", len(perfect_numbers))
print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")