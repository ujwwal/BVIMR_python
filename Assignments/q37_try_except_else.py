# Q37. Try, except, else.

if __name__ == "__main__":
    try:
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid integer.")
    else:
        print("Square is:", x * x)