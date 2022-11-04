

# parameter: the variable used in defining the function
# first and second are called: parameters
def our_print(first, second):
    print('Sum =', first + second)
    print('Multiplication =', first * second)


# argument is an expression PASSED to the function
# first, 2 * 3 + 1 are arguments
first = 1
our_print(first, 2 * 3 + 1)
