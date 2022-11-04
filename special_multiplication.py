# Homework 1: Special Multiplication
# ●
# ●
# Develop function: def special_multiplication(string):
# It returns a string where each character is repeated according to its position
# ○
# ○
# ○
# Input: abcxf
# Output: abbcccxxxxfffff
# Observe
# ■ a repeated once
# ■ b twice
# ■ c 3 times
# ■ x 4 times
# ■ And so on


def special_multiplication(string):

  result=""

  for indx , letter in enumerate(string):
      indx+=1
      result+=letter*indx
  return result





print(special_multiplication("ABC"))