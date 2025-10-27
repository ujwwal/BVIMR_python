"""
myutils: A simple user-defined module with utility functions.

Functions:
- is_prime(n): check if n is prime
- gcd(a, b): greatest common divisor
- lcm(a, b): least common multiple
- mean(values): arithmetic mean of a sequence
- greet(name): return a greeting string
"""

__all__ = ["is_prime", "gcd", "lcm", "mean", "greet"]

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    g = gcd(a, b)
    return 0 if g == 0 else abs(a // g * b)

def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    total = 0.0
    count = 0
    for v in values:
        total += v
        count += 1
    return total / count

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Demo myutils:")
    print("is_prime(29):", is_prime(29))
    print("gcd(54, 24):", gcd(54, 24))
    print("lcm(12, 18):", lcm(12, 18))
    print("mean([1,2,3,4,5]):", mean([1, 2, 3, 4, 5]))
    print(greet("Alice"))