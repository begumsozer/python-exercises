def countdown(n,txt):
  c=""
  for x in range(n,0,-1):
    c+=str(x)+"."
  c+=txt.upper()+"!"
  return(c)

print(countdown(10, "Blast Off"))
