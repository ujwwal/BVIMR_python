# Q45. Create and access nested tuples.

if __name__ == "__main__":
    t = (1, (2, 3), (4, (5, 6)))
    print("Nested tuple:", t)
    print("t[1][1]:", t[1][1])
    print("t[2][1][0]:", t[2][1][0])