# 


# find frequency number without nested array 

lst  = list(map(int, input().split()))






def fast_find_frequency(lst):

  # create frequency array 
  frequency_arry = [0] * (max(lst) +1 )
  
  for item in lst :
    frequency_arry[item] +=1

  most_value = frequency_arry.index(max(frequency_arry))

  return most_value , frequency_arry[most_value]




result = fast_find_frequency(lst)
print(result)
    

    