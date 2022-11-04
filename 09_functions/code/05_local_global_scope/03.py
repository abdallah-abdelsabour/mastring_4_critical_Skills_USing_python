

b = 20
c = 6


def f():
    global b
    # now the assigned b is actually the global one
    b = c + 1
    print(b)    # 7
    return b


f()
print(b)    # 7


