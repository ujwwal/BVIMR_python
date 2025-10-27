def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
                print(f"[repeat {i+1}/{times}] result: {result}")
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name: str):
    return f"Hello, {name}!"

if __name__ == "__main__":
    greet("Alice")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
