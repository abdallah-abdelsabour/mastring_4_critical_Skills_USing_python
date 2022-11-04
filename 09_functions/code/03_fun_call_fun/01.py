
x = 1
y = 2

def our_abs(num):
    if num >= 0:
        return num
    return -num


def our_max2(first, second):
    first = our_abs(first)
    second = our_abs(second)

    if first > second:
        return first
    return second


print(our_max2(2, 5))   # 5
print(our_max2(2, -5))  # 5
