#produce 10 random numbers, store and print them
import random
y=0
sayılar = []
print("random numbers generated")
while y < 10:
  x = random.randint(1,100)
  print(x)
  sayılar.append(x)
  y=y+1

#print random numbers in the reversed order
print("random numbers in the reversed order")
n=9
while n>=0:
  print(sayılar[n])
  n=n-1

#find the smallest and largest random number
m=1
kucuk_sayı=sayılar[0]
buyuk_sayı=sayılar[0]
while m<10:
  if sayılar[m]<kucuk_sayı:
    kucuk_sayı=sayılar[m]
  elif sayılar[m]>buyuk_sayı:
    buyuk_sayı=sayılar[m]
  m=m+1
print("largest number: ", buyuk_sayı)  
print("smallest number: ", kucuk_sayı)
