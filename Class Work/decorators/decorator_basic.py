def myDecorator(func):
    def wrapper():
        print("something is happening before the funciton is called")
        func()
        print("something is happening after the function is callled")
    return wrapper

@myDecorator
def sayHello():
    print("hello")

sayHello()