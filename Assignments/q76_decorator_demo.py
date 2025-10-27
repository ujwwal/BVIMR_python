def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

if __name__ == "__main__":
    add(10, 20)

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
