"""
Problem : n개의 숫자로 이루어진 배열 S에 있는 모든 숫자를 더하여라.
Input : 양수 n, 배열 S (1 ~ n까지의 index)
Output : S에 있는 모든 수를 더한 값
"""


def array_sum(n: int, S: list):
    result = 0

    for i in range(0, n):
        result = result + S[i]

    return result


if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('sum : %d' % array_sum(len(S), S))