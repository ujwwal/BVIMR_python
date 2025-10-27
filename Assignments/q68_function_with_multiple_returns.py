def divide_with_remainder(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return divmod(a, b)  # (quotient, remainder)

if __name__ == "__main__":
    a, b = 17, 5
    q, r = divide_with_remainder(a, b)
    print(f"{a} // {b} = {q}, remainder = {r}")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
