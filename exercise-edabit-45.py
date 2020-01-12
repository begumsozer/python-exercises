def rolls(lst):
  sum=0
  if len(lst)<3:
    return(sum)
  for x in lst:
    if x > 6 or x < 1:
      return(sum)
  sum=lst[0]
  for x in range(1,len(lst)):
    if lst[x-1]==6:
      sum+=(lst[x]*2)
    elif lst[x-1]!=1:
      sum+=lst[x]
  return(sum)

print(rolls([2,6,2,5]))
print(rolls([2,2]))
print(rolls([2,6,2,7]))
print(rolls([2,0,2,5]))
