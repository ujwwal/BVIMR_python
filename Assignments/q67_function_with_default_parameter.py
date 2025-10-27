def power(base: float, exp: float = 2) -> float:
    return base ** exp

if __name__ == "__main__":
    print("power(5) =", power(5))          # default exp=2
    print("power(2, 3) =", power(2, 3))    # 8
    print("power(9, 0.5) =", power(9, 0.5))  # 3.0

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
