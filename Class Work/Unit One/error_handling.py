try:
    number = int(input("enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")