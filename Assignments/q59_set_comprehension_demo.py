if __name__ == "__main__":
    squares = {x * x for x in range(1, 11)}
    print("Squares 1..10:", squares)

    text = "Set comprehensions capture unique elements!"
    vowels = {ch.lower() for ch in text if ch.lower() in "aeiou"}
    print("Vowels present:", vowels)

    nums = [1, 2, 2, 3, 4, 4, 5, 6]
    even_squares = {n * n for n in nums if n % 2 == 0}
    print("Unique even squares from list:", even_squares)

    pairs_sum_even = {(a, b) for a in range(4) for b in range(4) if (a + b) % 2 == 0}
    print("Pairs with even sum:", pairs_sum_even)

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
