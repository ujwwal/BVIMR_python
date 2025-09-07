# Q38. Try, except, finally.

if __name__ == "__main__":
    try:
        x = int(input("Enter a divisor of 10: "))
        print("10 / x =", 10 / x)
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)
    finally:
        print("This runs no matter what (finally).")