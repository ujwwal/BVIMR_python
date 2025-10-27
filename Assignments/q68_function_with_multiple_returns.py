def divide_with_remainder(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return divmod(a, b)  # (quotient, remainder)

if __name__ == "__main__":
    a, b = 17, 5
    q, r = divide_with_remainder(a, b)
    print(f"{a} // {b} = {q}, remainder = {r}")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
