squares = {x**2 for x in range(5)}
print(squares)

#lambda expressinos
numbers = [1,2,3,4]
squared = list(map(lambda x:x**2,numbers))
print(squared)

#write py code to demonstrate function

def greet(name):
    print(f"hello : {name}")
greet("lol")

#summation

def add (a,b):
    return a+b