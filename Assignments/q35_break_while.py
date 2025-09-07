# Q35. Break statement with while loop.

if __name__ == "__main__":
    i = 0
    while True:
        i += 1
        if i == 5:
            print("Breaking at i =", i)
            break
        print("i =", i)