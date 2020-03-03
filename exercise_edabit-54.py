def is_shuffled_well(lst):
  for x in range(len(lst)-1):
    if (lst[x]-1 == lst[x-1] and lst[x]+1 == lst[x+1]) or (lst[x]-1 == lst[x+1] and lst[x]+1 == lst[x-1]):
      return False
  return True

print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
