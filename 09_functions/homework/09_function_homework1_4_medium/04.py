

def nth_fib(n):

    if n == 1:
        return 0
    if n == 2:
        return 1
    # note: we can merge above 2 lines in single condition. Try

    a, b = 0, 1
    n -= 2

    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


for i in range(1, 10):
    print(i, nth_fib(i))

"""
1 0
2 1
3 1
4 2
5 3
6 5
7 8
8 13
9 21
"""