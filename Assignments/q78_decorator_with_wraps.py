from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def square(n: int) -> int:
    """Return the square of n."""
    return n * n

if __name__ == "__main__":
    print("Function name:", square.__name__)
    print("Docstring:", square.__doc__)
    print("Result:", square(7))

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
