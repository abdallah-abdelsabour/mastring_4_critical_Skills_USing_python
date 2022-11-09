

lst  = list(map(int, input().split()))


def is_array_increasing(lst):
  isIncreasing=True

  for indx in range(len(lst)) :
    if indx == 0:
      continue

    elif  lst[indx] < lst[indx -1 ]:
      isIncreasing = False
  # last result
  return isIncreasing



result = is_array_increasing(lst)
print(result)   



