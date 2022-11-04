

b = 20
c = 6


def f():
    # b is local NOT global. It doesn't affect global one
    # c not in local, but in global, so used
    b = c + 1
    print(b)    # 7
    return b


f()
print(b)    # 20 NOT 7

b = f()
print(b)    # 7

