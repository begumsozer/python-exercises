def censor(s):
  lst=s.split()
  words=""
  for x in lst:
    if len(x) > 4:
      words += "*"*len(x)
    else:
      words += x
    words += " "
  length=len(words)
  return words[0:length-1]

print(censor("The code is fourty"))

print(censor("Two plus three is five"))

print(censor("aaaa aaaaa 1234 12345"))
