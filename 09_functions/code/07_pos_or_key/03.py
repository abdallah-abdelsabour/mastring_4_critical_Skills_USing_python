

# all arguments after * must be specified by keyword (since python 3)
# x: positional_or_keyword
# y: keyword_only
def f3(x, *, y):
    return x * y

# TypeError: f3() takes 1 positional argument but 2 were given
#f3(1, 2)

f3(1, y=2)
f3(x=1, y=2)

