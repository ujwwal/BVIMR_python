def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_two_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    while True:
        print("\n===== Calculator Menu =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        elif choice in {"1", "2", "3", "4"}:
            a, b = get_two_numbers()
            try:
                if choice == "1":
                    print(f"Result: {a} + {b} = {add(a,b)}")
                elif choice == "2":
                    print(f"Result: {a} - {b} = {sub(a,b)}")
                elif choice == "3":
                    print(f"Result: {a} * {b} = {mul(a,b)}")
                elif choice == "4":
                    print(f"Result: {a} / {b} = {div(a,b)}")
            except ZeroDivisionError as e:
                print("Error:", e)
        else:
            print("Invalid choice. Please select 1-5.")