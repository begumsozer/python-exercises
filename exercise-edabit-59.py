def number_groups(group1, group2, group3):
 new=[]
 for x in group1:
  if x in group2 and x not in new:
    new.append(x)
  elif x in group3 and x not in new:
    new.append(x)
 for x in group2:
  if x in group3 and x not in new:
    new.append(x)
 new.sort()
 return new

print(number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) 

print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) )

print(number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]))

print(number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6])))
