# number lst 
lst  = list(map(int, input().split()))

# query lst
query  = list(map(int, input().split()))





# my solution 

def Search_by_query(lst, query):
    query_frequency =[-1]*(max(query)+1)
    for item in query :
      for indx in range(len(lst)) :
        if lst[indx] == item:
           query_frequency[item]=indx
    
    # printing meaning 
    
    for  indx in range(len(query_frequency)):
      if query_frequency[indx] > -1 :
        print("query " + str(indx) + " answer " + str(query_frequency[indx]))
    

# def Search_by_query(lst , query):

#    lst.reverse()
#    idx = -1 
#    for q in query :
#       if q in lst:
#         idx = lst.index(q)
#         idx = len(lst) -idx -1 
#       print("query ",q,"answer ",idx )  







    

Search_by_query(lst, query)