def mystery_func(n):
  str_n=str(n)
  len_str_n=len(str_n)
  output=1
  if len_str_n == 0:
    return ""
  x=1
  while x < len_str_n:
    if str_n[x] == str_n[0]:
      output+=1
    else:
      break
    x+=1
  return str(output)+str_n[0]+mystery_func(str_n[x:])

print(mystery_func(521))
print(mystery_func(5211255))
print(mystery_func(513515))
