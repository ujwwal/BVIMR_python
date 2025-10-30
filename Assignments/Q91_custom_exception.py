class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_value(x):
    if x < 0:
        raise CustomError("Value must be non-negative")
    return x

try:
    check_value(-5)
except CustomError as e:
    print(f"Caught custom exception: {e}")

    
print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
