# Q54. Use a generator with a loop.

def simple_generator(n: int):
    for i in range(n):
        yield i


if __name__ == "__main__":
    for val in simple_generator(5):
        print(val, end=" ")
    print()

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
