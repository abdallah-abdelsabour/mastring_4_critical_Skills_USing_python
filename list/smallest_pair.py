# arry of  N number 
# print smallest A[i]+A[j]+A[i]-[j]


def smallest_pair(lst):

    smallest_pair = 10000000
    
    for i in range(len(lst)):
      for j in range(len(lst)):
        if smallest_pair >  lst[i]+lst[j]+i-j :
          smallest_pair = lst[i]+lst[j]+i-j
    return smallest_pair




result = smallest_pair([20,1,9,4])
print(result)
