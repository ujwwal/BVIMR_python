if __name__ == "__main__":
    s = input("Enter a string: ")
    out = ""
    i = len(s) - 1
    while i >= 0:
        out += s[i]
        i -= 1
    print("Reversed:", out)