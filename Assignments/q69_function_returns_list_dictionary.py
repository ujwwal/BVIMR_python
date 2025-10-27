def list_of_squares(n: int) -> list:
    return [i * i for i in range(1, n + 1)]

def char_frequency(s: str) -> dict:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

if __name__ == "__main__":
    print("Squares up to 10:", list_of_squares(10))
    sample = "abracadabra"
    print(f"Character frequency for '{sample}':", char_frequency(sample))

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
