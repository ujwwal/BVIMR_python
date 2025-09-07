# Q53. Create a simple generator.

def simple_generator(n: int):
    for i in range(n):
        yield i


if __name__ == "__main__":
    # Demo
    for v in simple_generator(5):
        print(v, end=" ")
    print()