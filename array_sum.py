def array_sum(n: int, S: list):
    result = 0

    for i in range(0, n):
        result = result + S[i]

    return result


if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('sum : %d' % array_sum(len(S), S))