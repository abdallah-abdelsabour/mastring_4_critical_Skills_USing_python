
str = "123456789987654321"

def is_palinrome(str):
  low = 0
  heigh = len(str) -1 
  while heigh > low:
    if str[heigh] != str[low]:
       return False
    low +=1
    heigh -=1   
  return True


res = is_palinrome(str)
print(res)

# mostafa Solution 

def is_palinrome_2(str):
 
 return str == str[::-1]

most_result = is_palinrome_2(str) 
print(most_result)