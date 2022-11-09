# number lst 
lst  = list(map(int, input().split()))

# query lst
query  = list(map(int, input().split()))






def Search_by_query(lst, query):
    query_frequency =[0]*(max(query)+1)
    for item in query :
      for indx in range(len(lst)) :
        if lst[indx] == item:
           query_frequency[item]=indx
    
    # printing meaning 
    
    for  indx in range(len(query_frequency)):
      if query_frequency[indx] > 0 :
        print("query " + str(indx) + " answer " + str(query_frequency[indx]))
    

Search_by_query(lst, query)