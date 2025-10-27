# Q46. Set operations.

if __name__ == "__main__":
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("A:", a)
    print("B:", b)
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference A-B:", a - b)
    print("Symmetric difference:", a ^ b)
    a.add(10)
    a.discard(2)
    print("Modified A:", a)
    print("Is subset?", {3, 4}.issubset(a))
    print("Is superset?", a.issuperset({3, 4}))

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
