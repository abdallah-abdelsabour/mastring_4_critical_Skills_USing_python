

# The default type of parameter in python is positional or keyword
def f(a, b, c, d, e = 10):
    print(a, b, c, d, e)

# positional arguments
f(1, 2, 3, 4, 5)                # 1 2 3 4 5

# keyword arguments in order
f(a=1, b=2, c=3, d=4, e=5)      # 1 2 3 4 5

# keyword arguments out of order
f(e=5, b=2, c=3, d=4, a=1)      # 1 2 3 4 5

# 2 positionals, 3 keyword arguments
f(1, 2, c=3, d=4, e=5)      # 1 2 3 4 5

# 2 positionals, 2 keyword arguments, 1 default
f(1, 2, d=4, c=3)           # 1 2 3 4 10

#TypeError: f() got an unexpected keyword argument 'k'
#f(1, 2, d=4, k=3)

# positional arguments must all come before any keyword arguments
# SyntaxError: positional argument follows keyword argument
#f(d=4, c=3, 1, 2)

