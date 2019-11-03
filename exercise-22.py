dersler = {
  "mathematic":6, 
  "literature":6,
  "history":2,
  "geography":2,
  "chemistry":2,
  "biology":2,
  "physics":2,
}

print("Lessons and number of hours:")
for x in dersler:
 txt="  {0}:{1}"
 print(txt.format(x,dersler[x]))

print("---------------------------")

while True:
 print("Enter the lesson you want to change:")
 ders=input()
 ders=ders.lower()
 if ders in dersler:  
  x=dersler[ders]
  print("Number of hours=",str(x))
  print("Enter new number of hours:")
  yeni_ders=input()
  dersler[ders]=int(yeni_ders)
 else:
  break

print("---------------------------")
print("Lessons and revised number of hours:")
for x in dersler:
 txt="  {0}:{1}"
 print(txt.format(x,dersler[x]))
