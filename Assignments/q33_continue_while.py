# Q33. Continue statement with while loop.

if __name__ == "__main__":
    i = 0
    while i < 10:
        i += 1
        if i % 3 == 0:
            continue
        print(i, end=" ")
    print()