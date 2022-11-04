# Homework 2: Max of 6 numbers
# ●
# ●
# Develop these 4 functions to help
# compute maximum of 6 numbers
# Each function should be only a single
# line of code
# ○
# Hint: make use of the other functions

# f
def my_max2(a,b):

  max= a if a > b else b
  return max


# fun
def my_max3(a,b,c):
  return my_max2(my_max2(a,b), c)
# fun 
 
def my_max4(a,b,c,d):
   return my_max2(my_max3(a,b,c), d)

# fun 
def my_max5(a,b,c,d,e):
  return my_max2(my_max4(a, b, c, d), e)


# fun
def my_max6(a,b,c,d,e,f):
  return my_max2(my_max5(a, b, c, d, e), f)





# solution 
print(my_max6(4, 20, 6, 10, 5, 1))