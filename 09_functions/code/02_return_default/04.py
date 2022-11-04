

# a, b: non-default argument
# c, d: default argument
# the function accepts from 2 to 4 arguments
def my_sum(a, b, c = 1, d = 2):
    return a + b + c + d


print(my_sum(1, 2, 3, 4))   # 10
print(my_sum(3, 7))         # 13

# TypeError: my_sum() takes from 2 to 4 positional arguments but 5 were given
#my_sum(1, 2, 3, 4, 5)

# SyntaxError: non-default argument follows default argument
#def my_sum(a = 1, b, c = 1, d = 2):
#   return a + b + c + d

