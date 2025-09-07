# Q30. Continue statement with for loop.

if __name__ == "__main__":
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()