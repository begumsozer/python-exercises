def larger_than_right(lst):
  result=[]
  len_lst=len(lst)
  for x in range(len_lst):
    for y in range(x+1, len_lst):
      if lst[x] <= lst[y]:
        break
      if y == len_lst-1:
        result.append(lst[x])
  result.append(lst[-1])
  return result
