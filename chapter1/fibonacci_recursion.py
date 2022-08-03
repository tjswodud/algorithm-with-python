"""
Problem : 피보나치 수열의 n번째 수를 구하여라.
Input : 음이 아닌 정수 n
Output : 피보나치 수열의 n번째 수
"""


def fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(1, 11):
        print("fibonacci(%d) - %d" % (i, fibonacci(i)))
