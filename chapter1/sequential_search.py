"""
Problem : n개의 숫자로 이루어진 배열 S에 있는 모든 숫자를 더하여라.
Input : 양수 n, 배열 S (1 ~ n까지의 index)
Output : S에 있는 모든 수를 더한 값
"""


def sequential_search(n: int, S: list, x: int):
    location = 0

    while location <= n and S[location] != x:
        location = location + 1

    if location > n:
        location = 0

    return location


if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in S:
        print("%d - index %d" % (i, sequential_search(len(S), S, i)))