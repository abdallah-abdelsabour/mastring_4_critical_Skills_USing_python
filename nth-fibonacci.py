# Homework 4: Get nth-fibonacci
# ●
# Fibonacci is a popular sequence: 0, 1, 1, 2, 3, 5, 8, 13,
# 21, …
# ○
# ○
# ●
# Every number is sum of last 2 numbers
# E.g. 13 = 5 + 8
# Write function: nth_fib(n)
# ○
# ○
# That returns the nth term
# Hint: Simple loop








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

