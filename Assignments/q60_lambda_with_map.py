if __name__ == "__main__":
    nums = list(range(1, 8))
    print("Original:", nums)

    squares = list(map(lambda x: x * x, nums))
    print("Squares:", squares)

    labels = list(map(lambda x: f"n={x}", nums))
    print("Labeled:", labels)

    triplets = list(map(lambda x: (x, x ** 2, x ** 3), nums))
    print("Tuples (n, n^2, n^3):", triplets)

    a = [1, 2, 3]
    b = [10, 20, 30]
    sums = list(map(lambda t: t[0] + t[1], zip(a, b)))
    print("Element-wise sums of a and b:", sums)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
