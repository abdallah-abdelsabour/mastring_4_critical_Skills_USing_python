
def filter(string):

  lst = string.replace(","," ").replace("#"," ").replace("$"," ").split()
  return lst





if __name__ =="__main__":
  result = filter("banana#########n,,banana")
  print(result)