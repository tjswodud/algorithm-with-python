"""
Problem : 피보나치 수열의 n번째 수를 구하여라.
Input : 음이 아닌 정수 n
Output : 피보나치 수열의 n번째 수
"""

def fibonacci_iterative(n: int):
    f = []
    for i in range(0, n + 1):
        f.append(i)

    f[0] = 0

    if n > 0:
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

    return f[n]


if __name__ == "__main__":
    for i in range(1, 11):
        print("fibonacci(%d) - %d" % (i, fibonacci_iterative(i)))
