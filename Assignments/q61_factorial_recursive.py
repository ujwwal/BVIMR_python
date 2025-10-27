def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"{n}! = {factorial(n)}")
    except Exception as e:
        print("Error:", e)