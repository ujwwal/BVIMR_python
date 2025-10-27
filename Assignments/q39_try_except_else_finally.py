# Q39. Try, except, else, finally.

if __name__ == "__main__":
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Inputs must be integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Cleanup complete (finally).")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
