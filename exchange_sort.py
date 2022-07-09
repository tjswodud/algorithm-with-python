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