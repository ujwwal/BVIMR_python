def repeat(numTimes):
    def decoratorRepeat(func):
        def wrapper(*args,**kwargs):
            for i in range(numTimes):
                result =func(*args, **kwargs)
                return result
        return wrapper
    return decoratorRepeat

@repeat(numTimes=3)
def greet(name):
    print(f"hello {name}")

greet("alice")  