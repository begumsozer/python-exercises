def equal(a,b,c):
  if a==b and a==c:
    return 3
  elif a==b or a==c or b==c:
    return 2
  else:
    return 0

print(equal(6,3,3))
