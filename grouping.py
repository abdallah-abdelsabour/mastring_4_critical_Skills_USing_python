


# string = "aaaaaasSddeefff"

# group = string[0]
# for indx , letter  in enumerate(string):
#   if indx == 0 :
#     continue
#   if string[indx].lower() == string[indx -1 ].lower():
#     group+=string[indx]
#   else:
#     print(group,end=",")
#     group=string[indx] 


# mostafa sloution     #  
string = "aabbcdd"

start_indx=0 
res = []
for indx in range(1,len(string)):
  if string[indx].lower() !=string[indx - 1].lower():
    res.append(string[start_indx:indx])
    start_indx = indx
res = ",".join(res)
print(res)     



    




