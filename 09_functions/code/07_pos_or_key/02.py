

# x: positional_or_keyword
def f1(x):
    return x+1

f1(10)      # positional argument
f1(x = 10)  # keyword argument

# all arguments before / must be specified by position
# x: positional ONLY  (Python 3.8 and higher)
def f2(x, /):
    return x+1

f2(10)      # positional argument
# TypeError: f2() got some positional-only arguments passed as keyword arguments: 'x'
#f2(x = 10)      # keyword argument

# x: positional_only
# y: positional_or_keyword
def f3(x, /, y):
    return x * y

f3(1, 2)
f3(1, y=2)
#f3(x=1, y=2)

# Optional Reading: https://stackoverflow.com/questions/58477827/why-use-positional-only-arguments-in-python-3-8