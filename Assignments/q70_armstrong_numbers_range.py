if __name__ == "__main__":
    try:
        a = int(input("Enter start of range: "))
        b = int(input("Enter end of range: "))
        if a > b:
            a, b = b, a
        armstrongs = []
        for n in range(a, b + 1):
            s = str(n)
            k = len(s)
            total = 0
            for d in s:
                total += int(d) ** k
            if total == n:
                armstrongs.append(n)
        print("Armstrong numbers:", armstrongs)
    except Exception as e:
        print("Error:", e)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
