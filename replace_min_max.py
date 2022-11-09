

# function replace min vlalue in array to max and max to min 


lst  = list(map(int, input().split()))



def replace_min_max(lst):

  min_value =min(lst)
  max_value = max(lst)
  for indx in range(len(lst)) :
    if lst[indx] == min_value :
      lst[indx]=max_value
    elif lst[indx]==max_value:
      lst[indx]= min_value  


replace_min_max(lst)
print(lst)      