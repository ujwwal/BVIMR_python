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

    # Addition
    add_res = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
    # Subtraction
    sub_res = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]
    # Multiplication
    mul_res = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            mul_res[i][j] = sum(A[i][k] * B[k][j] for k in range(3))
    # Transpose of A
    trans_A = [[A[j][i] for j in range(3)] for i in range(3)]

    print("Matrix A:", *A, sep="\n  ")
    print("Matrix B:", *B, sep="\n  ")
    print("A + B:", *add_res, sep="\n  ")
    print("A - B:", *sub_res, sep="\n  ")
    print("A * B:", *mul_res, sep="\n  ")
    print("Transpose(A):", *trans_A, sep="\n  ")

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
