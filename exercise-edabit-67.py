def stupid_addition(a, b): 
 if type(a) == type(b) == int:
  return str(a) + str(b)
 if type(a) == type(b) == str:
  return int(a) + int(b)
