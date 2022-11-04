
# enumerate() function returns an enumerated object.
for item in enumerate(range(5, 8)):
    #print(type(item))   # <class 'tuple'>
    idx, value = item
    print(idx, value)
"""
0 5
1 6
2 7  """
for idx, value in enumerate(range(5, 8)):
    print(idx, value)
"""
0 5
1 6
2 7   """
for idx, value in enumerate('ali'):
    print(idx, value)
"""
0 a
1 l
2 i   """
