#generate, store and print 10 random numbers
import random
y=0
n=0
sayılar = []
aynı_olmayan_sayılar = []
print("random numbers generated")
while y <= 10:
  x = random.randint(1,5)
  print(x)
  sayılar.append(x)
  y=y+1

#remove duplicate numbers and store
y=0
while y<=10:
 #aynı_olmayan_sayılar[y]=sayılar[y]
 if sayılar[y] not in aynı_olmayan_sayılar:
  aynı_olmayan_sayılar.append(sayılar[y])
 y=y+1
print("******************")

#print the unique numbers
y=0
while y<len(aynı_olmayan_sayılar):
  print(aynı_olmayan_sayılar[y])
  y=y+1

#find and print occurrunce of each unique number
y=0
while y<len(aynı_olmayan_sayılar):
 x=sayılar.count(aynı_olmayan_sayılar[y])
 txt="{0} occured {1} times"
 print(txt.format(aynı_olmayan_sayılar[y],x))
 y=y+1
