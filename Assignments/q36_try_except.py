# Q36. Try and except.

if __name__ == "__main__":
    try:
        x = int(input("Enter an integer: "))
        print("You entered:", x)
    except ValueError:
        print("That was not an integer!")