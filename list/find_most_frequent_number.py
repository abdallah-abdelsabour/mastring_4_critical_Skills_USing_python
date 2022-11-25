



def find_most_frequent(lst):
   lst.sort()

   most_frequet_elemet = None
   most_freqent_number = 0

   frequent = None
   number = 1

   for indx in range(len(lst)):
    if indx == 0:
      continue
    if lst[indx] == lst[indx -1]:
        frequent = lst[indx]
        number +=1

    else:
      if  number > most_freqent_number :
          most_freqent_number = number
          most_frequet_elemet = frequent
          # reset 
          number = 1

   return most_frequet_elemet ,most_freqent_number




       
value , number  = find_most_frequent([1,1,23,4,4,5,6,6,6])
print(value , "repated"  , number , "time")