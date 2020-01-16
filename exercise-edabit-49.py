def accumulating_list(lst):
  total=0
  new=[]
  for x in lst:
    total+=x
    new.append(total)
  return(new)

print(accumulating_list([1, 2, 3, 4]))
