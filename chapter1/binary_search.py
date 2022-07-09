def binary_search(n: int, S: list, x: int):
    low = 1
    high = n
    location = 0

    while low <= high and location == 0:
        mid = int(((low + high) / 2) // 1)  # floor function

        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return location


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in S:
        print("%d - index %d" % (i, binary_search(len(S), S, i)))
