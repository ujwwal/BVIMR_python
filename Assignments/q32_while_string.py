# Q32. While with string (iterate over string using while).

if __name__ == "__main__":
    s = input("Enter a string: ")
    i = 0
    while i < len(s):
        print(f"{i}: {s[i]}")
        i += 1