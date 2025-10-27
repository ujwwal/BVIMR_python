if __name__ == "__main__":
    s = input("Enter a string: ")
    # Clean alphanumeric and lowercase
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    # Reverse manually
    rev = ""
    i = len(cleaned) - 1
    while i >= 0:
        rev += cleaned[i]
        i -= 1

    print("Palindrome?", "Yes" if cleaned == rev else "No")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
