"""
Problem : 아이템 x가 n개의 아이템을 갖는 정렬된 배열 S에 존재하는지 확인하라.
Input : 양수 n, (비내림차순으로 정렬된) 배열 S (1 ~ n까지의 index), 아이템 x
Output : location. S 안에서의 x의 위치 (index) (x가 S 안에 없다면 0을 반환)
"""


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
