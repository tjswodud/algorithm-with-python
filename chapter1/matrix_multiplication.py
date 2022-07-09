"""
Problem : 두 개의 nxn 행렬을 곱하여라.
Input : 양수 n, 2차원 정수 배열 A, B (두 배열의 모든 column과 row는 1 ~ n까지의 index)
Output : A와 B의 곱의 결과인 2차원 정수 배열 C (모든 column과 row는 1 ~ n까지의 index)
"""


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