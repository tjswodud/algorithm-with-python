"""
Problem : n개의 아이템을 비내림차순으로 정렬하라.
Input : 양수 n, 배열 S (1 ~ n까지의 index)
Output : 비내림차순으로 정렬된 배열 S
"""


def exchange_sort(n: int, S: list):
    for i in range(0, n):
        for j in range(i + 1, n):
            if S[j] < S[i]:
                # exchange S[i] and S[j]
                temp = S[j]
                S[j] = S[i]
                S[i] = temp


if __name__ == '__main__':
    S = [10, 7, 11, 5, 13, 8]
    exchange_sort(len(S), S)
    print(S)