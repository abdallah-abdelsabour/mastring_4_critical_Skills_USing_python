
def f():
    return 1, 2, 3

a, b, c = f()
print(a, b, c)  # 1 2 3

together = f()
print(type(together))   # <class 'tuple'>

x, y, z = together      # unpack
print(x, y, z)  # 1 2 3

# ValueError: too many values to unpack (expected 2)
#x, y = together

# ValueError: not enough values to unpack (expected 5, got 3)
#x, y, z, w1, w2 = together
#print(w1)

my_tuple = (5, 6, 7)    # Create tuple
x, y, z = together      # unpack

# More on tuples later

