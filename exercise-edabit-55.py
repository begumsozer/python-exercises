def combinations(*items):
  result=1
  for x in items:
    if x != 0:
      result *= x
  return result

print(combinations(2,3))

print(combinations(3,7,4)) 

print(combinations(2,3,4,5))
