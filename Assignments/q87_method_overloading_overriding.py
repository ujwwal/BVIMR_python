from functools import singledispatch

# Overloading via argument count
def area(*args):
    """
    area(r) -> circle area (pi*r^2)
    area(l, w) -> rectangle area (l*w)
    area(a, b, c) -> triangle area via Heron's formula
    """
    import math
    if len(args) == 1:
        (r,) = args
        return math.pi * r * r
    elif len(args) == 2:
        l, w = args
        return l * w
    elif len(args) == 3:
        a, b, c = args
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        raise TypeError("Unsupported number of arguments")

# Overloading by type with singledispatch
@singledispatch
def stringify(value):
    return f"Object({value})"

@stringify.register
def _(value: int):
    return f"Int({value})"

@stringify.register
def _(value: str):
    return f"Str('{value}')"

# Overriding via inheritance
class Animal:
    def speak(self) -> str:
        return "Some generic sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

if __name__ == "__main__":
    # Overloading demos
    print("area(5) [circle]:", area(5))
    print("area(4, 6) [rectangle]:", area(4, 6))
    print("area(3, 4, 5) [triangle]:", area(3, 4, 5))
    print("stringify(42):", stringify(42))
    print("stringify('hello'):", stringify("hello"))
    print("stringify(3.14):", stringify(3.14))

    # Overriding demos
    animals = [Animal(), Dog(), Cat()]
    for a in animals:
        print(f"{a.__class__.__name__} speaks:", a.speak())