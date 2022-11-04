
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def nth_prime(n):
    start = 2
    while n > 0:
        if is_prime(start):
            n -= 1
            if n == 0:
                return start
        start += 1

    return -1   # not reachable


for i in range(1, 10):
    print(i, nth_prime(i))

"""
1 2
2 3
3 5
4 7
5 11
6 13
7 17
8 19
9 23
"""

