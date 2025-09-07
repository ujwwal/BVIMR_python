# Q37. Try, except, else, finally.

if __name__ == "__main__":
    try:
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid integer.")
    else:
        print("Square is:", x * x)
    finally:
        print("Execution completed.")