from functools import lru_cache

def fib_iter_upto(max_value: int) -> list:
    seq = []
    a, b = 0, 1
    while a <= max_value:
        seq.append(a)
        a, b = b, a + b
    return seq

@lru_cache(maxsize=None)
def fib_recursive(n: int) -> int:
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == "__main__":
    try:
        n = int(input("Generate Fibonacci numbers up to (max value): "))
        # Non-recursive
        print("Iterative:", fib_iter_upto(n))
        # Recursive up to n
        rec = []
        i = 0
        while True:
            val = fib_recursive(i)
            if val > n:
                break
            rec.append(val)
            i += 1
        print("Recursive:", rec)
    except Exception as e:
        print("Error:", e)