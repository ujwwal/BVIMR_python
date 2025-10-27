# Q55. Chain generators.

def evens(n: int):
    for i in range(0, n + 1, 2):
        yield i


def odds(n: int):
    for i in range(1, n + 1, 2):
        yield i


def chained(n: int):
    # Chain using yield from
    yield from evens(n)
    yield from odds(n)

if __name__ == "__main__":
    n = 10
    print("Chained with yield from:", *chained(n))

    from itertools import chain
    print("Chained with itertools.chain:", *chain(evens(n), odds(n)))

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
