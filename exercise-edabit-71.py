def number_of_swaps(lst):
  len_lst=len(lst)
  swap=0
  for x in range(1,len_lst):
   number=lst[x]
   index_num=x
   while index_num>0 and lst[index_num-1]>number:
     lst[index_num]=lst[index_num-1]
     swap+=1
     index_num-=1
     lst[index_num]=number
  return swap 
