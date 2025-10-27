# Q43. List comprehensions.

if __name__ == "__main__":
    squares = [x * x for x in range(1, 11)]
    evens = [x for x in range(20) if x % 2 == 0]
    pairs = [(i, j) for i in range(3) for j in range(3)]
    print("Squares:", squares)
    print("Evens:", evens)
    print("Pairs:", pairs)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
