def remove_dups(lst):
  result=[]
  for x in lst:
   if x not in result:
     result.append(x)
  return(result)
