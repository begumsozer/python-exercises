def pos_neg_sort(lst):
  positive=sorted([x for x in lst if x > 0])
  no=0
  for x in range (len(lst)):
    if lst[x] > 0:
      lst[x]=positive[no]
      no+=1
  return lst

print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))
