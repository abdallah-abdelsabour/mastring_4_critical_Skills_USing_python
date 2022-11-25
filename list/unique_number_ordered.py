



def unique_number_orderd(lst):

  unique_list = []
  temp = None
  for item in lst :
    if item !=temp :
      unique_list.append(item)
      temp = item

  return unique_list  


result = unique_number_orderd([1,1,1,2,2,4,4,5,5,1])

print(result)
f




