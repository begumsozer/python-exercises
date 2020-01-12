def majority_vote(lst):
  a_counter=0
  b_counter=0
  c_counter=0
  total=0
  if len(lst)==0:
    return None
  for x in lst:
    if x=="A":
      a_counter+=1
      total+=1
    elif x=="B":
      b_counter+=1
      total+=1
    elif x=="C":
      c_counter+=1
      total+=1
  if a_counter > len(lst)/2:
    return "A"
  elif b_counter > len(lst)/2:
    return "B"
  elif c_counter > len(lst)/2:
    return "C"
  else:
    return None

print(majority_vote(["A", "B", "B", "A", "C", "C"]))
