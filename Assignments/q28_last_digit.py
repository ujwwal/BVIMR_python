# Q28. Print last digit of a given integer number.

def last_digit(n: int) -> int:
    return abs(n) % 10


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print("Last digit:", last_digit(n))

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
