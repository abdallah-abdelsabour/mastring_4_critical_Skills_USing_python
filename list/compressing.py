

def compressing(string):
  frequncy_arry =[]
  letters=[]
  for letter in string:
    if letter not in letters :
      letters.append(letter)
      frequncy_arry.append(f"{string.count(letter)}_{letter}")
  return frequncy_arry
    









if __name__=="__main__":
  result =compressing("z")
  result = sorted(result)
  print(result)