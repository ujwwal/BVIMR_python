try:
    number = int(input("pls enter number: "))
    result =10/number
except ValueError:
    print("enter a valid number.")
else:
    print(f"the result is {result}")