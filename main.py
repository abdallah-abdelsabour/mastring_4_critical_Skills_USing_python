# home 1
# class Range:

#   def __init__(self,start,end,step):

#     self.start = start 
#     self.end = end 
#     self.step = step


#   def get_next(self):
#     out = None
#     if self.start < self.end :
#      out  =self.start
#      self.start +=self.step  
      
#     return out


#   def has_next(self):
#     if self.start <   self.end :
#       return True
#     # in case end 
#     return False




# range = Range(5, 20, 2)


# while range.has_next():
#   print(range.get_next())


class Range:

  def __init__(self,start,end,step):

    self.start = start 
    self.end = end 
    self.step = step
    self.indx = 0


  def get_next(self):
      ret = self.start , self.indx
      self.start +=self.step
      self.indx += 1
      return ret
  
  def has_next(self):
     if self.step > 1 :
        return  self.end > self.start
     return self.end < self.start 

range = Range(100, 20, -1)


while range.has_next():
  print(range.get_next())