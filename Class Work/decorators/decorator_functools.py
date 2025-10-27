import functools

def myDecorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("something is happening before the function is called")
        result = func(*args,**kwargs)
        print("something is happening after the functoin is called")
        return result
    return wrapper

@myDecorator
def sayHello():
    '''this says hello'''
    print("hello")

print(sayHello.__name__)
print(sayHello.__doc__)