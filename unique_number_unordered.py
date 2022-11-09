
# number lst 
# lst  = list(map(int, input().split()))



def unique_number_list(lst):

  unique_list =[]
  for element in lst:
    if element not in unique_list :
      unique_list.append(element)
  return unique_list

result = unique_number_list([1,6,3,4,5,6,6,6,1,2,5,3,1 ])
print(result)