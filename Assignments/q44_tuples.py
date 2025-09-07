# Q44. Create and access tuples.

if __name__ == "__main__":
    t = (1, 2, 3, "python")
    print("Tuple:", t)
    print("First:", t[0], "Last:", t[-1])
    a, b, c, d = t
    print("Unpacked:", a, b, c, d)