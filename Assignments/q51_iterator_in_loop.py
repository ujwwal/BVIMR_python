# Q51. Use iterator inside a loop.

if __name__ == "__main__":
    it = iter([1, 2, 3, 4])
    for x in it:
        print(x, end=" ")
    print()