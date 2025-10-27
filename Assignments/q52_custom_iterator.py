# Q52. Create and use a custom iterator.

class CountDown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


if __name__ == "__main__":
    for n in CountDown(5):
        print(n, end=" ")
    print()

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
