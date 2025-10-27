if __name__ == "__main__":
    s = input("Enter a string: ")
    out = ""
    i = len(s) - 1
    while i >= 0:
        out += s[i]
        i -= 1
    print("Reversed:", out)

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
