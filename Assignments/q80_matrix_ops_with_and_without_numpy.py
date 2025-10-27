if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0],
    ]
    B = [
        [7, 8, 9],
        [2, 3, 4],
        [1, 0, 2],
    ]

    # Without NumPy
    add_res = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
    sub_res = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]
    mul_res = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            mul_res[i][j] = sum(A[i][k] * B[k][j] for k in range(3))
    trans_A = [[A[j][i] for j in range(3)] for i in range(3)]

    print("=== Without NumPy ===")
    print("A + B:", *add_res, sep="\n  ")
    print("A - B:", *sub_res, sep="\n  ")
    print("A * B:", *mul_res, sep="\n  ")
    print("Transpose(A):", *trans_A, sep="\n  ")

    # With NumPy
    try:
        import numpy as np
        a = np.array(A, dtype=float)
        b = np.array(B, dtype=float)
        print("\n=== With NumPy ===")
        print("A + B:\n", a + b)
        print("A - B:\n", a - b)
        print("A * B (matrix product):\n", a @ b)
        print("Transpose(A):\n", a.T)
    except ImportError:
        print("\nNumPy not installed. Skipping NumPy demo.")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
