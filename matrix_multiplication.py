def matrix_multiplication(n: int, A: list, B: list, C: list):
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = 0
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C


if __name__ == '__main__':
    A = [[2, 3], [4, 1]]
    B = [[5, 7], [6, 8]]
    C = [[0, 0], [0, 0]]

    print("--- matrix A ---")
    for i in A:
        for j in i:
            print(j, end=' ')
        print('')

    print('\n')

    print("--- matrix B ---")
    for i in B:
        for j in i:
            print(j, end=' ')
        print('')

    print('\n')

    print("--- A x B ---")
    matrix_multiplication(2, A, B, C)
    for i in C:
        for j in i:
            print(j, end=' ')
        print('')