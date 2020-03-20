def look_and_say(n):
  str_n=str(n)
  length=len(str_n)
  if length%2==1:
    return "invalid"
  num=""
  for x in range(0,length,2):
    pair=str_n[x:x+2]
    num+=pair[1]*int(pair[0])
  return int(num)

print(look_and_say(95))

print(look_and_say(1213141516171819))

print(look_and_say(120520))

print(look_and_say(231))
