
def to_number(string):
  digits = '0123456789'
  res = 0
  for char in string:
    res = res *10 + digits.find(char) 
  return res 

if __name__ == "__main__":
  res= to_number("00000546")
  print(res)
  