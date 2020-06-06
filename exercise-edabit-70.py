def plus_sign(txt):
  if len(txt) < 3:
    return False
  for x in range(1,len(txt)-1):
    if txt[x].isalpha():
      if txt[x-1] != "+" or txt[x+1] != "+":
        return False
  return True
