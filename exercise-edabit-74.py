def reverse(txt):
  result=""
  reverse_txt=[x for x in txt[::-1]if x.isalpha()]
  for i in txt:
    if i.isdigit():
      result+=i
    else:
      result+=reverse_txt.pop(0)
  return result
