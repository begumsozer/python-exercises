def calculate_score(games):  
 b=0
 a=0
 print(b)
 for x in games:
  g1=x[0]
  g2=x[1]
  
  if g1 == "R" and g2 == "P":
   b=b+1
  elif g1 == "R" and g2 == "S":
   a=a+1
  elif g1 == "P" and g2 == "R":
   a=a+1
  elif g1 == "P" and g2 == "S":
   b=b+1
  elif g1 == 'S' and g2 == 'R':
   b=b+1
  elif g1 == 'S' and g2 == 'P':
   a=a+1

 if b > a:
  return("Benson")
 elif a > b:
  return("Abigail")
 else:
  return("Tie")
