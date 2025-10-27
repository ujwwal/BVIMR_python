# Q50. Built-in iterators.

if __name__ == "__main__":
    data = [10, 20, 30]
    it = iter(data)
    try:
        print("next:", next(it))
        print("next:", next(it))
        print("next:", next(it))
        print("next:", next(it))  # will raise StopIteration
    except StopIteration:
        print("Iterator exhausted.")

    s = "abc"
    print("Iterating over string with iter/next:")
    sit = iter(s)
    try:
        while True:
            print(next(sit), end=" ")
    except StopIteration:
        print()

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
